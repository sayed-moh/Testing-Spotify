from Base.Selenium_Driver import SeleniumDriver
import time


class EditPage(SeleniumDriver):
    def __init__(self, driver):
        # super().__init__(driver)
        self.Driver = driver

    login_link = "Log In"
    email_field = "login-username"
    password_field = "login-password"  # link
    login_button = "login-button"
    Edit_profile = "Edit profile"  # link
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
    remember_me = "control-indicator"
    facebook_button = "btn-facebook"
    facebook_username = "email"
    facebook_password = "pass"
    facebook_login = "login_button"

    def enter_email(self, email):
        self.send_keys(email, self.email_field)

    def enter_password(self, password):
        self.send_keys(password, self.password_field)

    def enter_confirm_password(self, password):
        self.send_keys(password, self.confirm_password)

    def click_login_link(self):
        self.element_click(self.login_link, "link")

    def click_remember(self):
        self.element_click(self.remember_me, "class")

    def click_login_button(self):
        self.element_click(self.login_button)

    def click_edit_profile(self):
        self.element_click(self.Edit_profile, "link")

    def change_mobile(self, data):
        self.send_keys(data, self.mobile)

    def change_monthes(self, data):
        self.select_item(data, self.Months)

    def change_days(self, data):
        self.select_item(data, self.Days)

    def change_years(self, data):
        self.select_item(data, self.Years)

    def change_email(self, email):
        self.send_keys(email, self.Profile_Email)

    def change_gender(self, data):
        self.select_item(data, self.gender)

    def click_menu(self):
        self.element_click(self.menu, "class")

    def click_logout(self):
        time.sleep(1.5)
        self.element_click(self.logout, "link")

    def click_save(self):
        self.element_click(self.save_profile)

    def click_cancel(self):
        self.element_click(self.cancel)

    def click_facebook_button(self):
        self.element_click(self.facebook_button, "class")

    def click_facebook_login(self):
        self.element_click(self.facebook_login)

    def enter_facebook_username(self, email):
        self.send_keys(email, self.facebook_username)

    def enter_facebook_password(self, password):
        self.send_keys(password, self.facebook_password)

    def clear_email(self):
        self.clears(self.email_field)

    def clear_password(self):
        self.clears(self.confirm_password)

    def clear_mobile(self):
        self.clears(self.mobile)

    def clear_change_email(self):
        self.clears(self.Profile_Email)

    def log_in_edit(self, email, password):
        time.sleep(1)
        self.click_login_link()
        time.sleep(1)
        self.enter_email(email)
        self.enter_password(password)
        self.click_remember()
        self.click_login_button()
        time.sleep(1)
        self.click_edit_profile()

    def logout_edit(self):
        self.click_menu()
        self.click_logout()

    def change_mobile_no(self, new_mobile):
        time.sleep(1.5)
        self.clear_mobile()
        self.send_keys(new_mobile, self.mobile)
        self.click_save()

    def change_day(self, day):
        time.sleep(2)
        self.select_item(day, self.Days)
        self.click_save()

    def change_month(self, month):
        time.sleep(1.5)
        self.select_item(month, self.Months)
        self.click_save()

    def change_year(self, year):
        time.sleep(1)
        self.select_item(year, self.Years)
        self.click_save()

    def change_gender1(self, gender):
        time.sleep(2)
        self.change_gender(gender)
        self.click_save()

    def change_birth_date(self, day, month, year):
        time.sleep(2)
        self.select_item(day, self.Days)
        self.select_item(month, self.Months)
        self.select_item(year, self.Years)
        self.click_save()

    def change_email1(self, password, new_email):
        time.sleep(2)
        self.clear_change_email()
        self.clear_password()
        self.change_email(new_email)
        self.enter_confirm_password(password)
        self.click_save()

    def change_all(self, new_email, password, gender, day, month, year, new_mobile):
        time.sleep(1)
        self.clear_change_email()
        self.clear_password()
        self.change_email(new_email)
        self.enter_confirm_password(password)
        self.change_gender(gender)
        self.select_item(day, self.Days)
        self.select_item(month, self.Months)
        self.select_item(year, self.Years)
        self.clear_mobile()
        self.send_keys(new_mobile, self.mobile)
        self.click_save()

    def login_facebook_edit(self, username, password):
        self.click_login_link()
        time.sleep(1)
        self.click_facebook_button()
        self.enter_facebook_username(username)
        self.enter_facebook_password(password)
        self.click_facebook_login()
        time.sleep(4)
        self.click_edit_profile()
