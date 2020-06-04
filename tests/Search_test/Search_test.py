from Pages.Search.SearchPage import SearchPage
import unittest
import pytest
import time


@pytest.mark.usefixtures("oneTime_Login_SetUp", "login_set_up")
class TestSearch(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp):
        self.Search = SearchPage(self.driver)
        time.sleep(1)
        self.Search.click_search_window()

    def test_a_search_artist(self):
        time.sleep(1)
        self.Search.send_in_search_tab("Mohamed ramadan")
        time.sleep(1)
        self.Search.click_searched_artist()
        time.sleep(1)
        # if we have time make here screenshot

    def test_b_search_song(self):
        time.sleep(1)
        self.Search.send_in_search_tab("sting ya king")
        time.sleep(1)
        self.Search.click_searched_song()
        time.sleep(20)

    def test_c_search_partial_artist_name(self):
        self.Search.send_in_search_tab("Mohamed rama")
        time.sleep(1)
        self.Search.click_searched_artist()
        time.sleep(1)

    def test_d_search_partial_song_name(self):
        self.Search.send_in_search_tab("sting ya k")
        time.sleep(1)
        self.Search.click_searched_song()
        time.sleep(20)
