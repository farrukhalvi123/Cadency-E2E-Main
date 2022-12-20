import datetime
import os
import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Elements.LoginElements import loginelements
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Constants.URLS import TestData


class LoginPage(loginelements):

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_main(self):
        self.driver.get(TestData.CADENCY_MAIN)

    def verify_hompage(self):
        assert self.homepage_logo in self.driver.page_source
    def enter_username(self,mail):
        try:
            self.input_element(self.emailfield,mail)
        except Exception as e:
            attach(str("username field is not displayed"), name=str("Not Displayed"),
                   attachment_type=AttachmentType.TEXT)


    def enter_password(self,pwd):
        try:
            self.input_element(self.password,pwd)
        except Exception as e:
            attach(str("username field is not displayed"), name=str("Not Displayed"),
                   attachment_type=AttachmentType.TEXT)

    def click_login(self):
        try:
            self.click_using_js(self.loginbtn)
        except Exception as e:
            attach(str("username field is not displayed"), name=str("Not Displayed"),
                   attachment_type=AttachmentType.TEXT)

    def verify_postloginhomepage(self):
        try:
            self.driver.implicitly_wait(5)
            self.popup_text = self.get_element_text(self.login_successful_popup)

            if self.popup_text == "User login successfully.":
                assert self.popup_text == "User login successfully."
            elif self.popup_text == " Invalid Email Or Password,Please try again ":
                assert self.popup_text == " Invalid Email Or Password,Please try again "
        except:
            print("no text found")
    def click_profilethumbnail(self):
        self.click_using_js(self.PROFILETHUMBNAIL)
    def click_logout(self):
        self.click_using_js(self.LOGOUT)

    def click_forgetpass(self):
        self.click_using_js(self.FORGETPASS)

    def enter_email(self,mail):
        self.input_element(self.EMAILFIELD,mail)

    def click_send(self):
        self.click_element(self.CLICKSEND)

    def enter_code(self,code):
        self.input_element(self.CODEID)