from Base.Selenium_Driver import SeleniumDriver
import time


class PlayPlaylist(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators Used in test

    Playlist = "Test"
    Play_button = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button"
    Next_Button = "/html/body/div[4]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[4]/button"
    Last_Song = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[5]/div/li"
    Second_Song = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[3]/div/li"
    First_Song = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[1]/div/li"
    Random_Song = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section/section/div/section[2]/div/div[" \
                  "2]/div/div/div[3] "

    def click_on_playlist(self):
        self.element_click(self.Playlist, "link")

    def click_on_play(self):
        self.element_click(self.Play_button, "xpath")

    def click_on_next(self):
        self.element_click(self.Next_Button, "xpath")


    def play_playlist(self):
        time.sleep(3)
        self.hover(self.Random_Song)
        time.sleep(4)
        self.click_on_playlist()
        self.hover(self.First_Song)
        time.sleep(1)
        self.hover(self.Second_Song)
        time.sleep(1)
        self.hover(self.Last_Song)
        self.click_on_play()
        time.sleep(10)
        self.click_on_next()
        time.sleep(10)
        self.click_on_next()
        time.sleep(10)
        self.click_on_next()
        time.sleep(10)
        self.click_on_next()
        time.sleep(10)
