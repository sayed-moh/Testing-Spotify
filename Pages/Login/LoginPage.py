from Base.Selenium_Driver import SeleniumDriver
import time
import logging
import utilities.custom_logger as cl


class LoginPage(SeleniumDriver):
    Log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.Driver = driver

    # locators
    email_field = "login-username"
    password_field = "login-password"
    submit_btn = "login-button"
    login_link = "/html/body/div[3]/div/div[2]/div[1]/header/div[4]/button[2]"

    def click_login_link(self):
        self.element_click(self.login_link, "xpath")

    def send_email_login(self, email):
        self.send_keys(email, self.email_field, "id")

    def send_pass_login(self, password):
        self.send_keys(password, self.password_field, "id")

    def click_login_btn(self):
        self.element_click(self.submit_btn, "id")

    def login_fn(self, email, password):
        self.click_login_link()
        time.sleep(2)
        self.send_email_login(email)
        self.send_pass_login(password)
        self.click_login_btn()
