from Base.Selenium_Driver import SeleniumDriver
import time


class LogInPage(SeleniumDriver):
    def __init__(self, driver):
        # super().__init__(driver)
        self.Driver = driver

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

    def enter_email(self, email):
        self.send_keys(email, self.emailfield)

    def enter_password(self, password):
        self.send_keys(password, self.passwordfield)

    def click_login_link(self):
        self.element_click(self.Loginlink, "link")

    def click_login_button(self):
        self.element_click(self.loginbutton)

    def click_remember(self):
        self.element_click(self.Remember_me, "class")

    def click_on_spotify(self):
        self.element_click(self.Spotify, "class")

    def click_on_web_player(self):
        self.element_click(self.web_player_button)

    def click_edit_profile(self):
        self.element_click(self.Editprofile, "link")

    def login_edit(self, email, password):
        time.sleep(1)
        self.click_login_link()
        time.sleep(1)
        self.enter_email(email)
        self.enter_password(password)
        self.click_remember()
        self.click_login_button()
        time.sleep(1)
        self.click_edit_profile()

    def login_password(self, username, password):
        time.sleep(3)
        self.click_login_link()
        time.sleep(1)
        self.enter_email(username)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(2)
        self.hover(self.Change_Password, "link")

    def login_webpalyer(self, username, password):
        time.sleep(3)
        self.click_login_link()
        time.sleep(1)
        self.enter_email(username)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(2)
        self.click_on_spotify()
        time.sleep(1)
        self.click_on_web_player()
