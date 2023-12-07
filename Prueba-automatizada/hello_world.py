#UN EJEMPLO SENCILLO PARA INICIARME EN LA AUTOMATIZACIÓN CON SELENIM

import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

class HolaMundo(unittest.TestCase):

    def setUp(self) -> None:
        chrome = Service(r"C:\Users\DELL E7240\Desktop\Prueba-automatizada-main\chromedriver.exe")

        self.driver = webdriver.Chrome(service= chrome)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()

    def test_search_text_field(self):
        search_field = self.driver.find_element("id", "search")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element("name", "q")

    def test_search_field_by_class_name(self):
        self_field = self.driver.find_element("class name", "input-text")

    def test_search_button_enabled(self):
        button = self.driver.find_element("class name", "button")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element("class name", "promos")
        banners = banner_list.find_elements("tag name", "img")
        self.assertEqual(3, len(banners))
    
    def test_vip_promo(self):
        vip_promo = self.driver.find_elements('xpath', '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[3]/a/img')

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_elements("css selector", "div.header-minicart span.icon")

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output= 'ejemploReport', report_name= 'registro-usuario'))
