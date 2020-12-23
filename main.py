# -*- encoding=utf8 -*-
__author__ = "liubo"

import numpy as np
from PIL import Image
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

SAVE_PATH = "./pics"
SLEEP_TIME = 5


class WeChatCircleSpider:
    def __init__(self):
        init_device("Android")
        self.screen_width, self.screen_heigth = device().get_current_resolution()

    def clear_black(self, img_path):
        """
        清除黑边
        Args:
            img_path: 图片路径

        Returns:

        """
        img = Image.open(img_path)
        img_array = np.array(img.convert("L"), "f")

        img_rows, img_cols = img_array.shape

        # 从中心点向下查找黑边
        bottom_pos = img_rows
        i = img_rows // 2
        while i + 1 < img_rows:
            sum = img_array[i : i + 1, :].sum()
            if sum < 1000:
                bottom_pos = i
                break
            i += 1

        # 从中心点向上查找黑边
        top_pos = 0
        i = img_rows // 2
        while i - 1 > 0:
            sum = img_array[i - 1 : i, :].sum()
            if sum < 1000:
                top_pos = i
                break
            i -= 1

        # 从中心点向左找黑边
        left_pos = 0
        i = img_cols // 2
        while i - 1 > 0:
            sum = img_array[:, i - 1 : i].sum()
            if sum < 10000:
                left_pos = i
                break
            i -= 1

        # 从中心点向右找黑边
        right_pos = img_cols
        i = img_cols // 2
        while i + 1 < img_cols:
            sum = img_array[:, i : i + 1].sum()
            if sum < 10000:
                right_pos = i
                break
            i += 1

        cropped_img = img.crop((left_pos, top_pos, right_pos, bottom_pos))
        cropped_img.save(img_path)

    def crawl(self):
        # 点击图片 下滑
        while True:
            poco = AndroidUiautomationPoco(
                use_airtest_input=True, screenshot_each_action=False
            )

            have_pic = poco("com.tencent.mm:id/ed3").exists()
            if have_pic:
                pics = poco("com.tencent.mm:id/ed3").children()
                for pic in pics:
                    pic.click()
                    time.sleep(SLEEP_TIME)
                    filename = "{}/{}.jpg".format(SAVE_PATH, int(time.time()))
                    snapshot(filename=filename, quality=99, max_size=1200)
                    self.clear_black(filename)
                    print("save image to {}".format(filename))
                    touch([self.screen_width * 0.5, self.screen_heigth * 0.5])
                    time.sleep(1)

            swipe(
                (self.screen_width * 0.5, self.screen_heigth),
                vector=[0, -0.8],
                duration=1,
            )


if __name__ == "__main__":
    spider = WeChatCircleSpider()
    spider.crawl()
