import time
from selenium import webdriver
from Pages.Home.Edit_Password_Page import ChangePassword
import unittest


class EditPasswordStress(unittest.TestCase):

    Password = "1234567891011"
    Email = "modyseka@gmail.com"
    Driver = webdriver.Chrome(
        executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
    Driver.get("https://www.spotify.com/eg-en//")
    Driver.maximize_window()
    Driver.implicitly_wait(5)
    CP = ChangePassword(Driver)
    CP.log_in_change_password(Email, Password)
    CP.wait_for_element(CP.new_password)

    def test_Stress_Password_1(self):
        self.CP.clear_current_password()
        self.CP.clear_new_password()
        self.CP.clear_repeat_password()
        self.CP.enter_current_password(self.Password)
        i = 0
        while(i<10000):
         self.CP.enter_new_password("00")
         self.CP.enter_repeat_password("00")
         i = i+1
    #   cp.click_save_password()
    #  I comment it because I afraid to save it


    def test_Stress_Password_2(self):
        self.CP.clear_current_password()
        self.CP.clear_new_password()
        self.CP.clear_repeat_password()
        i = 0
        while(i<5000):
          self.CP.enter_current_password(self.Password)
          i = i+1
        self.CP.enter_new_password("252525252525")
        self.CP.enter_repeat_password("252525252525")
        self.CP.click_save_password()


