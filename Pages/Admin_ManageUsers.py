import datetime
import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Constants.URLS import TestData


class AdminAddUsers():

    def __init__(self, driver):
        self.driver = driver
        self.USERACCESSCONTROL = "//p[normalize-space()='User Access Control']"
        self.LEFTSIDENAVMENU = "//div[@class='side-navigation-menu-container half-content']"
        self.MANAGEUSERS = "//p[normalize-space()='Manage Users']"
        self.ADDBUTTON = "//span[normalize-space()='Add +']"
        self.FIRSTNAME = "firstName"
        self.LASTNAME = "lastName"
        self.ADDUSER_USERNAME = "username"
        self.PHONE = "phone"
        self.EMAIL = "email"
        self.ADDUSER_PASSWORD = "//input[@placeholder=' Enter your Password']"
        self.ADDUSER_CONFPASSWORD = "//input[@placeholder=' Enter Confirm Password']"
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
        self.MBAPPEEMAIL = "//span[normalize-space()='ninja@yopmail.com']"
        self.ATU = "//span[normalize-space()='atu@yopmail.com']"
        self.NORECORDFOUND = "//div[@class='title-heading-3']"
        self.CLEARFILTERBUTTON = "//span[normalize-space()='Clear Filter']"

        # Filter Elements
        self.FILTERICON = "//i[@class='pi pi-filter']"
        self.USERSTATUSEDD = "//*[contains(@class,'p-dropdown-trigger-icon ng-tns')]"  # Dynamic XPATH
        self.SELECTACTIVE = "//span[normalize-space()='Active']"
        self.SELECTINACTIVE = "//span[normalize-space()='Inactive']"
        self.TEAMSEARCHBAR = "//*[contains(@class,'p-dropdown-filter p-inputtext p-component ng-tns')]"  # Dynamic XPATH
        self.ENTERTEAMNAME = "//span[normalize-space()='test']"
        self.APPLYBUTTON = "//button[normalize-space()='Apply']"
        self.MERCHANTACTIONBUTTON = "//div[@class='grid']//div[1]//p-card[1]//div[1]//div[1]//div[1]//div[1]//button[1]"

        self.EDITBUTTON = "//a[normalize-space()='Edit']"

    def click_on_leftnavmanu(self):
        leftnav = self.driver.find_element(By.XPATH, self.LEFTSIDENAVMENU)
        self.driver.execute_script("arguments[0].click()", leftnav)

    def check_user_exist(self, text):
        user_exist = self.driver.find_element(By.XPATH, self.MANAGEUSERSSEARCHBAR)
        self.driver.execute_script("arguments[0].click()", user_exist)
        self.driver.find_element(By.XPATH, self.MANAGEUSERSSEARCHBAR).send_keys(text)
        time.sleep(2)

    def verify_user(self):
        un = self.driver.find_element(By.XPATH, self.MBAPPEEMAIL)
        if un.text == "ninja@yopmail.com":
            print("Pass > Checking Add User Flow: Newly Created User Found")
        else:
            print("Fail > Checking Add User Flow: Newly Created User Not Found Through Search")

    def click_on_addbutton(self):
        element = self.driver.find_element(By.XPATH, self.ADDBUTTON)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(2)

    def adduserdetails(self, Fname, Lname, AdminUname, PhnNum, Email, Pass, Cpass):
        self.driver.find_element(By.ID, self.FIRSTNAME).send_keys(Fname)
        self.driver.find_element(By.ID, self.LASTNAME).send_keys(Lname)
        self.driver.find_element(By.ID, self.ADDUSER_USERNAME).clear()
        self.driver.find_element(By.ID, self.ADDUSER_USERNAME).send_keys(AdminUname)
        global Phone
        Phone = PhnNum
        self.driver.find_element(By.ID, self.PHONE).send_keys(PhnNum)
        self.driver.find_element(By.ID, self.EMAIL).send_keys(Email)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.ADDUSER_PASSWORD).send_keys(Pass)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.ADDUSER_CONFPASSWORD).send_keys(Cpass + Keys.TAB)

        time.sleep(2)

    def click_on_teamsdd(self):
        self.driver.find_element(By.XPATH, self.TEAMSDD).click()

    def enter_team_name(self, Teamname):
        self.driver.find_element(By.XPATH, self.TEAMSTYPEAREA).send_keys(Teamname)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.SELECTEDTEAMCHECKBOX).click()
        # self.driver.find_element(By.XPATH,self.SELECTTEST2TEAMCHECKBOX).click()

    def selectusertype(self):
        element = self.driver.find_element(By.XPATH, self.USERTYPEDD)
        self.driver.execute_script("arguments[0].click()", element)
        element = self.driver.find_element(By.XPATH, self.SUPERADMIN)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(2)

    def selectuserstatus(self):
        element = self.driver.find_element(By.XPATH, self.STATUS_ACTIVE)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(1)

    def click_on_savebutton(self):
        element = self.driver.find_element(By.XPATH, self.SAVEBUTTON)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(4)

    def hoverleftnavmenu(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.LEFTSIDENAVMENU)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.XPATH, self.USERACCESSCONTROL)
        self.driver.execute_script("arguments[0].click()", element)
        element = self.driver.find_element(By.XPATH, self.MANAGEUSERS)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(2)

    def gotodashboard(self):
        self.driver.get(TestData.CUSTOMERMANAGEMENT)

    def verify_no_record_found(self):
        nrf = self.driver.find_element(By.XPATH, self.NORECORDFOUND)
        if nrf.text == "No Record Found":
            time.sleep(1)
        else:
            time.sleep(1)

    def verify_users_found(self):
        nrf = self.driver.find_element(By.XPATH, self.NORECORDFOUND)
        if nrf.text == "No Record Found":
            time.sleep(1)
        else:
            time.sleep(1)

    def click_clearfilter_button(self):
        element = self.driver.find_element(By.XPATH, self.CLEARFILTERBUTTON)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(3)

    def click_on_filtericon(self):
        element = self.driver.find_element(By.XPATH, self.FILTERICON)
        self.driver.execute_script("arguments[0].click()", element)

    def select_user_status_active(self):
        usdd = self.driver.find_elements(By.XPATH, self.USERSTATUSEDD)
        var = usdd[0]
        var.click()
        time.sleep(1)
        element = self.driver.find_element(By.XPATH, self.SELECTACTIVE)
        self.driver.execute_script("arguments[0].click()", element)

    def select_filterby_team(self, test):
        usdd = self.driver.find_elements(By.XPATH, self.USERSTATUSEDD)
        var = usdd[1]
        self.driver.execute_script("arguments[0].click()", var)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.TEAMSEARCHBAR).send_keys(test)
        element = self.driver.find_element(By.XPATH, self.ENTERTEAMNAME)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(1)

    def click_on_apply_button(self):
        element = self.driver.find_element(By.XPATH, self.APPLYBUTTON)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(1)

    def filter_results(self):
        global un
        un = self.driver.find_element(By.XPATH, self.ATU)
        if un.text == "atu@yopmail.com":
            print("Pass > Checking Filter Results: User Found Filters Working Fine")
        else:
            print("Fail > Checking Filter Results: User Not Found, Filters Not Working")

    def make_user_inactive(self, user):
        self.driver.find_element(By.XPATH, self.MANAGEUSERSSEARCHBAR).click()
        self.driver.find_element(By.XPATH, self.MANAGEUSERSSEARCHBAR).send_keys(user)
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, self.MERCHANTACTIONBUTTON)
        self.driver.execute_script("arguments[0].click()", element)
        element = self.driver.find_element(By.XPATH, self.EDITBUTTON)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(2)
        element = self.driver.find_element(By.XPATH, self.STATUS_INACTIVE)
        self.driver.execute_script("arguments[0].click()", element)
        element = self.driver.find_element(By.XPATH, self.SAVEBUTTON)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(2)
        element = self.driver.find_element(By.XPATH, self.CLEARFILTERBUTTON)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(2)

    def select_user_status_Inactive(self):
        usdd = self.driver.find_elements(By.XPATH, self.USERSTATUSEDD)
        time.sleep(3)
        var = usdd[0]
        var.click()
        time.sleep(1)
        element = self.driver.find_element(By.XPATH, self.SELECTINACTIVE)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(3)
