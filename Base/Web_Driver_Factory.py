import traceback
from selenium import webdriver


class WebDriverFactory:

    def __init__(self, browser):

        self.browser = browser

    def get_web_driver_instance(self):

        base_url = "https://open.spotify.com/"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie(executable_path="C:\\Users\\Eslam\\PycharmProjects\\web\\drivers\\IEDriverServer.exe")
        elif self.browser == "firefox":
            driver = webdriver.Firefox(
                executable_path="C:\\Users\\Eslam\\PycharmProjects\\web\\drivers\\ geckodriver.exe")
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome(executable_path="E:\\software\\web\\drivers\\chromedriver.exe")
        else:
            driver = webdriver.Chrome(executable_path="E:\\software\\web\\drivers\\chromedriver.exe")
        # Setting driver Implicit Time out for An Element
        driver.implicitly_wait(2)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(base_url)

        return driver

    def get_web_driver_instance_home(self):

        base_url = "https://www.spotify.com/eg-en/"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie(executable_path="C:\\Users\\Eslam\\PycharmProjects\\web\\drivers\\IEDriverServer.exe")
        elif self.browser == "firefox":
            driver = webdriver.Firefox(
                executable_path="C:\\Users\\Eslam\\PycharmProjects\\web\\drivers\\ geckodriver.exe")
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome(executable_path="E:\\software\\web\\drivers\\chromedriver.exe")
        else:
            driver = webdriver.Chrome(executable_path="E:\\software\\web\\drivers\\chromedriver.exe")
        # Setting driver Implicit Time out for An Element
        driver.implicitly_wait(2)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(base_url)

        return driver
