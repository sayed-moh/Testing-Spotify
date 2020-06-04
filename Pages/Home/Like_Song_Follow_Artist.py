from Base.Selenium_Driver import SeleniumDriver
import time

class Like_Follow(SeleniumDriver):

    def __init__(self, Driver):
        super().__init__(Driver)
        self.driver = Driver

        # Locators Used in test


    Happy_Hits = "Happy Hits!" # link
    Mood = "Mood Booster"# link
    Mood_Song1 = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[1]/div/li"
    Mood_Song2 = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[2]/div/li"
    Mood_Song3 = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[3]/div/li"
    Song = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[4]/section/ol/div[1]/div/li"
    Like = "/html/body/div[4]/div/div[2]/div[3]/footer/div/div[1]/div/div[3]/button"
    Liked_List = "Liked Songs"
    Artist = "Amr Diab"
    Follow = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button[2]"
    Library = "Your Library"
    Your_Artist = "Artists"
    Playlist = "Test"
    Back = "/html/body/div[4]/div/div[2]/div[1]/header/div[2]/button[1]"
    Home = "Home"


    def click_Happy_Hits(self):
        self.ElementClick(self.Happy_Hits, "link")

    def click_Liked_List(self):
        self.ElementClick(self.Liked_List, "link")

    def Click_On_Playlist(self):
        self.ElementClick(self.Playlist, "link")

    def click_Artist(self):
        self.ElementClick(self.Liked_List, "link")

    def Click_Library(self):
        self.ElementClick(self.Library, "Link")

    def Click_Artists(self):
        self.ElementClick(self.Your_Artist, "Link")

    def Click_Like(self):
        self.ElementClick(self.Like, "xpath")

    def Click_Back(self):
        self.ElementClick(self.Back, "xpath")

    def Click_Home(self):
        self.ElementClick(self.Home, "link")




    # all sleeps in the code to can see what happened and my internet is not good
    def Like_Follow_Test(self):
        time.sleep(4)
        self.Click_On_Playlist()
        self.Hover_Listed_Song(self.Song)
        time.sleep(3)
        self.Hover(self.Like)
        time.sleep(1)
        self.click_Liked_List()
        time.sleep(3)
        self.Hover(self.Like)
        time.sleep(1)
        self.Hover(self.Like)
        time.sleep(1)
        self.Hover(self.Artist, "Link")
        time.sleep(1)
        self.Hover(self.Follow)
        time.sleep(1)
        self.Click_Library()
        time.sleep(1)
        self.Click_Artists()
        time.sleep(1)
        self.Click_Back()
        time.sleep(1)
        self.Click_Back()
        time.sleep(1)
        self.Hover(self.Follow, "xpath")
        time.sleep(1)
        self.Click_Library()
        time.sleep(1)
        self.Click_Artists()
        time.sleep(1)
        self.click_Liked_List()
        time.sleep(1)
        self.Hover(self.Like)
        time.sleep(1)
        self.Click_Home()


    def Like_Test(self):
       time.sleep(4)
       self.Hover(self.Mood, "link")
       self.Hover_Listed_Song(self.Mood_Song1)
       time.sleep(3)
       self.Hover(self.Like)
       time.sleep(1)
       self.Hover_Listed_Song(self.Mood_Song2)
       time.sleep(3)
       self.Hover(self.Like)
       time.sleep(1)
       self.Hover_Listed_Song(self.Mood_Song3)
       time.sleep(3)
       self.Hover(self.Like)
       time.sleep(1)
       self.click_Liked_List()
       time.sleep(2)
       self.Hover_Listed_Song(self.Mood_Song3)
       time.sleep(3)
       self.Hover(self.Like)
       time.sleep(1)
       self.Hover_Listed_Song(self.Mood_Song2)
       time.sleep(3)
       self.Hover(self.Like)
       time.sleep(1)
       self.Hover_Listed_Song(self.Mood_Song1)
       time.sleep(3)
       self.Hover(self.Like)
       time.sleep(1)
       self.Click_Home()



