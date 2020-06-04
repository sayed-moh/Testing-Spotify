from Base.Selenium_Driver import SeleniumDriver
import time

class Log_in_Page(SeleniumDriver):
    def __init__(self, Driver):
        # super().__init__(driver)
        self.Driver =Driver

        # Locators Used in test

    Loginlink = "Log In"
    emailfield = "login-username"
    passwordfield = "login-password"  # link
    loginbutton = "login-button"
    Change_Password = "Change password"
    Editprofile = "Edit profile"  # link
    Remember_me = "control-indicator"
    Spotify = "svelte-1gcdbl9"  # class
    web_player_button = "segmented-desktop-launch"



    def entereamil(self, email):
        self.SendKeys(email, self.emailfield)

    def enterpassword(self, password):
        self.SendKeys(password, self.passwordfield)

    def clickloginlink(self):
        self.ElementClick(self.Loginlink, "link")

    def clickloginbutton(self):
        self.ElementClick(self.loginbutton)

    def clickremember(self):
        self.ElementClick(self.Remember_me, "class")

    def click_on_spotify(self):
         self.ElementClick(self.Spotify, "class")

    def click_on_web_player(self):
         self.ElementClick(self.web_player_button)

    def Click_Edit_Profile(self):
        self.ElementClick(self.Editprofile, "link")

    def Login_Edit(self, email, password):
        time.sleep(1)
        self.clickloginlink()
        time.sleep(1)
        self.entereamil(email)
        self.enterpassword(password)
        self.clickremember()
        self.clickloginbutton()
        time.sleep(1)
        self.Click_Edit_Profile()

    def Login_Password(self, username, password):
        time.sleep(3)
        self.clickloginlink()
        time.sleep(1)
        self.entereamil(username)
        self.enterpassword(password)
        self.clickloginbutton()
        time.sleep(2)
        self.Hover(self.Change_Password, "link")

    def Login_Webpalyer(self, username, password):
        time.sleep(3)
        self.clickloginlink()
        time.sleep(1)
        self.entereamil(username)
        self.enterpassword(password)
        self.clickloginbutton()
        time.sleep(2)
        self.click_on_spotify()
        time.sleep(1)
        self.click_on_web_player()