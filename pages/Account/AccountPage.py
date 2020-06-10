from base.Selenium_Driver import SeleniumDriver
import time
import logging
import utilities.custom_logger as cl


class AccountPage(SeleniumDriver):
    Log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.Driver = driver

    # locators
    # recover_playlists = "https://www.spotify.com/eg-ar/account/recover-playlists/"
    recover_playlists = "/html/body/div/div/div/div[2]/div[2]/div[1]/div/ul/li[6]"
    restore = "/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div/div/section/div/table/tbody/tr/td[4]/button"

    def click_recover_playlists(self):
        self.element_click(self.recover_playlists, "xpath")

    def click_restore(self):
        self.element_click(self.restore, "xpath")
