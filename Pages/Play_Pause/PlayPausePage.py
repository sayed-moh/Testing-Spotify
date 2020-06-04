from Base.Selenium_Driver import SeleniumDriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging
import utilities.custom_logger as cl


class PlayPausePage(SeleniumDriver):
    Log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.Driver = driver

    # locators
    first_song_playlist = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[" \
                          "1]/div/li "
    play_top = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button"
    play_pause_lower = "/html/body/div[4]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[3]/button"
    next = "/html/body/div[4]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[4]/button"
    previous = "/html/body/div[4]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[2]/button"
    play_queue = "/html/body/div[4]/div/div[2]/div[3]/footer/div/div[3]/div/div/div[1]/div/button"
    queued_song = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[4]/div/li"
    options = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[4]/div/li/div[" \
              "3]/div/div/button "
    add_to_queue = "/html/body/div[4]/div/nav[1]/div[3]"
    sound_play = "/html/body/div[4]/div/div[2]/div[3]/footer/div/div[3]/div/div/div[3]/div"
    sound_switch = "/html/body/div[4]/div/div[2]/div[3]/footer/div/div[3]/div/div/div[3]/button"

    def play_first_song(self):
        result = self.Driver.find_element_by_xpath(self.first_song_playlist)
        actions = ActionChains(self.Driver)
        actions.move_to_element(result).click.perform()

    def play_playlist(self):
        self.element_click(self.play_top, "xpath")
        time.sleep(5)

    def click_play_pause(self):
        self.element_click(self.play_pause_lower, "xpath")
        time.sleep(2)
        self.element_click(self.play_pause_lower, "xpath")
        time.sleep(2)

    def click_next(self):
        self.element_click(self.next, "xpath")
        time.sleep(5)

    def click_previous(self):
        self.element_click(self.previous, "xpath")
        time.sleep(5)

    def slider_sound(self):
        self.element_click(self.sound_play, "xpath")
        time.sleep(2)

    def queue_play(self):
        self.element_click(self.queued_song, "xpath")
        time.sleep(2)
        self.element_click(self.options, "xpath")
        self.element_click(self.add_to_queue, "xpath")
        self.element_click(self.play_queue, "xpath")

    def sound_btn(self):
        self.element_click(self.sound_switch, "xpath")


'''def Playing_with_queue(self):
self.element_click(self.play_queue,"xpath")
self.element_click(self.Wanted_Song_Queue,"xpath")
time.sleep(2)
self.element_click(self.options,"xpath")
self.element_click(self.add_to_queue,"xpath")'''
