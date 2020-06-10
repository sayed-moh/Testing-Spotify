import unittest
import pytest
import time
from pages.WebPlayer.WebPlayerPage import WebPlayerPage
from pages.Account.AccountPage import AccountPage


@pytest.mark.usefixtures("oneTime_Login_SetUp", "login_set_up")
class TestDeleteRestore(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp):
        self.Account = AccountPage(self.driver)
        self.WebPlayer = WebPlayerPage(self.driver)

    def test_delete_playlist(self):
        time.sleep(1)
        self.WebPlayer.open_my_playlist()
        time.sleep(1)
        self.WebPlayer.click_refresh()
        time.sleep(2)
        self.WebPlayer.click_more_album_button()
        time.sleep(1)
        self.WebPlayer.click_delete_button()
        time.sleep(1)
        self.WebPlayer.click_confirm_delete()
        time.sleep(1)

    def test_restore_playlist(self):
        time.sleep(1)
        self.WebPlayer.click_user_widget()
        time.sleep(1)
        self.WebPlayer.click_account()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(1)
        self.Account.click_recover_playlists()
        time.sleep(1)
        self.Account.click_restore()
        time.sleep(1)
