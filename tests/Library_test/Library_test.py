import unittest
import pytest
import time
from web.pages.Library.Library_Page import LibraryPage


@pytest.mark.usefixtures("oneTime_Login_SetUp", "login_set_up")
class TestLibrary(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp):
        self.Library = LibraryPage(self.driver)
        time.sleep(1)
        self.Library.click_library()

    def test_a_all(self):
        time.sleep(1)
        self.Library.click_podcast()
        self.Library.click_albums()
        self.Library.click_playlist()
        self.Library.click_artist()
        time.sleep(1)

    def test_b_playlist(self):
        self.Library.click_playlist()
        self.Library.click_first_playlist()
        time.sleep(1)

    def test_c_album(self):
        self.Library.click_albums()
        self.Library.click_first_album()
        time.sleep(1)

    def test_d_artist(self):
        self.Library.click_artist()
        time.sleep(1)
        self.Library.click_find_artist()
        time.sleep(1)
