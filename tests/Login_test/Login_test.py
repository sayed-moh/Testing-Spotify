from Pages.Login.LoginPage import LoginPage
import unittest
import pytest
import time


############################################
# Note
# this test is just for exprimenting the functions to use it in another features but not from the features


##############################################
@pytest.mark.usefixtures("oneTime_Login_SetUp", "login_set_up")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp):
        self.lp = LoginPage(self.driver)
        time.sleep(2)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login_fn("modyseka@gmail.com", "12345678910")
        '''result = self.lp.verifyLoginSuccessful()
        assert result == True'''

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login_fn("modyseka@gmail.com", "abcabcabc")
        '''result = self.lp.verifyLoginFailed()
        assert result == True'''
