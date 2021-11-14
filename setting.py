# 日志配置
LOG_SETTING = {
    "log_level": "DEBUG",
    "sh_level": "ERROR",
    "fh_level": "DEBUG",
    "file_name": "test.log"
}

# app启动项设置
CAP = {
    # 设备操作系统
    "platformName": "Android",
    # 设备名称(随意填写)
    "deviceName": "HuaWeiP30",
    # 应用程序的包名
    "appPackage": "com.tencent.wework",
    # 应用程序的启动页面
    "appActivity": ".launch.LaunchSplashActivity",
    # 不重置app
    "noReset": "true"
}

# 服务的地址
REMOTE_DIR = "http://127.0.0.1:4723/wd/hub"
