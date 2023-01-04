import datetime
import os
import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Elements.Admin_LoginScreenElements import AdminportalElements
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Constants.URLS import TestData


class AdminForgotPass(AdminportalElements):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_forgotpass(self):
        self.click_using_js(self.FORGOT_PASSWORD)