from Base.Selenium_Driver import SeleniumDriver
import time

class Show_Songs(SeleniumDriver):

    def __init__(self, Driver):
        super().__init__(Driver)
        self.driver = Driver

    # Locators Used in test
    Back = "/html/body/div[4]/div/div[2]/div[1]/header/div[2]/button[1]"
    Search_Button = "Search"  # link
    Pop_Genre = "Pop"  # link
    Electronic_Genre = "Electronic / Dance"
    Hip_Genre = "Hip-Hop"
    Podcasts_Genre = "Podcasts"
    Made_For_You_Genre = "Made For You"
    Charts_Genre = "Charts"
    New_Genre = "New Releases"
    Discover_Genre = "Discover"
    At_Home_Genre = "At Home"
    Arabic_Genre = "Arabic"
    Mood_Genre = "Mood"
    Decades_Genre = "Decades"
    Khaleeji_Genre = "Khaleeji"
    Gaming_Genre = "Gaming"
    Latin_Genre = "Latin"
    Afro_Genre = "Afro"
    Kpop_Genre = "K-Pop"
    Tastemakers_Genre = "Tastemakers"
    Wellness_Genre = "Wellness"
    Chill_Genre = "Chill"
    Workout_Genre = "Workout"
    Focus_Genre = "Focus"
    Party_Genre = "Party"
    Rock_Genre = "Rock"
    Sleep_Genre = "Sleep"
    Cooking_Dining_Genre = "Cooking & Dining"
    Jazz_Genre = "Jazz"
    R_B_Genre = "R&B"
    TV_Movies_Genre = "TV & Movies"
    Romance_Genre = "Romance"
    Indie_Genre = "Indie"
    Soul_Genre = "Soul"
    Classical_Genre = "Classical"
    Metal_Genre = "Metal"
    Kids_Family_Genre = "Kids & Family"
    Reggae_Genre = "Reggae"
    Blues_Genre = "Blues"
    Funk_Genre = "Funk"
    Punk_Genre = "Punk"
    Country_Genre = "Country"
    Folk_Acoustic_Genre = "Folk & Acoustic"
    Comedy_Genre = "Comedy"
    Travel_Genre = "Travel"
    Summer_Genre = "Summer"
    Genre_Playlist = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[3]/section[1]/div/div[2]/div/div/div[4]"




    def Click_Pop(self):
         self.ElementClick(self.Pop_Genre, "link")

    def Click_Back(self):
        self.ElementClick(self.Back, "xpath")


    def Click_On_Search(self):
         self.ElementClick(self.Search_Button, "link")



    def Show_Songs_In_All_Genres(self):
        time.sleep(2)
        self.Click_On_Search()
        time.sleep(2)
        self.Hover(self.Pop_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Electronic_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Arabic_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Podcasts_Genre, "link")
        time.sleep(1)
        self.Click_Back()

        self.Hover(self.Made_For_You_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Charts_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.New_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Discover_Genre , "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.At_Home_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        # self.Hover(self.Arabic_Genre, "link")
        # self.WaitForElement(self.Genre_Playlist, "xpath")
        # self.Hover(self.Genre_Playlist)
        # time.sleep(3)
        # self.Click_Back()
        # self.Click_Back()

        self.Hover(self.Mood_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Decades_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Khaleeji_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Gaming_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Latin_Genre , "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()
        self.Hover(self.Afro_Genre, "link")
        time.sleep(3)
        self.Click_Back()

        self.Hover(self.Kpop_Genre, "link")
        time.sleep(1.5)
        self.Click_Back()
        #
        # self.Hover(self.Tastemakers_Genre, "link")
        # time.sleep(1)
        # self.WaitForElement(self.Genre_Playlist, "xpath")
        # self.Hover(self.Genre_Playlist)
        # time.sleep(3)
        # self.Click_Back()
        # self.Click_Back()
        #
        # self.Hover(self.Wellness_Genre, "link")
        # time.sleep(1)
        # self.WaitForElement(self.Genre_Playlist, "xpath")
        # self.Hover(self.Genre_Playlist)
        # time.sleep(3)
        # self.Click_Back()
        # self.Click_Back()

        self.Hover(self.Chill_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Workout_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Focus_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Party_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Rock_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Sleep_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Cooking_Dining_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Jazz_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.R_B_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.TV_Movies_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Romance_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Indie_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Soul_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Classical_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Metal_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Kids_Family_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Reggae_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Blues_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Funk_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Punk_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Country_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Folk_Acoustic_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Comedy_Genre, "link")
        time.sleep(3)
        self.Click_Back()

        self.Hover(self.Travel_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()

        self.Hover(self.Summer_Genre, "link")
        time.sleep(1)
        self.WaitForElement(self.Genre_Playlist, "xpath")
        self.Hover(self.Genre_Playlist)
        time.sleep(3)
        self.Click_Back()
        self.Click_Back()
        time.sleep(5)



