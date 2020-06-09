from Base.Selenium_Driver import SeleniumDriver
import time


class ChangePassword(SeleniumDriver):

    def __init__(self, driver):
        # super().__init__(driver)
        self.Driver = driver

    # Locators Used in test

    current_password = "change_password_validatePassword"  # id
    new_password = "change_password_new_password"  # id
    repeat_new_password = "change_password_check_password"  # id
    set_new_password = "change_password_submit"  # id
    cancel_password = "Cancel"  # link
    login_link = "Log In"
    email_field = "login-username"
    password_field = "login-password"  # link
    login_button = "login-button"
    change_password_button = "Change password"

    def enter_email(self, email):
        self.send_keys(email, self.email_field)

    def enter_password(self, password):
        self.send_keys(password, self.password_field)

    def click_login_link(self):
        self.element_click(self.login_link, "link")

    def click_login_button(self):
        self.element_click(self.login_button)

    def click_change_password(self):
        self.element_click(self.change_password_button)

    def enter_current_password(self, password):
        self.send_keys(password, self.current_password)

    def enter_new_password(self, newpassword):
        self.send_keys(newpassword, self.new_password)

    def enter_repeat_password(self, newpassword):
        self.send_keys(newpassword, self.repeat_new_password)

    def clear_current_password(self):
        self.clears(self.current_password)

    def clear_new_password(self):
        self.clears(self.new_password)

    def clear_repeat_password(self):
        self.clears(self.repeat_new_password)

    def click_save_password(self):
        self.element_click(self.set_new_password)

    def click_cancel_password(self):
        self.element_click(self.cancel_password, "link")

    def change_password(self, password, new_password, repeat):
        # self.wait_for_element(self.new_password)
        time.sleep(1)
        self.clear_current_password()
        self.clear_new_password()
        self.clear_repeat_password()
        self.enter_current_password(password)
        self.enter_new_password(new_password)
        self.enter_repeat_password(repeat)
        self.click_save_password()

    def log_in_change_password(self, username, password):
        time.sleep(3)
        self.click_login_link()
        time.sleep(1)
        self.enter_email(username)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(2)
        self.hover(self.change_password_button, "link")
