from web.base.Web_Driver_Factory import WebDriverFactory
from web.base.Selenium_Driver import SeleniumDriver
import unittest
from web.pages.Login.LoginPage import LoginPage
from web.pages.Add_Remove_Songs_Playlist.AddRemoveSongsPlaylistsPage import AddRemoveSongsPlaylistsPage
from web.pages.Search.SearchPage import SearchPage
from web.pages.Library.Library_Page import LibraryPage
from web.pages.Play_Pause.PlayPausePage import PlayPausePage


class TestStress(unittest.TestCase, SeleniumDriver):
    wdf = WebDriverFactory("chrome")
    Driver = wdf.get_web_driver_instance()
    LP = LoginPage(Driver)
    Add = AddRemoveSongsPlaylistsPage(Driver)
    Search = SearchPage(Driver)
    Library = LibraryPage(Driver)
    PP = PlayPausePage(Driver)
    LP.login_fn("modyseka@gmail.com", "1234567891011")

    def test_Web(self):
        for x in range(1000):
            self.Add.click_home()
            self.Search.click_search_window()
            self.Library.click_library()

    def test_Play_Pause(self):
        for x in range(1000):
            self.PP.click_play_pause()
