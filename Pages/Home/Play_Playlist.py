from Base.Selenium_Driver import SeleniumDriver
import time

class Play_Playlist(SeleniumDriver):

    def __init__(self, Driver):
        super().__init__(Driver)
        self.driver = Driver

        # Locators Used in test

    Loginlink = "Log In"
    emailfield = "login-username"
    passwordfield = "login-password"  # link
    loginbutton = "login-button"
    Spotify = "svelte-1gcdbl9"  # class
    web_player_button = "segmented-desktop-launch"
    Playlist = "Test"
    Play_button = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button"
    Next_Button = "/html/body/div[4]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[4]/button"
    Last_Song = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[5]/div/li"
    Second_Song = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[3]/div/li"
    First_Song = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[1]/div/li"
    Random_Song = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section/section/div/section[2]/div/div[2]/div/div/div[3]"

    def entereamil(self, email):
         self.SendKeys(email, self.emailfield)

    def enterpassword(self, password):
         self.SendKeys(password, self.passwordfield)

    def clickloginlink(self):
         self.ElementClick(self.Loginlink, "link")

    def clickloginbutton(self):
         self.ElementClick(self.loginbutton)

    def click_on_spotify(self):
         self.ElementClick(self.Spotify, "class")

    def click_on_web_player(self):
         self.ElementClick(self.web_player_button)

    def Click_On_Playlist(self):
        self.ElementClick(self.Playlist, "link")

    def Click_On_Play(self):
        self.ElementClick(self.Play_button, "xpath")

    def Click_On_Next(self):
        self.ElementClick(self.Next_Button, "xpath")

    # def Login_Webplayer(self, username, password):
    #     self.clickloginlink()
    #     self.WaitForElement(self.emailfield)
    #     self.entereamil(username)
    #     self.enterpassword(password)
    #     self.clickloginbutton()
    #     self.WaitForElement(self.Spotify, "class")
    #     self.click_on_spotify()
    #     self.click_on_web_player()
    #     self.WaitForElement(self.Playlist, "link")


    def Play_Playlist(self):
        time.sleep(3)
        self.Hover(self.Random_Song)
        time.sleep(4)
        self.Click_On_Playlist()
        self.Hover(self.First_Song)
        time.sleep(1)
        self.Hover(self.Second_Song)
        time.sleep(1)
        self.Hover(self.Last_Song)
        self.Click_On_Play()
        time.sleep(10)
        self.Click_On_Next()
        time.sleep(10)
        self.Click_On_Next()
        time.sleep(10)
        self.Click_On_Next()
        time.sleep(10)
        self.Click_On_Next()
        time.sleep(10)

