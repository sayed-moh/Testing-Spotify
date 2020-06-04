from Base.Selenium_Driver import SeleniumDriver
import logging
import utilities.custom_logger as cl


class SearchPage(SeleniumDriver):
    Log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.Driver = driver

    # locators
    search_window = "Search"  # link
    search_tab = "/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/input"
    target_artist = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/div/div/div/section[1]/div/div[" \
                    "2]/div/div/div/div[4] "
    target_song = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/div/div/div/section[1]/div/div[" \
                  "2]/div/div/div/div[4] "
    def click_searched_song(self):
        self.element_click(self.target_song, "xpath")

    def click_search_window(self):
        self.element_click(self.search_window, "link")

    def send_in_search_tab(self, song):
        self.send_keys(song, self.search_tab, "xpath")

    def clear_search_bar(self):
        search_tab1 = self.get_element(self.search_tab, "xpath")
        search_tab1.clear()

    def click_searched_artist(self):
        self.element_click(self.target_artist, "xpath")
