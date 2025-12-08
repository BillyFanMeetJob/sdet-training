# toolkit/web_toolkit.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import config as C  # 直接整個模組 import，不用一個一個 from
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def create_driver(timeout: int | None = None):
    if timeout is None:
        timeout = C.DEFAULT_TIMEOUT

    chrome_options = Options()
    if C.HEADLESS:
        chrome_options.add_argument("--headless=new")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, timeout)
    return driver, wait

def take_screenshot(driver, name_prefix="error"):
    """
    依照目前環境 (DEV / UAT / SIT / PROD)
    將 screenshot 存到專屬資料夾。
    """
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"{name_prefix}_{timestamp}.png"
    filepath = os.path.join(C.SCREENSHOT_DIR, filename)

    driver.save_screenshot(filepath)
    return filepath

def wait_and_type(wait, by:By, locator: str, text: str, clear: bool = True):
    """
    通用輸入文字動作：
    - 等待元素可見
    - 選擇性清空
    - send_keys
    """
    elem = wait.until(EC.visibility_of_element_located((by, locator)))
    if clear:
        elem.clear()
    elem.send_keys(text)
    return elem


def wait_and_click(wait, by:By, locator: str):
    """
    通用點擊動作：
    - 等待元素可被點擊
    - click
    """
    elem = wait.until(EC.element_to_be_clickable((by, locator)))
    elem.click()
    return elem

def wait_and_get_text(wait, by:By, locator: str):
    """
    等到元素可見後回傳文字。
    """
    elem = wait.until(EC.visibility_of_element_located((by, locator)))
    return elem.text

def is_visible(wait, by:By, locator: str, timeout: int = 2):
    """
    檢查元素是否在畫面上可見。
    不會 throw exception，而是回傳 True/False。
    """
    try:
        wait.until(EC.visibility_of_element_located((by, locator)))
        return True
    except:
        return False
    
def wait_for_url(driver, expected: str, timeout: int = 10, partial: bool = True):
    """
    等待 URL 變成指定內容（可設定部分比對）
    partial = True 代表 URL 包含 expected 就算成功。
    """
    end_time = time.time() + timeout

    while time.time() < end_time:
        current = driver.current_url
        if partial:
            if expected in current:
                return True
        else:
            if expected == current:
                return True
        time.sleep(0.1)

    return False
    
