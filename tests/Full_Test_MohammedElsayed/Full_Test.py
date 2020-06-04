import unittest
from web.tests.Library_test.Library_test import TestLibrary
from web.tests.Add_Remove_Songs_playlists_test.Add_Remove_Songs_playlists_test import TestAddRemove
from web.tests.Play_Pause_test.Play_Pause_test import TestPlayPause
from web.tests.Search_test.Search_test import TestSearch

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLibrary)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestAddRemove)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestPlayPause)
tc4 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)

# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4])
unittest.TextTestRunner(verbosity=2).run(smokeTest)
