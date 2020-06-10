from Base.Selenium_Driver import SeleniumDriver
import time
import logging
import utilities.custom_logger as cl


class AddRemoveSongsPlaylistsPage(SeleniumDriver):
    Log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.Driver = driver

    # locators
    refresh = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/div/div/div[2]/button"  #
    playlist_name = "sayed_Test"  #
    first_searched_song = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/section/ol/div/div/li"  #
    add_button = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/div/section/ol/div[" \
                 "1]/div/li/div[3]/button"  #
    hovered_options = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[" \
                      "1]/div/li/div[3]/div/div/button"  #
    add_to_playlist = "/html/body/div[4]/div/nav[1]/div[4]"  #
    choose_playlist = "/html/body/div[4]/div/div[3]/div/div[2]/div[1]/div/div/div/div/div[1]/div"  #
    upper_options = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/div/button"
    upper_add_playlist = "/html/body/div[4]/div/nav[2]/div[3]"
    first_song_to_remove = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[" \
                           "1]/div/li "
    remove_from_playlist = "/html/body/div[4]/div/nav[1]/div[5]"
    target_playlists = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section/section/div/section[1]/div/div[" \
                       "7]/div/div/div[4] "
    wanted_song = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[1]/div/li"
    "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[1]/div/li"
    my_playlist = "/html/body/div[3]/div/div[4]/div/div[2]/div[1]/div/div/div/div"
    home = "Home"
    searched_song = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section[1]/section/ol/div/div/li/div[2]"
    remove_option = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[" \
                    "1]/div/li/div[3]/div/div/button "
    options_a = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/section/ol/div/div/li/div[" \
                "3]/div/div/button "

    def click_target_playlist(self):
        self.element_click(self.target_playlists, "xpath")

    def click_wanted_song_home(self):
        self.element_click(self.wanted_song, "xpath")

    def open_my_playlist(self):
        self.element_click(self.playlist_name, "link")

    def click_refresh(self):
        self.element_click(self.refresh, "xpath")

    def click_add_button(self):
        self.element_click(self.add_button, "xpath")

    def click_home(self):
        self.element_click(self.home, "link")

    def click_options(self):
        time.sleep(1)
        self.hover(self.first_searched_song, "xpath")
        self.hover(self.options_a, "xpath")
        self.element_click(self.add_to_playlist, "xpath")
        time.sleep(1)
        self.element_click(self.choose_playlist, "xpath")
        time.sleep(1)

    ###################################de
    def remove_song(self):
        time.sleep(1)
        self.hover(self.first_song_to_remove, "xpath")
        time.sleep(2)
        self.element_click(self.remove_option, "xpath")
        time.sleep(1)
        self.element_click(self.remove_from_playlist, "xpath")
        time.sleep(1)

    def add_playlist_from_upper_options(self):
        time.sleep(5)
        self.hover(self.upper_options, "xpath")
        time.sleep(2)
        self.element_click(self.upper_add_playlist, "xpath")
        time.sleep(1)
        self.element_click(self.choose_playlist, "xpath")

    def get_song_home_playlist(self):
        self.hover(self.wanted_song, "xpath")
        time.sleep(1)
        self.element_click(self.remove_option, "xpath")
        time.sleep(1)
        self.element_click(self.add_to_playlist, "xpath")
        time.sleep(1)
        self.element_click(self.choose_playlist, "xpath")
