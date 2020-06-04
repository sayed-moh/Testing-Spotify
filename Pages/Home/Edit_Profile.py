from Base.Selenium_Driver import SeleniumDriver
import time

class Edit_Page(SeleniumDriver):
    def __init__(self, Driver):
        # super().__init__(Driver)
        self.Driver =Driver

    Loginlink = "Log In"
    emailfield = "login-username"
    passwordfield = "login-password"  # link
    loginbutton = "login-button"
    Editprofile = "Edit profile"  # link
    gender = "profile_gender"  # id
    Months = "profile_birthdate_month"  # id
    Days = "profile_birthdate_day"  # id
    Years = "profile_birthdate_year"  # id
    mobile = "profile_mobile_number"  # id
    save_profile = "profile_save_profile"  # id
    cancel = "profile_cancel"  # id
    confirm_password = "profile_confirmPassword"  # id
    Profile_Email = "profile_email"  # id
    menu = "svelte-kdyqkb"
    logout = "Log Out"
    Remember_me ="control-indicator"
    Facebook_Button = "btn-facebook"
    Facebook_Username = "email"
    Facebook_Password = "pass"
    Facebook_Login = "loginbutton"


    def entereamil(self, email):
         self.SendKeys(email, self.emailfield)

    def enterpassword(self, password):
         self.SendKeys(password, self.passwordfield)

    def enter_confirm_password(self, password):
        self.SendKeys(password, self.confirm_password)


    def clickloginlink(self):
         self.ElementClick(self.Loginlink, "link")

    def clickremember(self):
        self.ElementClick(self.Remember_me, "class")

    def clickloginbutton(self):
         self.ElementClick(self.loginbutton)

    def Click_Edit_Profile(self):
        self.ElementClick(self.Editprofile, "link")

    def change_mobile(self,data):
        self.SendKeys(data, self.mobile)

    def change_monthes(self, data):
        self.SelectItem(data, self.Months)

    def chanege_days(self, data):
        self.SelectItem(data, self.Days)

    def change_years(self, data):
        self.SelectItem(data, self.Years)

    def change_email(self, email):
         self.SendKeys(email, self.Profile_Email)

    def change_gender(self, data):
        self.SelectItem(data, self.gender)

    def clickmenu(self):
        self.ElementClick(self.menu, "class")

    def clicklogout(self):
        time.sleep(1.5)
        self.ElementClick(self.logout, "link")

    def clickSave(self):
        self.ElementClick(self.save_profile)

    def click_Cancel(self):
        self.ElementClick(self.cancel)

    def Click_Facebook_Button(self):
        self.ElementClick(self.Facebook_Button, "class")

    def Click_Facebook_Login(self):
        self.ElementClick(self.Facebook_Login)

    def Enter_Facebook_Username(self, email):
        self.SendKeys(email, self.Facebook_Username)

    def Enter_Facebook_Password(self, password):
        self.SendKeys(password, self.Facebook_Password)


    def clear_email(self):
        self.Clears(self.emailfield)

    def clear_password(self):
        self.Clears(self.confirm_password)

    def clear_mobile(self):
        self.Clears(self.mobile)

    def clear_change_email(self):
        self.Clears(self.Profile_Email)

    def Log_In_Edit(self, email, password):
        time.sleep(1)
        self.clickloginlink()
        time.sleep(1)
        self.entereamil(email)
        self.enterpassword(password)
        self.clickremember()
        self.clickloginbutton()
        time.sleep(1)
        self.Click_Edit_Profile()

    def Logout_Edit(self):
        self.clickmenu()
        self.clicklogout()


    def Change_Mobile_No(self, newmobile):
        time.sleep(1.5)
        self.clear_mobile()
        self.SendKeys(newmobile, self.mobile)
        self.clickSave()

    def Change_Day(self, Day):
        time.sleep(2)
        self.SelectItem(Day, self.Days)
        self.clickSave()

    def Change_Month(self, Month):
        time.sleep(1.5)
        self.SelectItem(Month, self.Months)
        self.clickSave()

    def Change_Year(self, Year):
        time.sleep(1)
        self.SelectItem(Year, self.Years)
        self.clickSave()

    def Change_Gender(self, gender):
        time.sleep(2)
        self.change_gender(gender)
        self.clickSave()

    def Change_Brith_date(self, Day, Month, Year):
        time.sleep(2)
        self.SelectItem(Day, self.Days)
        self.SelectItem(Month, self.Months)
        self.SelectItem(Year, self.Years)
        self.clickSave()

    def Change_Email(self, Password, New_email):
        time.sleep(2)
        self.clear_change_email()
        self.clear_password()
        self.change_email(New_email)
        self.enter_confirm_password(Password)
        self.clickSave()

    def Change_All(self, New_Email, Password, Gender, Day, Month, Year, New_Mobile):
        time.sleep(1)
        self.clear_change_email()
        self.clear_password()
        self.change_email(New_Email)
        self.enter_confirm_password(Password)
        self.change_gender(Gender)
        self.SelectItem(Day, self.Days)
        self.SelectItem(Month, self.Months)
        self.SelectItem(Year, self.Years)
        self.clear_mobile()
        self.SendKeys(New_Mobile, self.mobile)
        self.clickSave()

    def Login_Facebook_Edit(self, Username, Password):
        self.clickloginlink()
        time.sleep(1)
        self.Click_Facebook_Button()
        self.Enter_Facebook_Username(Username)
        self.Enter_Facebook_Password(Password)
        self.Click_Facebook_Login()
        time.sleep(4)
        self.Click_Edit_Profile()