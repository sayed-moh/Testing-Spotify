import time
from selenium import webdriver
from Pages.Home.Play_Playlist import Play_Playlist
import unittest
import pytest
@pytest.mark.usefixtures("oneTime_Login_SetUp_Webplayer", "Login_setUp")
class Play_list(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp_Webplayer):
        self.PP = Play_Playlist(self.Driver)

    def test_Playlist(self):
        # play random song and then go to the playlist, firstly show the songs in playlist and them play it
        self.PP.Play_Playlist()
        time.sleep(5)
