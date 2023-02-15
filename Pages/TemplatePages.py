import datetime
import os
import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# from Elements.LoginElements import loginelements
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Constants.URLS import TestData
# from Elements.TemplateElements import TemplateElements


class TemplatePage():
    def __init__(self, driver):
        self.driver = driver
        self.SETTINGCOGS = "Group_19806"
        self.TEMPLATETILE = "//div[contains(text(),'Templates')]"
        self.ADDTEMPLATE = "//button[@class='p-element p-button-primary button-with-icon btn-150 p-button p-component ng-star-inserted']"
        self.TEMPLATENAME = "TemplateName"

    def click_settingsgear(self):
        time.sleep(5)
        self.driver.find_element(By.ID,self.SETTINGCOGS).click()

    def select_template(self):
        temptitle = self.driver.find_element(By.XPATH,self.TEMPLATETILE)
        self.driver.execute_script("arguments[0].click()",temptitle)

    def click_addtemplate(self):
        self.driver.find_element(By.XPATH,self.ADDTEMPLATE).click()

    def enter_templatename(self,temp):
        self.driver.find_element(By.ID,self.TEMPLATENAME).send_keys(temp)

