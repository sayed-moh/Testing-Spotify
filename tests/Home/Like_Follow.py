import time
from selenium import webdriver
from Pages.Home.Like_Song_Follow_Artist import Like_Follow
import unittest
import pytest
@pytest.mark.usefixtures("oneTime_Login_SetUp_Webplayer", "Login_setUp")
class Like_Follow_Class(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp_Webplayer):
        self.Lf = Like_Follow(self.Driver)

    def test_Like_And_Follow(self):
        self.Lf.Like_Follow_Test()
        time.sleep(5)

    def test_Like(self):
        self.Lf.Like_Test()
        time.sleep(5)

