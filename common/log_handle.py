import logging
import os
from common.path_handle import LOG_PATH

from setting import LOG_SETTING


def set_log(log_level, fh_level, sh_level, log_file_name):
    logger = logging.getLogger("po_framework")
    logger.setLevel(log_level)
    # 设置控制台日志输出
    sh = logging.StreamHandler()
    sh.setLevel(sh_level)
    logger.addHandler(sh)
    # 设置文件日志输出
    fh = logging.FileHandler(log_file_name, encoding="utf-8")
    fh.setLevel(fh_level)
    logger.addHandler(fh)

    # 设置日志输出格式
    matter = logging.Formatter('%(asctime)s-[%(filename)s-->line:%(lineno)d]- %(levelname)s: %(message)s')
    sh.setFormatter(matter)
    fh.setFormatter(matter)
    return logger


log = set_log(
    log_level=LOG_SETTING["log_level"],
    fh_level=LOG_SETTING["fh_level"],
    sh_level=LOG_SETTING["sh_level"],
    log_file_name=os.path.join(LOG_PATH, LOG_SETTING["file_name"])
)
