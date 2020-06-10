import traceback
from selenium import webdriver


class WebDriverFactory:

    def __init__(self, browser):

        self.browser = browser

    def get_web_driver_instance(self):

        base_url = "https://open.spotify.com/"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome()
        # Setting driver Implicit Time out for An Element
        driver.implicitly_wait(2)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(base_url)

        return driver
