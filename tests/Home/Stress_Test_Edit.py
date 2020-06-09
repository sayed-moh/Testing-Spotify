import time
from selenium import webdriver
import unittest
from Pages.Home.Edit_Profile import EditPage
class EditPasswordStress(unittest.TestCase):
    Password = "1234567891011"
    Email = "modyseka@gmail.com"
    Driver = webdriver.Chrome(
        executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
    Driver.get("https://www.spotify.com/eg-en//")
    Driver.maximize_window()
    Driver.implicitly_wait(5)
    EP = EditPage(Driver)
    EP.log_in_edit(Email, Password)
    i = 0
    while (i < 1000):
        EP.change_mobile("0")
        i = i + 1
    EP.click_save()
    time.sleep(2)
    # Using sleep to can see what happened
    Driver.quit()