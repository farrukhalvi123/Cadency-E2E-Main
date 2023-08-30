import datetime
import os
import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from Elements.LoginElements import loginelements
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Constants.URLS import TestData



class CustomerPortalLogin():

    def __init__(self,driver):
        self.driver = driver
        self.username_tb = "//input[@placeholder='Enter Username']"
        self.password_tb =  " //input[@placeholder='Enter Password']"
        self.login_btn =  "//span[normalize-space()='Login']"
        self.right_topdropdown =  "//span[@class='p-button-label']"
        self.logout = "//a[normalize-space()='Logout']"

    def go_to_login(self):
        self.driver.get(TestData. STAGING_CUSTOMER)


    def enter_username1(self,uname4):
        try:
            self.driver.find_element(By.XPATH,self.username_tb).send_keys(uname4)
        except Exception as e:
            attach(str("username field is not displayed"), name=str("Not Displayed"),
                   attachment_type=AttachmentType.TEXT)
        time.sleep(1)

    def enter_password1(self,pw):
        try:
            self.driver.find_element(By.XPATH,self.password_tb).send_keys(pw)
        except Exception as e:
            attach(str("password field is not displayed"), name=str("Not Displayed"),
                  attachment_type=AttachmentType.TEXT)
        time.sleep(3)


    def login_button(self):
        clickbutton= self.driver.find_element(By.XPATH, self.login_btn)
        self.driver.execute_script("arguments[0].click()",clickbutton )
        time.sleep(5)

    def open_newtab(self):
        self.driver.execute_script("window.open();")
        self.driver.switch_to.window(self.driver.window_handles[1])