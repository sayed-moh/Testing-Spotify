
import traceback
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):

        self.browser = browser


    def GetWebDriverInstance(self):

        BaseURL = "https://open.spotify.com/"
        if self.browser == "iexplorer":
            # Set ie Driver
            Driver = webdriver.Ie(executable_path="C:\\Users\\Eslam\\PycharmProjects\\web\\drivers\\IEDriverServer.exe")
        elif self.browser == "firefox":
            Driver = webdriver.Firefox(executable_path="C:\\Users\\Eslam\\PycharmProjects\\web\\drivers\\ geckodriver.exe")
        elif self.browser == "chrome":
            # Set chrome Driver
            Driver = webdriver.Chrome(executable_path="E:\\software\\web\\drivers\\chromedriver.exe")
        else:
            Driver = webdriver.Chrome(executable_path="E:\\software\\web\\drivers\\chromedriver.exe")
        # Setting Driver Implicit Time out for An Element
        Driver.implicitly_wait(2)
        # Maximize the window
        Driver.maximize_window()
        # Loading browser with App URL
        Driver.get(BaseURL)

        return Driver

    def GetWebDriverInstance_Home(self):

        BaseURL = "https://www.spotify.com/eg-en/"
        if self.browser == "iexplorer":
            # Set ie Driver
            Driver = webdriver.Ie(executable_path="C:\\Users\\Eslam\\PycharmProjects\\web\\drivers\\IEDriverServer.exe")
        elif self.browser == "firefox":
            Driver = webdriver.Firefox(executable_path="C:\\Users\\Eslam\\PycharmProjects\\web\\drivers\\ geckodriver.exe")
        elif self.browser == "chrome":
            # Set chrome Driver
            Driver = webdriver.Chrome(executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        else:
            Driver = webdriver.Chrome(executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        # Setting Driver Implicit Time out for An Element
        Driver.implicitly_wait(2)
        # Maximize the window
        Driver.maximize_window()
        # Loading browser with App URL
        Driver.get(BaseURL)

        return Driver

