from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import time
class SeleniumDriver():

    def __init__(self, Driver):
        self.Driver = Driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False

    def GetElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.Driver.find_element(byType, locator)
            print("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            print("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def ElementClick(self, locator, locatorType="id"):
        try:
            element = self.GetElement(locator, locatorType)
            element.click()
            print("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            print("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def SendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.GetElement(locator, locatorType)
            element.send_keys(data)
            print("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            print("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def Hover_song(self, locator, locatorType="xpath", button=""):
        try:
            self.WaitForElement(locator, locatorType)
            element = self.GetElement(locator, locatorType)
            itemToClickLocator = button
            actions = ActionChains(self.Driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on element")
            song = self.Driver.find_element(By.XPATH, itemToClickLocator)
            actions.move_to_element(song).click().perform()
        except:
            print("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def Hover(self, locator, locatorType="xpath" ):
        try:
            time.sleep(2)
            # self.WaitForElement(locator, locatorType)
            element = self.GetElement(locator, locatorType)
            actions = ActionChains(self.Driver)
            actions.move_to_element(element).click().perform()
            print("Mouse Hovered on element")
        except:
            print("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def Hover_Listed_Song(self, locator, locatorType="xpath"):
        try:
            self.WaitForElement(locator, locatorType)
            element = self.GetElement(locator, locatorType)
            actions = ActionChains(self.Driver)
            actions.move_to_element(element).double_click(element).perform()
            print("Mouse Hovered on element")
        except:
            print("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def SelectItem(self, data, locator, locatorType="id"):
        try:
            element = self.GetElement(locator, locatorType)
            item = Select(element)
            item.select_by_visible_text(data)
            print("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            print("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            # print_stack()

    def Clears(self, locator, locatorType="id"):
        try:
            element = self.GetElement(locator, locatorType)
            element.clear()
            print("claer data from element with locator: " + locator + " locatorType: " + locatorType)
        except:
             print("Cannot claer data from the element with locator: " + locator +
                   " locatorType: " + locatorType)
            # print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.GetElement(locator, locatorType)
            if element is not None:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.Driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def WaitForElement(self, locator, locatorType="id",
                       timeout=15, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.Driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element
