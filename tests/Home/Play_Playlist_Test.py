import time
from Pages.Home.Play_Playlist import PlayPlaylist
import unittest
import pytest


@pytest.mark.usefixtures("oneTime_Login_SetUp_Webplayer", "Login_setUp")
class PlayList(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp_Webplayer):
        self.PP = PlayPlaylist(self.Driver)

    def test_Playlist(self):
        # play random song and then go to the playlist, firstly show the songs in playlist and them play it
        self.PP.play_playlist()
        time.sleep(5)
