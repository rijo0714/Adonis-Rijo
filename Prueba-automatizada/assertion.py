import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        chrome = Service(r"C:\Users\DELL E7240\Desktop\Prueba-automatizada-main\chromedriver.exe")

        self.driver = webdriver.Chrome(service= chrome)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))
        
    def tearDown(self) -> None:
        self.driver.quit()
    
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException():
            return False
        return True

if __name__ == "__main__":
    unittest.main(verbosity= 2)
