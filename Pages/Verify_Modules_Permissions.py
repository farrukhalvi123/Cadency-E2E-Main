import datetime
import os
import time
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Constants.URLS import TestData
from Elements.Verify_Modules_Permissions import VerifyPermissionsElements


class VerifyPermissions(VerifyPermissionsElements):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_addusername(self, NinjaTurtle):
        self.input_element(self.USERNAME, NinjaTurtle)

    def enter_adpassword(self, Talha123):
        self.input_element(self.PASSWORD, Talha123)

    def click_loginbutton(self):
        self.click_using_js(self.LOGINBUTTON)
        time.sleep(4)

    def open_left_panel(self):
        self.move_to_element(self.LEFTSIDENAVMENU)
        self.wait(1)

    def click_on_dashboard(self):
        self.click_using_js(self.DASHBOARD)
        dbtext = self.get_element_text(self.DASHBOARD)
        if dbtext == "Dashboard":
            print("PASS > Dashboard Option Found")

    def click_on_onboardmerchants(self):
        self.click_using_js(self.DASHBOARD)
        dbtext = self.get_element_text(self.ONBOARDMERCHANT)
        if dbtext == "Onboard Merchants":
            print("PASS > Onboard Merchants Option Found")

    def click_on_actlogs(self):
        self.click_using_js(self.ACTIVITYLOGS)
        dbtext = self.get_element_text(self.ACTIVITYLOGS)
        if dbtext == "Activity Logs":
            print("PASS > Activity Logs Option Found")

    def click_on_uac(self):
        self.click_using_js(self.USERACCESSCONTROL)
        dbtext = self.get_element_text(self.USERACCESSCONTROL)
        if dbtext == "User Access Control":
            print("FAIL > User Access Control Option Found")

    def click_on_pi(self):
        self.click_using_js(self.PAYMENTINTEGRATION)
        dbtext = self.get_element_text(self.PAYMENTINTEGRATION)
        if dbtext == "Payment Integration":
            print("FAIL > Payment Integration Option Found")

    def click_on_obmtile(self):
        # self.click_using_js(self.ONBOARDMERCHANTTILE)
        dbtext = self.get_element_text(self.ONBOARDMERCHANTTILE)
        if dbtext == "Onboarded Merchants":
            print("PASS > Onboarded Merchants Tile Found")

    def click_on_pmtile(self):
        # self.click_using_js(self.PENDINGMERCHANTTILE)
        dbtext = self.get_element_text(self.PENDINGMERCHANTTILE)
        if dbtext == "Pending Merchants":
            print("PASS > Pending Merchants Tile Found")

    def click_on_tutile(self):
        # self.click_using_js(self.TOTALUSERSTILE)
        dbtext = self.get_element_text(self.TOTALUSERSTILE)
        if dbtext == "Total Users":
            print("FAIL > Total Users Tile Found")

    def click_on_tttile(self):
        # self.click_using_js(self.TOTALTEAMTILE)
        dbtext = self.get_element_text(self.TOTALTEAMTILE)
        if dbtext == "Total Teams":
            print("FAIL > Total Teams Tile Found")

    def click_on_mstile(self):
        # self.click_using_js(self.MERCHANTSUMMARYTILE)
        dbtext = self.get_element_text(self.MERCHANTSUMMARYTILE)
        if dbtext == "Merchant Summary":
            print("PASS > Merchant Summary Tile Found")

    def click_on_matile(self):
        # self.click_using_js(self.MYACTIVITIESTILE)
        dbtext = self.get_element_text(self.MYACTIVITIESTILE)
        if dbtext == "My Activities":
            print("PASS > My Activities Tile Found")

    def click_on_mbctile(self):
        # self.click_using_js(self.MYACTIVITIESTILE)
        dbtext = self.get_element_text(self.MERCHANTCOUNTRIESTILE)
        if dbtext == "Merchants By Country":
            print("PASS > Merchants By Country Tile Found")

    def click_on_mttile(self):
        # self.click_using_js(self.MYACTIVITIESTILE)
        dbtext = self.get_element_text(self.MYTASKTILE)
        if dbtext == "My Task":
            print("PASS > My Task Tile Found")

    def verifying_edit_option(self):
        self.click_using_js(self.ONBOARDMERCHANTTILE)
        self.click_using_js(self.MERCHANTACTIONBUTTON)
        dbtext = self.get_element_text(self.EDITBUTTON)
        if dbtext == "Edit":
            print("FAIL > Edit Button Found")

    def verifying_Labels(self):
        self.click_using_js(self.ACTIVITYLOGS)
        dbtext = self.get_element_text(self.LEVELS)
        if dbtext == "Levels":
            print("PASS > Levels Label Found")
        else:
            print("FAIL > Levels Label Not Found")

        dbtext = self.get_element_text(self.MODULE)
        if dbtext == "Module":
            print("PASS > Module Label Found")
        else:
            print("FAIL > Module Label Not Found")

        dbtext = self.get_element_text(self.DESC)
        if dbtext == "Description":
            print("PASS > Description Label Found")
        else:
            print("FAIL > Description Label Not Found")

        dbtext = self.get_element_text(self.IPADD)
        if dbtext == "IP Addess":
            print("PASS > IP Address Label Found")
        else:
            print("FAIL > IP Address Label Not Found")

        dbtext = self.get_element_text(self.LOGGEDBY)
        if dbtext == "Logged By":
            print("PASS > Logged By Label Found")
        else:
            print("FAIL > Logged By Label Not Found")

        dbtext = self.get_element_text(self.DATETIME)
        if dbtext == "Date & Time":
            print("PASS > Date & Time Label Found")
        else:
            print("FAIL > Date & Time Label Not Found")

    def verifying_Firstrow(self):
        self.click_using_js(self.CLICKONNAME)
        time.sleep(2)
        self.click_using_js(self.PROFSETTINGS)
        time.sleep(2)
        fn = self.get_element_text(self.FNAME)
        print(fn)
        # FirstName = self.driver.find_elements(By.CLASS_NAME, self.NAME)
        # fn = self.get_element_text(FirstName[1])
        # ln = self.get_element_text(FirstName[2])
        # print(FirstName[1].text)

        rowdata = self.get_element_text(self.INFO)
        if rowdata == "Info":
            print("PASS > Info Found")
        else:
            print("FAIL > Info Not Found")

        rowdata = self.get_element_text(self.USER)
        if rowdata == "User":
            print("PASS > Module = User, Found")
        else:
            print("FAIL > Module = User, Not Found")

        rowdata = self.get_element_text(self.USERLOGINSUCCESSFULLY)
        if rowdata == "User Login successfully":
            print("PASS > User Login successfully Found")
        else:
            print("FAIL > User Login successfully Not Found")
