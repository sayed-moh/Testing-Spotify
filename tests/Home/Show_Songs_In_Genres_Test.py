import time
from selenium import webdriver
from Pages.Home.Show_Songs_In_Genres import Show_Songs
import unittest
import pytest
@pytest.mark.usefixtures("oneTime_Login_SetUp_Webplayer", "Login_setUp")
class Songs_In_Genres(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTime_Login_SetUp_Webplayer):
        self.SS = Show_Songs(self.Driver)

    def test_Show_Songs_In_All_Genres(self):
        self.SS.Show_Songs_In_All_Genres()