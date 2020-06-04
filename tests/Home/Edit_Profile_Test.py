import time
import pytest
from Pages.Home.Edit_Profile import EditPage
import unittest


@pytest.mark.usefixtures("oneTime_Login_SetUp_Edit", "Login_setUp")
class TestEditProfile(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp_Edit):
        self.Password = "1234567891011"
        self.Email_1 = "modyseka@gmail.com"
        self.Email_2 = "ahmed.gaber428@yahoo.com"
        self.Mobile = "01033811138"

        self.EP = EditPage(self.Driver)

    # This compelete Scenario if you want to
    # def test_Change_phone_All_Scenarios(self):
    #
    #     self.EP.change_mobile_no("abc")
    #     self.EP.change_mobile_no("abc@gmailcom")
    #     self.EP.change_mobile_no("0")
    #     self.EP.change_mobile_no("0258956599999999999999999999999999999999999999999999999999999999999999")
    #     # It accepts any type of characters less than 20 character
    #     self.EP.change_mobile_no(self.Mobile)
    #     time.sleep(2)
    #     # Using sleep to can see what happened
    #     # driver.quit()

    def test_Change_phone_Scenario_1(self):
        # will accept it as Phone number
        self.EP.change_mobile_no("abc")
        time.sleep(2)
        # driver.quit()

    def test_Change_phone_Scenario_2(self):
        # will accept it as Phone number
        self.EP.change_mobile_no("abc@gmailcom")
        time.sleep(2)
        # driver.quit()

    def test_Change_phone_Scenario_3(self):
        # will accept it as Phone number
        self.EP.change_mobile_no("0")
        time.sleep(2)
        # driver.quit()

    def test_Change_Phone_Scenario_4(self):
        # will not accept because more than 20 character
        self.EP.change_mobile_no("0258956599999999999999999999999999999999999999999999999999999999999999")
        time.sleep(2)
        # driver.quit()

    def test_Change_Phone_Scenario_5(self):
        self.EP.change_mobile_no(self.Mobile)
        time.sleep(2)
        # driver.quit()

    def test_Change_year_All_Scenario(self):
        # try to choose year is not appear in years box
        self.EP.change_year("0000")
        # it will not save it as less than 21 years old and refuse any date less than 21
        self.EP.change_year("2000")
        # it will save it and it is very old it !!!!!!!!!
        self.EP.change_year("1900")
        # try normal year
        self.EP.change_year("1995")
        time.sleep(2)
        # driver.quit()

    def test_Change_Months_All_Scenario(self):
        # try normal month
        self.EP.change_month("05")
        # try to choose month is not appear in month box
        self.EP.change_month("13")
        time.sleep(2)
        # driver.quit()

    def test_Change_Days_All_Scenario(self):
        # try to choose day is not appear in day box
        self.EP.change_day("32")
        # try normal month
        self.EP.change_day("20")
        time.sleep(2)
        # driver.quit()

    def test_Change_Gender_All_Scenario(self):
        self.EP.change_gender1("Female")
        self.EP.change_gender1("asm")
        self.EP.change_gender1("Male")
        time.sleep(2)
        # driver.quit()

    def test_Change_Brith_date_All_Scenario(self):
        # It will not accept it as february 28 days only
        self.EP.change_birth_date("31", "02", "1998")
        # It will not accept it as April 30 days only
        self.EP.change_birth_date("31", "04", "1998")
        # It will not accept it as june 30 days only
        self.EP.change_birth_date("31", "06", "1998")
        # It will not accept it as september 30 days only
        self.EP.change_birth_date("31", "09", "1998")
        # It will not accept it as november 30 days only
        self.EP.change_birth_date("31", "11", "1998")
        # It will not accept it as february 28 days only
        self.EP.change_birth_date("30", "02", "1998")
        # It will not accept it as 1998 is not Leap year
        self.EP.change_birth_date("29", "02", "1998")
        # It will not accept it as this date less than 21 years old
        self.EP.change_birth_date("30", "09", "1999")
        # It will accept it as 1996 is Leap year
        self.EP.change_birth_date("29", "02", "1996")
        # It will accept it as march 31 day
        self.EP.change_birth_date("31", "03", "1998")
        time.sleep(2)
        # driver.quit()

    def test_Change_Email_Successfully(self):
        self.EP.change_email1(self.Password, self.Email_2)
        self.EP.logout_edit()
        self.EP.log_in_edit(self.Email_2, self.Password)
        self.EP.change_email1(self.Password, self.Email_1)
        time.sleep(2)
        # driver.quit()

    def test_Change_Email_Failed_Scenarios(self):
        self.EP.change_email1(self.Password, "a@yahoo.com")
        self.EP.change_email1(self.Password, "abcd")
        self.EP.change_email1(self.Password, "modyseka@.com")
        self.EP.change_email1(self.Password, "modyseka@@gmail.com")
        self.EP.change_email1(self.Password, "@gmail.com")
        self.EP.change_email1(self.Password,
                              "modyseka@gmail.commmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
        self.EP.change_email1("abcd", self.Email_2)
        self.EP.change_email1(self.Password, " ")
        time.sleep(2)
        # driver.quit()

    def test_Change_All_Successfully(self):
        self.EP.change_all(self.Email_2, self.Password, "Female", "10", "07", "1995", self.Mobile)
        self.EP.change_all(self.Email_1, self.Password, "Male", "15", "09", "1997", self.Mobile)
        time.sleep(2)
        # driver.quit()

    def test_Change_All_Failed_Scenarios(self):
        self.EP.log_in_edit(self.Email_1, self.Password)
        self.EP.change_all("abc", self.Password, "Male", "15", "09", "1997", self.Mobile)
        self.EP.change_all("a@yahoo.com", self.Password, "Male", "15", "09", "1997", self.Mobile)
        self.EP.change_all("123", self.Password, "Male", "15", "09", "1997", self.Mobile)
        self.EP.change_all(" ", self.Password, "Male", "15", "09", "1997", self.Mobile)
        self.EP.change_all(self.Email_2, self.Password, "Male", "15", "09", "2001", self.Mobile)
        self.EP.change_all(self.Email_2, self.Password, "Male", "31", "09", "1997", self.Mobile)
        self.EP.change_all(self.Email_2, "00000", "Male", "15", "09", "1997", self.Mobile)
        time.sleep(2)
        # driver.quit()

    def test_Change_Phone_Facebook_Account(self):
        self.EP.logout_edit()
        self.EP.login_facebook_edit("01033811138", "ahmedgaber")
        self.EP.change_mobile_no("abc@")
        self.EP.change_mobile_no("0")
        self.EP.change_mobile_no("!@#$%^&*()")
        self.EP.change_mobile_no(self.Mobile)
        self.EP.change_mobile_no("55555555555555555555555555555555555555555555555555555555555")
        time.sleep(3)
