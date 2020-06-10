from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import os
import time
import logging


class SeleniumDriver:
    Log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.Driver = driver

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
            # print_stack()

    def send_keys(self, data, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.Log.info("Sent data on element with locator: " + locator +
                          " locator_type: " + locator_type)
        except:
            self.Log.info("Cannot send data on the element with locator: " + locator +
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
                return False
        except:
            print("element not found")
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
                         timeout=3, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.Log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.Driver, 3, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(ec.element_to_be_clickable((by_type,
                                                             "stopFilter_stops-0")))
            self.Log.info("Element appeared on the web page")
        except:
            self.Log.info("Element not appeared on the web page")
            # print_stack()
        return element

    def clears(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.clear()
            print("clear data from element with locator: " + locator + " locatorType: " + locator_type)
        except:
            print("Cannot clear data from the element with locator: " + locator +
                  " locatorType: " + locator_type)
            # print_stack()
