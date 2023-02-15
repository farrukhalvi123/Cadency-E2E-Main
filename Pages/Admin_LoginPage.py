import datetime
import os
import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# from Elements.Admin_LoginScreenElements import AdminportalElements
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Constants.URLS import TestData


class AdminLoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.USERNAME = "login-email"
        self.PASSWORD = "//input[@placeholder='Enter Password']"
        self.LOGINBUTTON = "//button[@type='submit']"
        self.PROFILEPICCLICK = "//span[@class='p-button-link ml-2 font-semibold flex align-items-center']"
        self.LOGOUTBUTTON = "//a[normalize-space()='Logout']"
        self.FORGOT_PASSWORD = "//span[normalize-space()='Forgot Password?']"

        # General Elements
        self.LEFTSIDENAVMENU = "//div[@class='side-navigation-menu-container half-content']"

        # Add New User
        self.USERACCESSCONTROL = "//p[normalize-space()='User Access Control']"
        self.MANAGEUSERS = "//p[normalize-space()='Manage Users']"
        self.ADDBUTTON = "//span[normalize-space()='Add +']"
        self.FIRSTNAME = "firstName"
        self.LASTNAME = "lastName"
        self.ADDUSER_USERNAME = "username"
        self.PHONE = "phone"
        self.EMAIL = "email"
        self.ADDUSER_PASSWORD = "//input[@placeholder=' Enter your Password']"
        self.ADDUSER_CONFPASSWORD = "//input[@placeholder=' Enter your Confirm Password']"
        self.TEAMSDD = "//*[contains(@class,'p-multiselect-label ng-tns')]"  # Dynamic XPATH
        self.TEAMSTYPEAREA = "//input[@role='textbox']"
        self.SELECTEDTEAMCHECKBOX = "//span[normalize-space()='test']"
        self.USERTYPEDD = "//*[contains(@class,'p-dropdown-trigger-icon ng-tns')]"  # Dynamic XPATH
        self.SUPERADMIN = "//span[normalize-space()='Super Admin']"
        self.STANDARD = "//span[normalize-space()='Standard']"
        self.STATUS_ACTIVE = "//span[normalize-space()='Active']"
        self.STATUS_INACTIVE = "//span[normalize-space()='Inactive']"
        self.SAVEBUTTON = "//span[normalize-space()='Save']"

        # Users Listing Page Elements
        self.MANAGEUSERSSEARCHBAR = "//input[@id='searchText']"
        self.MBAPPEXPATH = "//h3[normalize-space()='Kylian Mbappe']"
        self.NORECORDFOUND = "//div[@class='title-heading-3']"
        self.CLEARFILTERBUTTON = "//span[normalize-space()='Clear Filter']"

        # Filter Elements
        self.FILTERICON = "//i[@class='pi pi-filter']"
        self.USERSTATUSEDD = "//*[contains(@class,'p-dropdown-trigger-icon ng-tns')]"  # Dynamic XPATH
        self.SELECTACTIVE = "//span[normalize-space()='Active']"
        self.TEAMSEARCHBAR = "//*[contains(@class,'p-dropdown-filter p-inputtext p-component ng-tns')]"  # Dynamic XPATH
        self.ENTERTEAMNAME = "//span[normalize-space()='test']"
        self.APPLYBUTTON = "//button[normalize-space()='Apply']"

    def go_to_admin(self):
        self.driver.get(TestData.CADENCY_MANAGEMENT)

    def enter_adusername(self, un):
        try:
            time.sleep(2)
            self.driver.find_element(By.ID,self.USERNAME).send_keys(un)
        except Exception as e:
            attach(str("username field is not displayed"), name=str("Not Displayed"),
                   attachment_type=AttachmentType.TEXT)

    def enter_adpassword(self, pwd):
        try:
            self.driver.find_element(By.XPATH,self.PASSWORD).send_keys(pwd)
        except Exception as e:
            attach(str("username field is not displayed"), name=str("Not Displayed"),
                   attachment_type=AttachmentType.TEXT)
        time.sleep(5)

    def click_loginbutton(self):
        logbtn = self.driver.find_element(By.XPATH,self.LOGINBUTTON)
        self.driver.execute_script("arguments[0].click()",logbtn)
        time.sleep(2)

    def click_profpic(self):
        profpic = self.driver.find_element(By.XPATH,self.PROFILEPICCLICK)
        self.driver.execute_script("arguments[0].click()", profpic)

    def click_Adminlogout(self):
        logout = self.driver.find_element(By.XPATH,self.LOGOUTBUTTON)
        self.driver.execute_script("arguments[0].click()",logout)