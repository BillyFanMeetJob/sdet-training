# pages/base_page.py
from selenium.webdriver.support import expected_conditions as EC
import toolkit.web_toolkit as Tool
import base.browser as Browser
class BasePage():
    def __init__(self, browser:Browser):
        # browser 是你自己那個 Browser 物件
        self.browser = browser
        self.driver = browser.driver
        self.wait = browser.wait

    def type(self, by, locator, text):
        return Tool.wait_and_type(self.wait,by, locator,text)

    def click(self, by, locator):
        return Tool.wait_and_click(self.wait,by, locator)

    def get_text(self, by, locator):
        return Tool.wait_and_get_text(self.wait, by, locator)

    def is_visible(self, by, locator, timeout=2):
        # 呼叫 toolkit 版
        return Tool.is_visible(self.wait, by, locator, timeout=timeout)

    def wait_for_url(self, expected, timeout=10, partial=True):
        return Tool.wait_for_url(self.driver, expected, timeout=timeout, partial=partial)
