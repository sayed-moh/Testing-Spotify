from Base.Selenium_Driver import SeleniumDriver
import time


class Like_Follow(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators Used in test

    Happy_Hits = "Happy Hits!"  # link
    Mood = "Mood Booster"  # link
    Mood_Song1 = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[1]/div/li"
    Mood_Song2 = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[2]/div/li"
    Mood_Song3 = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[3]/div/li"
    Song = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[1]/div/li"
    Like = "/html/body/div[4]/div/div[2]/div[3]/footer/div/div[1]/div/div[3]/button"
    Liked_List = "Liked Songs"
    Artist = "Amr Diab"
    Follow = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button[2]"
    Library = "Your Library"
    Your_Artist = "Artists"
    Playlist = "Test"
    Back = "/html/body/div[4]/div/div[2]/div[1]/header/div[2]/button[1]"
    Home = "Home"

    def click_happy_hits(self):
        self.element_click(self.Happy_Hits, "link")

    def click_liked_list(self):
        self.element_click(self.Liked_List, "link")

    def click_on_playlist(self):
        self.element_click(self.Playlist, "link")

    def click_artist(self):
        self.element_click(self.Liked_List, "link")

    def click_library(self):
        self.element_click(self.Library, "Link")

    def click_artists(self):
        self.element_click(self.Your_Artist, "Link")

    def click_like(self):
        self.element_click(self.Like, "xpath")

    def click_back(self):
        self.element_click(self.Back, "xpath")

    def click_home(self):
        self.element_click(self.Home, "link")

    # all sleeps in the code to can see what happened and my internet is not good
    def like_follow_test(self):
        time.sleep(4)
        self.click_on_playlist()
        self.hover_listed_song(self.Song)
        time.sleep(3)
        self.hover(self.Like)
        time.sleep(1)
        self.click_liked_list()
        time.sleep(3)
        self.hover(self.Like)
        time.sleep(1)
        self.hover(self.Like)
        time.sleep(1)
        self.hover(self.Artist, "Link")
        time.sleep(1)
        self.hover(self.Follow)
        time.sleep(1)
        self.click_library()
        time.sleep(1)
        self.click_artists()
        time.sleep(1)
        self.click_back()
        time.sleep(1)
        self.click_back()
        time.sleep(1)
        self.hover(self.Follow, "xpath")
        time.sleep(1)
        self.click_library()
        time.sleep(1)
        self.click_artists()
        time.sleep(1)
        self.click_liked_list()
        time.sleep(1)
        self.hover(self.Like)
        time.sleep(1)
        self.click_home()

    def like_test(self):
        time.sleep(4)
        self.hover(self.Mood, "link")
        self.hover_listed_song(self.Mood_Song1)
        time.sleep(3)
        self.hover(self.Like)
        time.sleep(1)
        self.hover_listed_song(self.Mood_Song2)
        time.sleep(3)
        self.hover(self.Like)
        time.sleep(1)
        self.hover_listed_song(self.Mood_Song3)
        time.sleep(3)
        self.hover(self.Like)
        time.sleep(1)
        self.click_liked_list()
        time.sleep(2)
        self.hover_listed_song(self.Mood_Song3)
        time.sleep(3)
        self.hover(self.Like)
        time.sleep(1)
        self.hover_listed_song(self.Mood_Song2)
        time.sleep(3)
        self.hover(self.Like)
        time.sleep(1)
        self.hover_listed_song(self.Mood_Song1)
        time.sleep(3)
        self.hover(self.Like)
        time.sleep(1)
        self.click_home()
