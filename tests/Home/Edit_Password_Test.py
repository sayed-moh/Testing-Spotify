import time
from Pages.Home.Edit_Password_Page import ChangePassword
import unittest
import pytest


@pytest.mark.usefixtures("oneTime_Login_SetUp_Account", "Login_setUp")
class TestEditPassword(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp_Account):
        # self.CP = Change_Password(self.driver)
        self.Password = "1234567891011"
        self.Email = "modyseka@gmail.com"
        self.CP = ChangePassword(self.Driver)

    def test_Change_Password_Scenario_1(self):
        self.CP.change_password(" ", " ", " ")
        # try to send empty spaces it will refuse it
        time.sleep(1)

    def test_Change_Password_Scenario_2(self):
        # send correct password and and spaces in new password
        self.CP.change_password(self.Password, "", "")
        time.sleep(1)

    def test_Change_Password_Scenario_3(self):
        self.CP.change_password(self.Password, "", "252525252525")
        # send correct password and send only the repeat password
        time.sleep(1)

    def test_Change_Password_Scenario_4(self):
        self.CP.change_password(self.Password, "252525252525", "")
        # send correct password and send only the new password
        time.sleep(1)

    def test_Change_Password_Scenario_5(self):
        self.CP.change_password("", "252525252525", "252525252525")
        # send valid new and repeat password but not send the old password
        time.sleep(1)

    def test_Change_Password_Scenario_6(self):
        self.CP.change_password(self.Password, self.Password, self.Password)
        # send old password and send new password as same the old password
        time.sleep(1)

    def test_Change_Password_Scenario_7(self):
        self.CP.change_password(self.Password, "a", "a")
        # send old password correct but make new password very small
        time.sleep(1)

    def test_Change_Password_Scenario_8(self):
        self.CP.change_password(self.Password, "ag@195", "ag@195")
        # send old password correct but make new password in good format but small it will refuse it
        time.sleep(1)

    def test_Change_Password_Scenario_9(self):
        self.CP.change_password(self.Password, "252525252525", "252525")
        # send old password correct and send new password and repeat password do not match
        time.sleep(1)

    def test_Change_Password_Scenario_10(self):
        self.CP.change_password(self.Password, "252525", "252525252525")
        # send old password correct and send new password and repeat password do not match
        time.sleep(1)

    def test_Change_Password_Scenario_11(self):
        self.CP.change_password("1111", "252525252525", "252525252525")
        # send old password not correct and send new password and repeat password match and in correct format
        time.sleep(1)

    def test_Change_Password_Scenario_12(self):
        self.CP.change_password(self.Password, "123456789", "123456789")
        # send old password correct and new password is password used before so it will refuse it
        time.sleep(1)

    def test_Change_Password_Scenario_14(self):
        # make new password as the username email it will accept it
        # but i tried it before so it will refuse it as it is old password
        self.CP.change_password(self.Password, self.Email, self.Email)
        time.sleep(1)

    # this function change the password correctly so do not run it because the password change correctly please do
    # not run it as password too huge and it is hard to change it def test_Change_Password_Scenario_13(self): # send
    # old password correct and new password and repeat password is too long # it will accept it so please do not run
    # it self.CP.change_password(self.password,
    # "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmzzzzzzzzzzzzzzzzzzz" ,
    # "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmzzzzzzzzzzzzzzzzzzz")
    # time.sleep(1)

    # this function change the password correctly so please run it at the end
    # def test_Change_Password_Successfully(self):
    #     # it will change password correctly
    #     self.CP.change_password(self.password, "123456789101112", "123456789101112")
    #     time.sleep(1)

    # this function change all Scenario if you want to run it just incomment it
    # def test_Change_Password_All_Scenario_Without_Change(self):
    #     # it will change password correctly
    #     CP.change_password(" ", " ", " ")
    #     time.sleep(1)
    #     CP.change_password(self.password, " ", " ")
    #     time.sleep(1)
    #     CP.change_password(self.password, "", "252525252525")
    #     time.sleep(1)
    #     CP.change_password(self.password, "252525252525", "")
    #     time.sleep(1)
    #     CP.change_password("", "252525252525", "252525252525")
    #     time.sleep(1)
    #     CP.change_password(self.password, self.password, self.password)
    #     time.sleep(1)
    #     CP.change_password(self.password, "a", "a")
    #     time.sleep(1)
    #     CP.change_password(self.password, "ag@195", "ag@195")
    #     time.sleep(1)
    #     CP.change_password(self.password, "252525252525", "252525")
    #     time.sleep(1)
    #     CP.change_password(self.password, "252525", "252525252525")
    #     time.sleep(1)
    #     CP.change_password("1111", "252525252525", "252525252525")
    #     time.sleep(1)
    #     CP.change_password(self.password, "123456789", "123456789")
    #     time.sleep(1)
    #     CP.change_password(self.password, self.Email, self.Email)
    #     time.sleep(3)
