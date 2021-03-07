from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SampleProject.POMDemo.Pages.LoginPage import LoginPage
from SampleProject.POMDemo.Pages.HomePage import HomePage
#import HTMLTestRunner


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Marwa/PycharmProjects/Selenium/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_login_valid(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login=LoginPage(driver)

        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage=HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")
#if __name__=='__main__':
   #  unittest.main(testRunner=HTMLTestRunner.HtmlTestRunner(outout="C:/Users/Marwa/PycharmProjects/Selenium/Report"))
