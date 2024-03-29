from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
from PageObjects.homepage import HomePage
class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(38)
        self.base_url = "https://www.youtube.com/"
    def testd_google_search(self):
        driver = self.driver
        driver.get(self.base_url)
        homepage = HomePage(driver)
        homepage.enter_search_text("An")
        homepage.press_return_key_search_field()
        time.sleep(2)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()