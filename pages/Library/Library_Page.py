from web.base.Selenium_Driver import SeleniumDriver
import logging
import web.utilities.custom_logger as cl


class LibraryPage(SeleniumDriver):
    Log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.Driver = driver

    # locators
    my_library = "Your Library"
    podcasts = "Podcasts"
    playlist = "Playlists"
    artists = "Artists"
    albums = "Albums"
    r_playlist = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[1]/div[1]/div/div/div[4]"
    r_album = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[1]/div[1]/div/div/div[4]"
    find_artist = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/section/a"

    def click_library(self):
        self.element_click(self.my_library, "link")

    def click_podcast(self):
        self.element_click(self.podcasts, "link")

    def click_playlist(self):
        self.element_click(self.playlist, "link")

    def click_albums(self):
        self.element_click(self.albums, "link")

    def click_artist(self):
        self.element_click(self.artists, "link")

    def click_first_playlist(self):
        self.element_click(self.r_playlist, "xpath")

    def click_first_album(self):
        self.element_click(self.r_album, "xpath")

    def click_find_artist(self):
        self.element_click(self.find_artist, "xpath")
