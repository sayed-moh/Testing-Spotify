import unittest
import pytest
import time
from pages.WebPlayer.WebPlayerPage import WebPlayerPage
from pages.Search.SearchPage import SearchPage


@pytest.mark.usefixtures("oneTime_Login_SetUp", "login_set_up")
class TestCopy(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp):
        self.Search = SearchPage(self.driver)
        self.WebPlayer = WebPlayerPage(self.driver)

    def test_copy_song_link(self):
        time.sleep(1)
        self.Search.click_search_window()
        self.Search.send_in_search_tab("bad guy")
        time.sleep(1)
        self.Search.click_searched_song()
        time.sleep(2)
        self.WebPlayer.click_refresh()
        time.sleep(2)
        self.WebPlayer.click_hidden_more_song_button()
        time.sleep(2)
        self.WebPlayer.click_more_song_button()
        time.sleep(1)
        self.WebPlayer.click_copy_song()
        time.sleep(1)

    def test_copy_album_link(self):
        time.sleep(1)
        self.Search.click_search_window()
        self.Search.send_in_search_tab("WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?")
        time.sleep(2)
        self.Search.click_searched_song()
        time.sleep(2)
        self.WebPlayer.click_refresh()
        time.sleep(2)
        self.WebPlayer.click_more_album_button()
        time.sleep(1)
        self.WebPlayer.click_copy_album()
        time.sleep(1)
