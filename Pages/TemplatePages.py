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
from Elements.TemplateElements import TemplateElements


class TemplatePage(TemplateElements):
    def __init__(self, driver):
        super().__init__(driver)

    def click_settingsgear(self):
        self.click_element(self.SETTINGCOGS)

    def select_template(self):
        self.click_element(self.TEMPLATETILE)

    def click_addtemplate(self):
        self.click_element(self.ADDTEMPLATE)

    def enter_templatename(self,temp):
        self.input_element(self.TEMPLATENAME,temp)

