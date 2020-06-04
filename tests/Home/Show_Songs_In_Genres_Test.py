from Pages.Home.Show_Songs_In_Genres import ShowSongs
import unittest
import pytest


@pytest.mark.usefixtures("oneTime_Login_SetUp_Webplayer", "Login_setUp")
class SongsInGenres(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp_Webplayer):
        self.SS = ShowSongs(self.Driver)

    def test_Show_Songs_In_All_Genres(self):
        self.SS.show_songs_in_all_genres()
