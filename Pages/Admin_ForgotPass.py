import datetime
import os
import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from Constants.URLS import TestData


class AdminForgotPass():

    def __init__(self, driver):
        self.driver = driver
        self.FORGOT_PASSWORD = "//span[normalize-space()='Forgot Password?']"

    def click_on_forgotpass(self):
        forgetpwd = self.driver.find_element(By.XPATH,self.FORGOT_PASSWORD)
        self.driver.execute_script("arguments[0].click()", forgetpwd)