import datetime
import os
import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Elements.Admin_LoginScreenElements import AdminportalElements
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Constants.URLS import TestData


class AdminLoginPage(AdminportalElements):

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_admin(self):
        self.driver.get(TestData.CADENCY_MANAGEMENT)

    def enter_adusername(self, un):
        try:
            self.input_element(self.USERNAME, un)
        except Exception as e:
            attach(str("username field is not displayed"), name=str("Not Displayed"),
                   attachment_type=AttachmentType.TEXT)

    def enter_adpassword(self, pwd):
        try:
            self.input_element(self.PASSWORD, pwd)
        except Exception as e:
            attach(str("username field is not displayed"), name=str("Not Displayed"),
                   attachment_type=AttachmentType.TEXT)
        time.sleep(5)

    def click_loginbutton(self):
        self.click_using_js(self.LOGINBUTTON)
        time.sleep(2)

    def click_profpic(self):
        self.click_using_js(self.PROFILEPICCLICK)

    def click_Adminlogout(self):
        self.click_using_js(self.LOGOUTBUTTON)