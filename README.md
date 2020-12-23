# 微信朋友圈图片抓取

## 首次运行必要条件

1. 手机开启usb调试：设置-开发者选项-usb调试
2. 手机与电脑通过usb连接
3. 安装python包 pip install -r requirements.txt
4. 安装apk文件夹下的两个app，或直接运行main.py, 会自动安装app到手机


## 抓取步骤

1. 登录微信，手动进入微信朋友圈页面
2. 运行 python main.py
3. 图片文件存储在当前目录pics下面，若需修改存储路径，可修改main.py里的SAVE_PATH变量

## 常见问题

1. 运行时报权限错误，给文件夹授权 chmod 777 文件夹名
2. 抓取原理为模拟人点击图片，可能存在误点情况，需要人工矫正
3. 若网络较慢，图片加载不完，可修改main.py里的SLEEP_TIME

