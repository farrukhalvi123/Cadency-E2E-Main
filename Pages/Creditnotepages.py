import datetime
import os
import time
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from Elements.LoginElements import loginelements
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from webdriver_manager.core import driver

from Constants.URLS import TestData

class Cns():
    def __init__(self, driver):

        self.driver = driver

        self.open_filter = "//a[contains(text(), 'Open')]"

        self.nukhty3 = "//tbody/tr[1]/td[9]/div[1]/button[1]/*[1]//*[name()='svg']"
        self.add_cn = "//a[normalize-space()='Add Credit Note']"
        self.cn_number = "//input[@id='customerName']"
        self.cn_amount = "//input[@placeholder='Enter Amount']"
        self.billing_add_dd = "//span[@class='p-dropdown-trigger-icon ng-tns-c73-1462 pi pi-chevron-down']"
        self.ba_2 = "//span[normalize-space()='Billing Center 1']"
        self.save_but = "//button[@type='submit']"

    def Opentab(self):
        openfil = self.driver.find_element(By.XPATH, self.open_filter)
        # driver.execute_script("arguments[3].click;", openfil)
        openfil.click()
        time.sleep(3)

    def selectCn(self):
        threedash = self.driver.find_element(By.XPATH, self.nukhty3)
        threedash.click()
        selectCnote = self.driver.find_element(By.XPATH, self.add_cn)
        selectCnote.click()

