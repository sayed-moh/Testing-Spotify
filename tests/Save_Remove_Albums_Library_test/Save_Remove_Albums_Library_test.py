import unittest
import pytest
import time
from pages.WebPlayer.WebPlayerPage import WebPlayerPage
from pages.Search.SearchPage import SearchPage
from pages.Library.Library_Page import LibraryPage


@pytest.mark.usefixtures("oneTime_Login_SetUp", "login_set_up")
class TestSaveRemoveAlbums(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp):
        self.Search = SearchPage(self.driver)
        self.WebPlayer = WebPlayerPage(self.driver)
        self.Library = LibraryPage(self.driver)

    def test_save_album_from_search(self):
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
        self.WebPlayer.click_save_album()
        time.sleep(1)

    def test_remove_album_from_search(self):
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
        self.WebPlayer.click_remove_album()
        time.sleep(1)

    def test_remove_album_from_library(self):
        self.test_save_album_from_search()
        time.sleep(1)
        self.Library.click_library()
        time.sleep(1)
        self.Library.click_albums()
        time.sleep(1)
        self.Library.click_first_album()
        time.sleep(1)
        self.WebPlayer.click_more_album_button()
        time.sleep(1)
        self.WebPlayer.click_remove_album()
        time.sleep(1)
