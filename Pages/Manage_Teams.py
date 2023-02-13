import datetime
import os
import time
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Elements.Admin_LoginScreenElements import AdminportalElements
from Elements.Manage_Teams_Elements import ManageTeamsElements
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Constants.URLS import TestData


class ManageTeams(ManageTeamsElements):

    def __init__(self, driver):
        super().__init__(driver)

    def click_manageteams(self):
        self.move_to_element(self.LEFTSIDENAVMENU)
        self.wait(1)
        self.click_using_js(self.USERACCESSCONTROL)
        self.click_using_js(self.MANAGETEAMS)
        time.sleep(2)

    def add_new_team(self):
        self.click_using_js(self.ADDBUTTON)

    def enter_teamname_desc(self, teamname, teamdesc):
        self.input_element(self.TEAMNAME, teamname)
        self.input_element(self.TEAMDESC, teamdesc)
        time.sleep(3)

    def goto_assignusers_tab(self):
        self.click_using_js(self.ASSIGNUSERTAB)

    def searchuser(self, user):
        self.input_element(self.ASSIGNUSERSEARCHBAR, user)

    def check_userin_allusersbox(self):
        username = self.driver.find_element(By.ID, self.ALLUSERSBOX)
        alluserbox = username.find_elements(By.CLASS_NAME,
                                            "p-ripple.p-element.cdk-drag.p-picklist-item.ng-star-inserted")
        if (len(alluserbox)) == 1:
            print("Pass > User found in All User Box")
        else:
            print("Fail > User not found in All User Box")

    def check_userin_assignedusersbox(self):
        username = self.driver.find_element(By.ID, self.ASSIGNEDUSERBOX)
        alluserbox = username.find_elements(By.CLASS_NAME,
                                            "p-ripple.p-element.cdk-drag.p-picklist-item.ng-star-inserted")
        # print(len(alluserbox))
        if (len(alluserbox)) == 1:
            print("Pass > User found in Assigned User Box")
        else:
            print("Fail > User not found in Assigned User Box")

    def move_userto_assignusers(self):
        self.click_element(self.ASSIGNUSERSEARCHUSERFOUND)
        self.click_element(self.MOVESINGLEBUTTON)
        time.sleep(4)

    def select_modules(self):
        self.click_element(self.MODULESTAB)
        self.click_element(self.DASHBOARD)
        getnames = self.driver.find_elements(By.NAME, self.OTHERCHECKBOXES) # Getting NAME which is associated with all checkboxes
        getnames[20].click() # Click on NAME+20th indexing checkbox
        time.sleep(2)
        getnames[32].click()  # Click on NAME+32nd indexing checkbox
        time.sleep(2)

    def save_team(self, qateam):
        self.click_element(self.SAVETEAM)
        time.sleep(4)
        self.click_element(self.MANAGETEAMSEARCHBAR)
        self.input_element(self.MANAGETEAMSEARCHBAR, qateam)
        time.sleep(2)
        getteamname = self.get_element_text(self.SEARCHEDQATEAM)
        if getteamname == "QA Team":
            print("Team Save & Verified Successfully... ")
