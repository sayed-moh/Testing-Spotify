import pytest
from Base.Web_Driver_Factory import WebDriverFactory
from Pages.Home.Log_in import Log_in_Page
#########################################################################################
@pytest.yield_fixture()
def Login_setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")



##############################################################################################
# @pytest.yield_fixture(scope="class")
# def oneTime_Login_SetUp(request, browser):
#     print("Running one time setUp")
#     wdf = WebDriverFactory(browser)
#     driver = wdf.GetWebDriverInstance()
#     lp = Login_page(driver)
#     lp.LoginFN("modyseka@gmail.com", "12345678910")
#
#     if request.cls is not None:
#         request.cls.driver = driver
#
#     yield driver
#     driver.quit()
#     print("Running one time tearDown")
# @pytest.yield_fixture()
# def home_setUp():
#     print("Running method level setUp")
#     yield
#     print("Running method level tearDown")
##########################################################################################
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
############################################################################################
@pytest.yield_fixture(scope="class")
def oneTime_Login_SetUp_Account(request, browser):
    wdf1 = WebDriverFactory(browser)
    Driver = wdf1.GetWebDriverInstance_Home()
    lp1 = Log_in_Page(Driver)
    lp1.Login_Password("modyseka@gmail.com", "1234567891011")

    if request.cls is not None:
        request.cls.Driver = Driver

    yield Driver
    Driver.quit()
    print("Running one time tearDown")
############################################################################################
@pytest.yield_fixture(scope="class")
def oneTime_Login_SetUp_Edit(request, browser):
    wdf1 = WebDriverFactory(browser)
    Driver = wdf1.GetWebDriverInstance_Home()
    lp1 = Log_in_Page(Driver)
    lp1.Login_Edit("modyseka@gmail.com", "1234567891011")

    if request.cls is not None:
        request.cls.Driver = Driver

    yield Driver
    Driver.quit()
    print("Running one time tearDown")

############################################################################################
@pytest.yield_fixture(scope="class")
def oneTime_Login_SetUp_Webplayer(request, browser):
    wdf1 = WebDriverFactory(browser)
    Driver = wdf1.GetWebDriverInstance_Home()
    lp1 = Log_in_Page(Driver)
    lp1.Login_Webpalyer("modyseka@gmail.com", "1234567891011")

    if request.cls is not None:
        request.cls.Driver = Driver

    yield Driver
    Driver.quit()
    print("Running one time tearDown")