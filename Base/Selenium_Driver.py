from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import utilities.custom_logger as cl
import os
import time
import logging


class SeleniumDriver:
    Log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.Driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.Log.info("locator type " + locator_type +
                          " not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.Driver.find_element(by_type, locator)
            self.Log.info("element found with locator: " + locator +
                          " and  locator_type: " + locator_type)
        except:
            self.Log.info("element not found with locator: " + locator +
                          " and  locator_type: " + locator_type)
        return element

    def element_click(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.Log.info("Clicked on element with locator: " + locator +
                          " locator_type: " + locator_type)
        except:
            self.Log.info("Cannot click on the element with locator: " + locator +
                          " locator_type: " + locator_type)
            print_stack()

    def send_keys(self, data, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.Log.info("Sent data on element with locator: " + locator +
                          " locator_type: " + locator_type)
        except:
            self.Log.info("Cannot send data on the element with locator: " + locator +
                          " locator_type: " + locator_type)
            print_stack()

    def hover_song(self, locator, locator_type="xpath", button=""):
        try:
            self.wait_for_element(locator, locator_type)
            element = self.get_element(locator, locator_type)
            item_to_click_locator = button
            actions = ActionChains(self.Driver)
            actions.move_to_element(element).perform()
            self.Log.info("Mouse Hovered on element")
            song = self.Driver.find_element(By.XPATH, item_to_click_locator)
            actions.move_to_element(song).click().perform()
        except:
            self.Log.info("Cannot send data on the element with locator: " + locator +
                  " locator_type: " + locator_type)
            print_stack()

    def hover(self, locator, locator_type="xpath"):
        try:
            time.sleep(2)
            # self.wait_for_element(locator, locator_type)
            element = self.get_element(locator, locator_type)
            actions = ActionChains(self.Driver)
            actions.move_to_element(element).click().perform()
            self.Log.info("Mouse Hovered on element")
        except:
            self.Log.info("Cannot send data on the element with locator: " + locator +
                  " locator_type: " + locator_type)
            print_stack()

    def hover_listed_song(self, locator, locator_type="xpath"):
        try:
            self.wait_for_element(locator, locator_type)
            element = self.get_element(locator, locator_type)
            actions = ActionChains(self.Driver)
            actions.move_to_element(element).double_click(element).perform()
            self.Log.info("Mouse Hovered on element")
        except:
            self.Log.info("Cannot send data on the element with locator: " + locator +
                  " locator_type: " + locator_type)
            print_stack()

    def select_item(self, data, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            item = Select(element)
            item.select_by_visible_text(data)
            self.Log.info("Sent data on element with locator: " + locator + " locator_type: " + locator_type)
        except:
            self.Log.info("Cannot send data on the element with locator: " + locator +
                  " locator_type: " + locator_type)
            # print_stack()

    def clears(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.clear()
            self.Log.info("clear data from element with locator: " + locator + " locator_type: " + locator_type)
        except:
            self.Log.info("Cannot clear data from the element with locator: " + locator +
                  " locator_type: " + locator_type)
        # print_stack()

    def is_element_present(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                self.Log.info("element Found")
                return True
            else:
                self.Log.info("element not found")
        except:
            self.Log.info("Element not found")
            return False

    def element_presence_check(self, locator, by_type):
        try:
            element_list = self.Driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.Log.info("Element Found")
                return True
            else:
                self.Log.info("Element not found")
                return False
        except:
            self.Log.info("Element not found")
            return False

    def wait_for_element(self, locator, locator_type="id",
                         timeout=15, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.Log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.Driver, timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.Log.info("Element appeared on the web page")
        except:
            self.Log.info("Element not appeared on the web page")
            print_stack()
        return element

    def screen_shot1(self, result_message):
        """
        Takes screenshot of the current open web page
        """
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.Driver.save_screenshot(destination_file)
            self.Log.info("Screenshot save to directory: " + destination_file)
        except:
            self.Log.error("### Exception Occurred when taking screenshot")

    def screen_shot(self, result_message):
        """
        Takes screenshot of the current open web page
        """
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.Driver.save_screenshot(destination_file)
            self.Log.info("Screenshot save to directory: " + destination_file)
        except:
            self.Log.error("### Exception Occurred when taking screenshot")
            # print_stack()
