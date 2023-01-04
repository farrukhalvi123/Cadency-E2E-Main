import datetime
import os
import time
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Elements.Admin_LoginScreenElements import AdminportalElements
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Constants.URLS import TestData


class AdminAddUsers(AdminportalElements):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_leftnavmanu(self):
        self.click_using_js(self.LEFTSIDENAVMENU)

    def check_user_exist(self, text):
        self.click_using_js(self.MANAGEUSERSSEARCHBAR)
        self.input_element(self.MANAGEUSERSSEARCHBAR, text)
        time.sleep(1)

    def verify_user(self):
        un = self.get_element_text(self.MBAPPEXPATH)
        print(un)
        if un == "Kylian Mbappe":
            print("User Exist")
        else:
            print("")

    def click_on_addbutton(self):
        self.click_using_js(self.ADDBUTTON)

    def adduserdetails(self, Fname, Lname, AdminUname, PhnNum, Email, Pass, Cpass):
        self.input_element(self.FIRSTNAME, Fname)
        self.input_element(self.LASTNAME, Lname)
        self.input_element(self.ADDUSER_USERNAME, AdminUname)
        global Phone
        Phone = PhnNum
        self.input_element(self.PHONE, PhnNum)
        self.input_element(self.EMAIL, Email)
        self.input_element(self.ADDUSER_PASSWORD, Pass)
        self.input_element(self.ADDUSER_CONFPASSWORD, Cpass + Keys.TAB)
        time.sleep(2)

    def click_on_teamsdd(self):
        self.click_element(self.TEAMSDD)

    def enter_team_name(self, Teamname):
        self.input_element(self.TEAMSTYPEAREA, Teamname)
        time.sleep(2)
        self.click_element(self.SELECTEDTEAMCHECKBOX)

    def selectusertype(self):
        self.click_using_js(self.USERTYPEDD)
        self.click_using_js(self.SUPERADMIN)
        time.sleep(2)

    def selectuserstatus(self):
        self.click_using_js(self.STATUS_ACTIVE)
        time.sleep(1)

    def click_on_savebutton(self):
        self.click_using_js(self.SAVEBUTTON)
        time.sleep(2)

    def hoverleftnavmenu(self):
        self.move_to_element(self.LEFTSIDENAVMENU)
        self.wait(1)
        self.click_using_js(self.USERACCESSCONTROL)
        self.click_using_js(self.MANAGEUSERS)
        time.sleep(2)

    def gotodashboard(self):
        self.driver.get(TestData.CUSTOMERMANAGEMENT)

    def verify_no_record_found(self):
        nrf = self.get_element_text(self.NORECORDFOUND)
        if nrf == "No Record Found":
            print(nrf)
            time.sleep(1)
        else:
            print("Some Record Found Test Case Failed")

    def click_clearfilter_button(self):
        self.click_using_js(self.CLEARFILTERBUTTON)
        time.sleep(3)

    def click_on_filtericon(self):
        self.click_using_js(self.FILTERICON)

    def select_user_status(self):
        usdd = self.driver.find_elements(By.XPATH, self.USERSTATUSEDD)
        var = usdd[0]
        var.click()
        time.sleep(1)
        self.click_using_js(self.SELECTACTIVE)

    def select_filterby_team(self, test):
        usdd = self.driver.find_elements(By.XPATH, self.USERSTATUSEDD)
        var = usdd[1]
        var.click()
        time.sleep(1)
        self.input_element(self.TEAMSEARCHBAR, test)
        self.click_using_js(self.ENTERTEAMNAME)
        time.sleep(2)

    def click_on_apply_button(self):
        self.click_using_js(self.APPLYBUTTON)

    def filter_results(self):
        self.click_using_js(self.APPLYBUTTON)
