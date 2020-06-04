import time
from selenium import webdriver
from Pages.Home.Edit_Password_Page import ChangePassword
import unittest
from Pages.Home.Edit_Profile import EditPage


class EditPasswordStress(unittest.TestCase):

    Password = "12345678910"
    Email = "modyseka@gmail.com"

    def test_Stress_Password_1(self):
        Driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        Driver.get("https://www.spotify.com/eg-en//")
        Driver.maximize_window()
        Driver.implicitly_wait(5)
        cp = ChangePassword(Driver)
        cp.Log_In_Change_Password(self.Email, self.Password)
        cp.wait_for_element(cp.new_password)
        cp.clear_current_password()
        cp.clear_new_password()
        cp.clear_repeat_password()
        cp.enter_current_password(self.Password)
        i = 0
        while(i<10000):
         cp.enter_new_password("00")
         cp.enter_repeat_password("00")
         i = i+1
         # cp.click_save_password()
        Driver.quit()

    def test_Stress_Password_2(self):
        Driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        Driver.get("https://www.spotify.com/eg-en//")
        Driver.maximize_window()
        Driver.implicitly_wait(5)
        CP = ChangePassword(Driver)
        CP.Log_In_Change_Password(self.Email, self.Password)
        CP.wait_for_element(CP.new_password)
        CP.clear_current_password()
        CP.clear_new_password()
        CP.clear_repeat_password()
        i = 0
        while(i<5000):
          CP.enter_current_password(self.Password)
          i = i+1
        CP.enter_new_password("252525252525")
        CP.enter_repeat_password("252525252525")
        CP.click_save_password()
        Driver.quit()

    def test_Change_phone_Scenarios_5(self):
        Driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        Driver.get("https://www.spotify.com/eg-en//")
        Driver.maximize_window()
        Driver.implicitly_wait(5)
        EP = EditPage(Driver)
        EP.log_in_edit(self.Email, self.Password)
        i = 0
        while(i<5000):
         EP.change_mobile("0")
         i = i+1
        EP.click_save()
        time.sleep(2)
        # Using sleep to can see what happened
        Driver.quit()