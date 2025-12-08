# toolkit/logger.py
import logging
import os

# 確保 logs 資料夾存在
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "test_run.log")

# 基本設定：輸出到 console + 檔案
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[
        logging.StreamHandler(),              # 終端機
        logging.FileHandler(LOG_FILE, encoding="utf-8")  # 檔案
    ],
)

def get_logger(name: str = __name__):
    return logging.getLogger(name)
