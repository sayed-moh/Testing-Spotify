from web.pages.Add_Remove_Songs_Playlist.AddRemoveSongsPlaylistsPage import AddRemoveSongsPlaylistsPage
from web.pages.Play_Pause.PlayPausePage import PlayPausePage
import unittest
import pytest
import time


@pytest.mark.usefixtures("oneTime_Login_SetUp", "login_set_up")
class TestPlayPause(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp):
        self.AR = AddRemoveSongsPlaylistsPage(self.driver)
        self.PP = PlayPausePage(self.driver)
        time.sleep(1)
        self.AR.open_my_playlist()

    def test_a_play(self):
        time.sleep(1)
        self.PP.play_playlist()
        self.PP.click_play_pause()
        self.PP.click_next()
        self.PP.click_previous()

    def test_b_queue(self):
        self.PP.queue_play()
        self.PP.click_play_pause()
        self.PP.click_next()
        time.sleep(2)

    def test_c_sound(self):
        self.PP.click_play_pause()
        time.sleep(2)
        self.PP.slider_sound()
        time.sleep(2)

    def test_d_sound_off(self):
        self.PP.click_play_pause()
        time.sleep(2)
        self.PP.sound_btn()
        time.sleep(2)
        self.PP.sound_btn()
        time.sleep(1)
