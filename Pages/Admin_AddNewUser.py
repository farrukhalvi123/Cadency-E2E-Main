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
        if un == "Kylian Mbappe":
            print("Pass > Checking Add User Flow: Newly Created User Found")
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
        self.click_element(self.SELECTTESTTEAMCHECKBOX)
        self.click_element(self.SELECTTEST2TEAMCHECKBOX)

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
            time.sleep(1)
        else:
            time.sleep(1)

    def verify_users_found(self):
        nrf = self.get_element_text(self.NORECORDFOUND)
        if nrf == "No Record Found":
            time.sleep(1)
        else:
            time.sleep(1)

    def click_clearfilter_button(self):
        self.click_using_js(self.CLEARFILTERBUTTON)
        time.sleep(3)

    def click_on_filtericon(self):
        self.click_using_js(self.FILTERICON)

    def select_user_status_active(self):
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
        time.sleep(1)

    def click_on_apply_button(self):
        self.click_using_js(self.APPLYBUTTON)
        time.sleep(1)

    def filter_results(self):
        global un
        un = self.get_element_text(self.MBAPPEXPATH)
        if un == "Kylian Mbappe":
            print("Pass > Checking Filter Results: User Found Filters Working Fine")
        else:
            print("")

    def make_user_inactive(self):
        self.click_element(self.MANAGEUSERSSEARCHBAR)
        time.sleep(3)
        self.input_element(self.MANAGEUSERSSEARCHBAR, "Kylian")
        self.click_using_js(self.ACTIONBUTTON)
        self.click_using_js(self.EDITBUTTON)
        time.sleep(2)
        self.click_using_js(self.STATUS_INACTIVE)
        self.click_using_js(self.SAVEBUTTON)
        time.sleep(2)
        self.click_using_js(self.CLEARFILTERBUTTON)
        time.sleep(2)

    def select_user_status_Inactive(self):
        usdd = self.driver.find_elements(By.XPATH, self.USERSTATUSEDD)
        time.sleep(3)
        var = usdd[0]
        var.click()
        time.sleep(1)
        self.click_using_js(self.SELECTINACTIVE)
        time.sleep(3)
