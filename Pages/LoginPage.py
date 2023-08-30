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


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.emailfield = "EmailID"
        self.password = "EmailPassword"
        self.loginbtn = "//button[@type='submit']"
        self.homepage_logo = "//img[@class='svg-icon svg-logo']"
        self.HomePage = "//span[@class='breadcrumb-title']"
        self.HomePage_sidenavbar = "//div[@class='side-navigation-menu-container half-content']"
        self.login_successful_popup = "toast-container"
        self.login_unsuccessful_popup = "//*[@id='toast-container']/div/div[1]"
        self.PROFILETHUMBNAIL = "//p-avatar[@class='p-element avatar-square-54']//div[@class='p-avatar p-component']"
        self.LOGOUT = "//span[normalize-space()='Logout']"
        self.FORGETPASS = "//a[normalize-space()='Forgot Password?']"
        self.EMAILFIELD = "Email"
        self.CLICKSEND = "//button[@type='button']"
        self.CODEID = "token"

    def go_to_main(self):
        self.driver.get(TestData.STAGING_MAIN)

    def verify_hompage(self):
        assert self.homepage_logo in self.driver.page_source

    def enter_username(self, mail):
        try:
            self.driver.find_element(By.ID,self.emailfield).send_keys(mail)
        except Exception as e:
            attach(str("username field is not displayed"), name=str("Not Displayed"),
                   attachment_type=AttachmentType.TEXT)

    def enter_password(self, pwd):
        try:
            self.driver.find_element(By.ID,self.password).send_keys(pwd)
        except Exception as e:
            attach(str("username field is not displayed"), name=str("Not Displayed"),
                   attachment_type=AttachmentType.TEXT)

    def click_login(self):
        try:
            logbtn = self.driver.find_element(By.XPATH,self.loginbtn)
            self.driver.execute_script("arguments[0].click()",logbtn)
        except Exception as e:
            attach(str("username field is not displayed"), name=str("Not Displayed"),
                   attachment_type=AttachmentType.TEXT)

    def verify_postloginhomepage(self):
        try:
            self.driver.implicitly_wait(5)
            self.popup_text = self.driver.find_element(By.ID,self.login_successful_popup)
            if self.popup_text.text == "User login successfully.":
                assert self.popup_text.text == "User login successfully."
            elif self.popup_text.text == " Invalid Email Or Password,Please try again ":
                assert self.popup_text.text == " Invalid Email Or Password,Please try again "
        except:
            print(self.popup_text.text)
            return self.popup_text.text

    def click_profilethumbnail(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.PROFILETHUMBNAIL)))
        # element = self.driver.find_element(By.XPATH,self.PROFILETHUMBNAIL)
        self.driver.execute_script("arguments[0].click()", element)

    def click_logout(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.LOGOUT)))
        self.driver.execute_script("arguments[0].click()", element)

    def click_forgetpass(self):
        element = self.driver.find_element(By.XPATH,self.FORGETPASS)
        self.driver.execute_script("arguments[0].click()", element)
    def enter_email(self, mail):
        self.driver.find_element(By.ID,self.EMAILFIELD).send_keys(mail)

    def click_send(self):
        self.driver.find_element(By.XPATH,self.CLICKSEND)

    def enter_code(self, code):
        self.driver.find_element(By.ID, self.CODEID).send_keys(code)

    def close_browser(self):
        self.driver.close()
