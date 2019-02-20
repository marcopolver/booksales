from selenium import webdriver
import unittest

#Test avvio server e titolo corretto
class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    #Test titolo homepage
    def test_home_page_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('BookSales UniBG', self.browser.title)

if(__name__ == '__main__'):
    unittest.main()