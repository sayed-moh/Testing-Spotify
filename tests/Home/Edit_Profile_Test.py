import time

import pytest
from selenium import webdriver
from Pages.Home.Edit_Profile import Edit_Page
import unittest

@pytest.mark.usefixtures("oneTime_Login_SetUp_Edit", "Login_setUp")
class Test_EditProfile(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp_Edit):

        self.Password = "1234567891011"
        self.Email_1 = "modyseka@gmail.com"
        self.Email_2 = "ahmed.gaber428@yahoo.com"
        self.Mobile = "01033811138"

        self.EP = Edit_Page(self.Driver)


    # This compelete Scenario if you want to
    # def test_Change_phone_All_Scenarios(self):
    #
    #     self.EP.Change_Mobile_No("abc")
    #     self.EP.Change_Mobile_No("abc@gmailcom")
    #     self.EP.Change_Mobile_No("0")
    #     self.EP.Change_Mobile_No("0258956599999999999999999999999999999999999999999999999999999999999999")
    #     # It accepts any type of characters less than 20 character
    #     self.EP.Change_Mobile_No(self.Mobile)
    #     time.sleep(2)
    #     # Using sleep to can see what happened
    #     # Driver.quit()

    def test_Change_phone_Scenario_1(self):

        # will accept it as Phone number
        self.EP.Change_Mobile_No("abc")
        time.sleep(2)
        # Driver.quit()

    def test_Change_phone_Scenario_2(self):
        # will accept it as Phone number
        self.EP.Change_Mobile_No("abc@gmailcom")
        time.sleep(2)
        # Driver.quit()
    def test_Change_phone_Scenario_3(self):
        # will accept it as Phone number
        self.EP.Change_Mobile_No("0")
        time.sleep(2)
        # Driver.quit()
    def test_Change_Phone_Scenario_4(self):
        # will not accept because more than 20 character
        self.EP.Change_Mobile_No("0258956599999999999999999999999999999999999999999999999999999999999999")
        time.sleep(2)
        # Driver.quit()

    def test_Change_Phone_Scenario_5(self):
        self.EP.Change_Mobile_No(self.Mobile)
        time.sleep(2)
        # Driver.quit()

    def test_Change_year_All_Scenario(self):
        # try to choose year is not appear in years box
        self.EP.Change_Year("0000")
        # it will not save it as less than 21 years old and refuse any date less than 21
        self.EP.Change_Year("2000")
        # it will save it and it is very old it !!!!!!!!!
        self.EP.Change_Year("1900")
        # try normal year
        self.EP.Change_Year("1995")
        time.sleep(2)
        # Driver.quit()

    def test_Change_Months_All_Scenario(self):
        # try normal month
        self.EP.Change_Month("05")
        # try to choose month is not appear in month box
        self.EP.Change_Month("13")
        time.sleep(2)
        # Driver.quit()

    def test_Change_Days_All_Scenario(self):
        # try to choose Day is not appear in Day box
        self.EP.Change_Day("32")
        # try normal month
        self.EP.Change_Day("20")
        time.sleep(2)
        # Driver.quit()

    def test_Change_Gender_All_Scenario(self):
        self.EP.Change_Gender("Female")
        self.EP.Change_Gender("asm")
        self.EP.Change_Gender("Male")
        time.sleep(2)
        # Driver.quit()

    def test_Change_Brith_date_All_Scenario(self):
        # It will not accept it as february 28 days only
        self.EP.Change_Brith_date("31", "02", "1998")
        # It will not accept it as April 30 days only
        self.EP.Change_Brith_date("31", "04", "1998")
        # It will not accept it as june 30 days only
        self.EP.Change_Brith_date("31", "06", "1998")
        # It will not accept it as september 30 days only
        self.EP.Change_Brith_date("31", "09", "1998")
        # It will not accept it as november 30 days only
        self.EP.Change_Brith_date("31", "11", "1998")
        # It will not accept it as february 28 days only
        self.EP.Change_Brith_date("30", "02", "1998")
        # It will not accept it as 1998 is not Leap year
        self.EP.Change_Brith_date("29", "02", "1998")
        # It will not accept it as this date less than 21 years old
        self.EP.Change_Brith_date("30", "09", "1999")
        # It will accept it as 1996 is Leap year
        self.EP.Change_Brith_date("29", "02", "1996")
        # It will accept it as march 31 day
        self.EP.Change_Brith_date("31", "03", "1998")
        time.sleep(2)
        # Driver.quit()

    def test_Change_Email_Successfully(self):
        self.EP.Change_Email(self.Password, self.Email_2)
        self.EP.Logout_Edit()
        self.EP.Log_In_Edit(self.Email_2, self.Password)
        self.EP.Change_Email(self.Password, self.Email_1)
        time.sleep(2)
        # Driver.quit()

    def test_Change_Email_Failed_Scenarios(self):
        self.EP.Change_Email(self.Password, "a@yahoo.com")
        self.EP.Change_Email(self.Password, "abcd")
        self.EP.Change_Email(self.Password, "modyseka@.com")
        self.EP.Change_Email(self.Password, "modyseka@@gmail.com")
        self.EP.Change_Email(self.Password, "@gmail.com")
        self.EP.Change_Email(self.Password, "modyseka@gmail.commmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
        self.EP.Change_Email("abcd", self.Email_2)
        self.EP.Change_Email(self.Password, " ")
        time.sleep(2)
        # Driver.quit()

    def test_Change_All_Successfully(self):
        self.EP.Change_All(self.Email_2, self.Password, "Female", "10", "07", "1995", self.Mobile)
        self.EP.Change_All(self.Email_1, self.Password, "Male", "15", "09", "1997", self.Mobile)
        time.sleep(2)
        # Driver.quit()

    def test_Change_All_Failed_Scenarios(self):
        self.EP.Log_In_Edit(self.Email_1, self.Password)
        self.EP.Change_All("abc", self.Password, "Male", "15", "09", "1997", self.Mobile)
        self.EP.Change_All("a@yahoo.com", self.Password, "Male", "15", "09", "1997", self.Mobile)
        self.EP.Change_All("123", self.Password, "Male", "15", "09", "1997", self.Mobile)
        self.EP.Change_All(" ", self.Password, "Male", "15", "09", "1997", self.Mobile)
        self.EP.Change_All(self.Email_2, self.Password, "Male", "15", "09", "2001", self.Mobile)
        self.EP.Change_All(self.Email_2, self.Password, "Male", "31", "09", "1997", self.Mobile)
        self.EP.Change_All(self.Email_2, "00000", "Male", "15", "09", "1997", self.Mobile)
        time.sleep(2)
        # Driver.quit()

    def test_Change_Phone_Facebook_Account(self):
        self.EP.Logout_Edit()
        self.EP.Login_Facebook_Edit("01033811138","ahmedgaber")
        self.EP.Change_Mobile_No("abc@")
        self.EP.Change_Mobile_No("0")
        self.EP.Change_Mobile_No("!@#$%^&*()")
        self.EP.Change_Mobile_No(self.Mobile)
        self.EP.Change_Mobile_No("55555555555555555555555555555555555555555555555555555555555")
        time.sleep(3)