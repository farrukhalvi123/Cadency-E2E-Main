import datetime
import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Constants.URLS import TestData


class VerifyPermissions():

    def __init__(self, driver):
        self.driver = driver
        self.USERNAME = "login-email"
        self.PASSWORD = "//input[@placeholder='Enter Password']"
        self.LOGINBUTTON = "//button[@type='submit']"
        self.LEFTSIDENAVMENU = "//div[@class='side-navigation-menu-container half-content']"
        self.DASHBOARD = "//p[normalize-space()='Dashboard']"
        self.USERACCESSCONTROL = "//p[normalize-space()='User Access Control']"
        self.PAYMENTINTEGRATION = "//p[normalize-space()='Payment Integrations']"
        self.ONBOARDMERCHANT = "//p[normalize-space()='Onboard Merchants']"
        self.ACTIVITYLOGS = "//p[normalize-space()='Activity Logs']"

        # Verifying Available Dashboard Options
        self.ONBOARDMERCHANTTILE = "//h3[normalize-space()='Onboarded Merchants']"
        self.PENDINGMERCHANTTILE = "//h3[normalize-space()='Pending Merchants']"
        self.TOTALUSERSTILE = "//h3[normalize-space()='Total Users']"
        self.TOTALTEAMTILE = "//h3[normalize-space()='Total Teams']"
        self.MERCHANTSUMMARYTILE = "//h3[normalize-space()='Merchant Summary']"
        self.MYACTIVITIESTILE = "//h3[normalize-space()='My Activities']"
        self.MERCHANTCOUNTRIESTILE = "//h3[normalize-space()='Merchants By Country']"
        self.MYTASKTILE = "//h3[normalize-space()='My Task']"

        # Verifying Edit Option in Merchants

        self.MERCHANTACTIONBUTTON = "//body[1]/app-root[1]/app-features[1]/div[1]/div[1]/div[1]/app-entity-list[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[6]/div[1]/button[1]/i[1]"
        self.EDITBUTTON = "//a[normalize-space()='Edit']"

        # Verifying Activity Logs (Labels)

        self.LEVELS = "//div[normalize-space()='Levels']"
        self.MODULE = "//div[@class='col-2 font-semibold flex justify-content-none lg:justify-content-center white-space-nowrap']"
        self.DESC = "//div[@class='col-4 font-semibold white-space-nowrap']"
        self.IPADD = "//div[normalize-space()='IP Addess']"
        self.LOGGEDBY = "//div[@class='col-2 font-semibold white-space-nowrap']"
        self.DATETIME = "//div[normalize-space()='Date & Time']"

        # Goto Profile
        self.CLICKONNAME = "//i[@class='pi pi-chevron-down ml-1']"
        self.PROFSETTINGS = "//a[normalize-space()='Profile Settings']"
        self.FNAME = "//input[@id='firstName']"
        self.LNAME = "//input[@id='firstName']"

        # Verifying Activity Logs (1st Row Data)

        self.INFO = "//body/app-root/app-features[@class='ng-star-inserted']/div[@class='feature-container']/div[@class='main-body-content']/div[@class='page-content']/app-activity-logs-list[@class='ng-star-inserted']/div[@class='container-wrapper']/div/div/div[2]/div[1]/div[1]/span[1]"
        self.USER = "status-container module-status status-blue3"
        self.USERLOGINSUCCESSFULLY = "custom-twolines-ellipsis"
        self.IP = "font-semibold lg:hidden"
        self.LOGINSUER = "loggedby-text"

    def  open_left_panel(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.LEFTSIDENAVMENU)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

    def click_on_dashboard(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.DASHBOARD)))
        self.driver.execute_script("arguments[0].click()", element)
        dbtext = self.driver.find_element(By.XPATH, self.DASHBOARD)
        if dbtext.text == "Dashboard":
            print("PASS > Dashboard Option Found")

    def click_on_onboardmerchants(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.ONBOARDMERCHANT)))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click()", element)
        dbtext = self.driver.find_element(By.XPATH, self.ONBOARDMERCHANT)
        time.sleep(2)
        if dbtext.text == "Onboard Merchants":
            print("PASS > Onboard Merchants Option Found")

    def click_on_actlogs(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.ACTIVITYLOGS)))
        self.driver.execute_script("arguments[0].click()", element)
        dbtext = self.driver.find_element(By.XPATH, self.ACTIVITYLOGS)
        if dbtext.text == "Activity Logs":
            print("PASS > Activity Logs Option Found")

    def click_on_uac(self):
        element = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, self.USERACCESSCONTROL)))
        self.driver.execute_script("arguments[0].click()", element)
        dbtext = self.driver.find_element(By.XPATH, self.USERACCESSCONTROL)
        if dbtext.text == "User Access Control":
            print("FAIL > User Access Control Option Found")

    def click_on_pi(self):
        element = WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, self.PAYMENTINTEGRATION)))
        self.driver.execute_script("arguments[0].click()", element)
        if element.text == "Payment Integration":
            print("FAIL > Payment Integration Option Found")

    def click_on_obmtile(self):
        # self.click_using_js(self.ONBOARDMERCHANTTILE)
        dbtext = self.driver.find_element(By.XPATH, self.ONBOARDMERCHANTTILE)
        if dbtext.text == "Onboarded Merchants":
            print("PASS > Onboarded Merchants Tile Found")

    def click_on_pmtile(self):
        # self.click_using_js(self.PENDINGMERCHANTTILE)
        dbtext = self.driver.find_element(By.XPATH, self.PENDINGMERCHANTTILE)
        if dbtext.text == "Pending Merchants":
            print("PASS > Pending Merchants Tile Found")

    def click_on_tutile(self):
        # self.click_using_js(self.TOTALUSERSTILE)
        dbtext = self.driver.find_element(By.XPATH, self.TOTALUSERSTILE)
        if dbtext.text == "Total Users":
            print("FAIL > Total Users Tile Found")

    def click_on_tttile(self):
        # self.click_using_js(self.TOTALTEAMTILE)
        dbtext = self.driver.find_element(By.XPATH, self.TOTALTEAMTILE)
        if dbtext.text == "Total Teams":
            print("FAIL > Total Teams Tile Found")

    def click_on_mstile(self):
        # self.click_using_js(self.MERCHANTSUMMARYTILE)
        dbtext = self.driver.find_element(By.XPATH, self.MERCHANTSUMMARYTILE)
        if dbtext.text == "Merchant Summary":
            print("PASS > Merchant Summary Tile Found")

    def click_on_matile(self):
        # self.click_using_js(self.MYACTIVITIESTILE)
        dbtext = self.driver.find_element(By.XPATH, self.MYACTIVITIESTILE)
        if dbtext.text == "My Activities":
            print("PASS > My Activities Tile Found")

    def click_on_mbctile(self):
        # self.click_using_js(self.MYACTIVITIESTILE)
        dbtext = self.driver.find_element(By.XPATH, self.MERCHANTCOUNTRIESTILE)
        if dbtext.text == "Merchants By Country":
            print("PASS > Merchants By Country Tile Found")

    def click_on_mttile(self):
        # self.click_using_js(self.MYACTIVITIESTILE)
        dbtext = self.driver.find_element(By.XPATH, self.MYTASKTILE)
        if dbtext.text == "My Task":
            print("PASS > My Task Tile Found")

    def verifying_edit_option(self):
        element1 = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.ONBOARDMERCHANTTILE)))
        self.driver.execute_script("arguments[0].click()", element1)
        element2 = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.MERCHANTACTIONBUTTON)))
        self.driver.execute_script("arguments[0].click()", element2)
        dbtext = self.driver.find_element(By.XPATH, self.EDITBUTTON)
        if dbtext.text == "Edit":
            print("FAIL > Edit Button Found")

    def verifying_viewndelete(self):
        element1 = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.ACTIVITYLOGS)))
        self.driver.execute_script("arguments[0].click()", element1)
        time.sleep(2)
        ulstext = self.driver.find_elements(By.CLASS_NAME, self.USERLOGINSUCCESSFULLY)
        if ulstext[0].text == "User Login successfully":
            print("Pass > View Works Fine > User Login successfully Text Found")
        else:
            print("Fail > View Not Works > User Login successfully Text Not Found")
        loggedbytext = self.driver.find_elements(By.CLASS_NAME, self.LOGINSUER)
        if loggedbytext[0].text == "Kylian Mbappe":
            print("Pass > Logged by = Kylian Mbappe Found")
        else:
            print("Fail > Logged by = Some Other Name")

    def verifying_Labels(self):
        element2 = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.ACTIVITYLOGS)))
        self.driver.execute_script("arguments[0].click()", element2)
        dbtext = self.driver.find_element(By.XPATH, self.LEVELS)
        if dbtext.text == "Levels":
            print("PASS > Levels Label Found")
        else:
            print("FAIL > Levels Label Not Found")
        dbtext = self.driver.find_element(By.XPATH, self.MODULE)
        if dbtext.text == "Module":
            print("PASS > Module Label Found")
        else:
            print("FAIL > Module Label Not Found")
        dbtext = self.driver.find_element(By.XPATH, self.DESC)
        if dbtext.text == "Description":
            print("PASS > Description Label Found")
        else:
            print("FAIL > Description Label Not Found")
        dbtext = self.driver.find_element(By.XPATH, self.IPADD)
        if dbtext.text == "IP Addess":
            print("PASS > IP Address Label Found")
        else:
            print("FAIL > IP Address Label Not Found")
        dbtext = self.driver.find_element(By.XPATH, self.LOGGEDBY)
        if dbtext.text == "Logged By":
            print("PASS > Logged By Label Found")
        else:
            print("FAIL > Logged By Label Not Found")
        dbtext = self.driver.find_element(By.XPATH, self.DATETIME)
        if dbtext.text == "Date & Time":
            print("PASS > Date & Time Label Found")
        else:
            print("FAIL > Date & Time Label Not Found")
