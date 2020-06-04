from Base.Selenium_Driver import SeleniumDriver
import time

class Change_Password(SeleniumDriver):

    def __init__(self, Driver):
        # super().__init__(Driver)
        self.Driver =Driver

    # Locators Used in test

    current_password = "change_password_validatePassword"  # id
    new_password = "change_password_new_password"  # id
    repeat_new_password = "change_password_check_password"  # id
    set_new_password = "change_password_submit"  # id
    cancel_password = "Cancel"  # link

    def enter_current_password(self, password):
        self.SendKeys(password, self.current_password)

    def enter_new_password(self, newpassword):
        self.SendKeys(newpassword, self.new_password)

    def enter_repeat_password(self, newpassword):
        self.SendKeys(newpassword, self.repeat_new_password)

    def clear_current_password(self):
        self.Clears(self.current_password)

    def clear_new_password(self):
        self.Clears(self.new_password)

    def clear_repeat_password(self):
        self.Clears(self.repeat_new_password)

    def click_save_password(self):
        self.ElementClick(self.set_new_password)

    def click_cancel_password(self):
        self.ElementClick(self.cancel_password, "link")

    def change_password(self, password, new_password, repeat):
        # self.WaitForElement(self.new_password)
        time.sleep(1)
        self.clear_current_password()
        self.clear_new_password()
        self.clear_repeat_password()
        self.enter_current_password(password)
        self.enter_new_password(new_password)
        self.enter_repeat_password(repeat)
        self.click_save_password()
