import pytest
from Base.Web_Driver_Factory import WebDriverFactory
from Pages.Home.Log_in import LogInPage
from Pages.Login.LoginPage import LoginPage


#########################################################################################
@pytest.yield_fixture()
def Login_setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")
@pytest.yield_fixture()
def login_set_up():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

##############################################################################################
@pytest.yield_fixture(scope="class")
def oneTime_Login_SetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_web_driver_instance()
    lp = LoginPage(driver)
    lp.login_fn("modyseka@gmail.com", "1234567891011")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")
@pytest.yield_fixture()
def home_setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")
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
    driver = wdf1.get_web_driver_instance_home()
    lp1 = LogInPage(driver)
    lp1.login_password("modyseka@gmail.com", "1234567891011")

    if request.cls is not None:
        request.cls.Driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


############################################################################################
@pytest.yield_fixture(scope="class")
def oneTime_Login_SetUp_Edit(request, browser):
    wdf1 = WebDriverFactory(browser)
    driver = wdf1.get_web_driver_instance_home()
    lp1 = LogInPage(driver)
    lp1.login_edit("modyseka@gmail.com", "1234567891011")

    if request.cls is not None:
        request.cls.Driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


############################################################################################
@pytest.yield_fixture(scope="class")
def oneTime_Login_SetUp_Webplayer(request, browser):
    wdf1 = WebDriverFactory(browser)
    driver = wdf1.get_web_driver_instance_home()
    lp1 = LogInPage(driver)
    lp1.login_webpalyer("modyseka@gmail.com", "1234567891011")

    if request.cls is not None:
        request.cls.Driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")
