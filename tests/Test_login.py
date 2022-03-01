import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
import time

#To add the path in system environment variable
sys.path.append("C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project")

#Importing locators from pageObjects Locators.py
from pageObjects.Locators import Locators

class LoginTest(unittest.TestCase):
    baseUrl = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"
    driver = webdriver.Chrome(executable_path="C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project//drivers//Chromedriver.exe")

    @classmethod
    def setUpClass(cls):
         cls.driver.get(cls.baseUrl)
         cls.driver.maximize_window()

    def test_login(self):
         lp = Locators(self.driver)  #created an object
         lp.setUsername(self.username)
         time.sleep(2)
         lp.setPassword(self.password)
         time.sleep(2)
         lp.clickLogin()
         time.sleep(2)
         lp.clickWelcome()
         time.sleep(2)
         lp.clickLogout()
         time.sleep(3)
         self.assertEqual("OrangeHRM",self.driver.title,"webpage title is not matching")

    @classmethod
    def tearDownClass(cls):
          cls.driver.close()
          print("Test Completed......")

if __name__ == "__main__":
    #This parameter is mandatory for generating Reports
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project//reports"))
