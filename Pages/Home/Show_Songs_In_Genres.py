from Base.Selenium_Driver import SeleniumDriver
import time


class ShowSongs(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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
    Genre_Playlist = "/html/body/div[4]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[3]/section[1]/div/div[" \
                     "2]/div/div/div[4] "

    def click_pop(self):
        self.element_click(self.Pop_Genre, "link")

    def click_back(self):
        self.element_click(self.Back, "xpath")

    def click_on_search(self):
        self.element_click(self.Search_Button, "link")

    def show_songs_in_all_genres(self):
        time.sleep(2)
        self.click_on_search()
        time.sleep(2)
        self.hover(self.Pop_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Electronic_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Arabic_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Podcasts_Genre, "link")
        time.sleep(1)
        self.click_back()

        self.hover(self.Made_For_You_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Charts_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.New_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Discover_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.At_Home_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        # self.hover(self.Arabic_Genre, "link")
        # self.wait_for_element(self.Genre_Playlist, "xpath")
        # self.hover(self.Genre_Playlist)
        # time.sleep(3)
        # self.click_back()
        # self.click_back()

        self.hover(self.Mood_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Decades_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Khaleeji_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Gaming_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Latin_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()
        self.hover(self.Afro_Genre, "link")
        time.sleep(3)
        self.click_back()

        self.hover(self.Kpop_Genre, "link")
        time.sleep(1.5)
        self.click_back()
        #
        # self.hover(self.Tastemakers_Genre, "link")
        # time.sleep(1)
        # self.wait_for_element(self.Genre_Playlist, "xpath")
        # self.hover(self.Genre_Playlist)
        # time.sleep(3)
        # self.click_back()
        # self.click_back()
        #
        # self.hover(self.Wellness_Genre, "link")
        # time.sleep(1)
        # self.wait_for_element(self.Genre_Playlist, "xpath")
        # self.hover(self.Genre_Playlist)
        # time.sleep(3)
        # self.click_back()
        # self.click_back()

        self.hover(self.Chill_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Workout_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Focus_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Party_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Rock_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Sleep_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Cooking_Dining_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Jazz_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.R_B_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.TV_Movies_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Romance_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Indie_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Soul_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Classical_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Metal_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Kids_Family_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Reggae_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Blues_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Funk_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Punk_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Country_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Folk_Acoustic_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Comedy_Genre, "link")
        time.sleep(3)
        self.click_back()

        self.hover(self.Travel_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()

        self.hover(self.Summer_Genre, "link")
        time.sleep(1)
        self.wait_for_element(self.Genre_Playlist, "xpath")
        self.hover(self.Genre_Playlist)
        time.sleep(3)
        self.click_back()
        self.click_back()
        time.sleep(5)
