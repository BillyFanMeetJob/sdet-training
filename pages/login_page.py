# pages/login_page.py
from selenium.webdriver.common.by import By
from base.basepage import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON   = (By.ID, "login-button")

    def open(self, base_url: str):
        self.driver.get(base_url)

    def login(self, username: str, password: str):
        self.type(*self.USERNAME_INPUT, text=username)
        self.type(*self.PASSWORD_INPUT, text=password)
        self.click(*self.LOGIN_BUTTON)
