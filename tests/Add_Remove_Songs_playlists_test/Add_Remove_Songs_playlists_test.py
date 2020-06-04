from Pages.Search.SearchPage import SearchPage
import unittest
import pytest
import time
from Pages.Add_Remove_Songs_Playlist.AddRemoveSongsPlaylistsPage import AddRemoveSongsPlaylistsPage


@pytest.mark.usefixtures("oneTime_Login_SetUp", "login_set_up")
class TestAddRemove(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp):
        self.Search = SearchPage(self.driver)
        self.Add = AddRemoveSongsPlaylistsPage(self.driver)

    def test_a_search_add_song(self):
        time.sleep(1)
        self.Search.click_search_window()
        self.Search.send_in_search_tab("sting ya king")
        time.sleep(2)
        self.Search.click_searched_song()
        time.sleep(1)
        self.Add.click_options()
        self.Add.open_my_playlist()

    def test_b_add_from_playlist(self):
        time.sleep(1)
        self.Add.open_my_playlist()
        time.sleep(1)
        self.Add.click_refresh()
        time.sleep(1)
        self.Add.click_add_button()
        time.sleep(1)

    def test_c_remove_song(self):
        time.sleep(1)
        self.Add.element_click("Test", "link")
        self.Add.open_my_playlist()
        self.Add.remove_song()

    def test_d_add_from_upper_options(self):
        time.sleep(1)
        self.Search.click_search_window()
        self.Search.send_in_search_tab("sting ya king")
        time.sleep(2)
        self.Search.click_searched_song()
        time.sleep(1)
        self.Add.add_playlist_from_upper_options()

    def test_e_home_song(self):
        time.sleep(1)
        self.Add.click_home()
        self.Add.click_target_playlist()
        self.Add.get_song_home_playlist()
        time.sleep(1)
