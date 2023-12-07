import time
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class RegisterNewUser(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        chrome = Service(r"C:\Users\DELL E7240\Desktop\Prueba-automatizada-main\chromedriver.exe")

        self.driver = webdriver.Chrome(service= chrome)
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver = self.driver

        driver.find_element('xpath', '//*[@id="header"]/div/div[2]/div/a').click()
        driver.save_screenshot("captures/desplegable.png")

        driver.find_element('xpath', '//*[@id="header-account"]/div/ul/li[6]/a').click()
        driver.save_screenshot("captures/myaccount.png")

        create_account_button = driver.find_element('xpath', '/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        driver.save_screenshot("captures/login.png")
        
        self.assertEqual('Create New Customer Account', driver.title)

        #Insertar datos en campos
        first_name = driver.find_element('id', 'firstname')
        middle_name = driver.find_element('id', 'middlename')
        last_name = driver.find_element('id', 'lastname')
        email_address = driver.find_element('id', 'email_address')
        news_letter_subscription = driver.find_element('id', 'is_subscribed')
        password = driver.find_element('id', 'password')
        confirm_password = driver.find_element('id', 'confirmation')
        submit_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button')

        #Comprobar que cada campo esté habilitado
        self.assertTrue(first_name.is_enabled() 
        and middle_name.is_enabled() 
        and last_name.is_enabled() 
        and email_address.is_enabled() 
        and news_letter_subscription.is_enabled() 
        and password.is_enabled() 
        and confirm_password.is_enabled() 
        and submit_button.is_enabled())

        #Enviar datos de prueba a esos campos del formulario
        first_name.send_keys('Adonis')
        time.sleep(1)
        middle_name.send_keys('Test')
        time.sleep(1)
        last_name.send_keys('Rijo')
        time.sleep(1)
        email_address.send_keys('Testadonis@itla.edu.do')
        time.sleep(1)
        news_letter_subscription.send_keys('Test')
        time.sleep(1)
        password.send_keys('Test123')
        time.sleep(1)
        confirm_password.send_keys('Test123')
        time.sleep(1)
        submit_button.click()
        time.sleep(1)

    def tearDown(self) -> None:
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output= 'reportRegister', report_name= 'registro-usuario'))
