import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_PATH = os.path.join(BASE_DIR, r"test_result/logs")
IMG_PATH = os.path.join(BASE_DIR, r"test_result/image")
REPORT_PATH = os.path.join(BASE_DIR, r"test_result/report")
