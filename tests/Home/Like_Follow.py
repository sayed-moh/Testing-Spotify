import time
from Pages.Home.Like_Song_Follow_Artist import Like_Follow
import unittest
import pytest


@pytest.mark.usefixtures("oneTime_Login_SetUp_Webplayer", "Login_setUp")
class LikeFollowClass(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp_Webplayer):
        self.Lf = Like_Follow(self.Driver)

    def test_Like_And_Follow(self):
        self.Lf.like_follow_test()
        time.sleep(5)

    def test_Like(self):
        self.Lf.like_test()
        time.sleep(5)
