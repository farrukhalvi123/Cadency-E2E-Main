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
from Pages.InvoicePage import *

from Constants.URLS import TestData
INVPAGE = InvoicePage()
class Cns():
    def __init__(self, driver):
        self.driver = driver

        self.open_filter = "//a[contains(text(), 'Open')]"
        # self.open_count = "//span[contains(text(), '0')]"
        self.opennumber= "ml-1.p-badge.p-component.p-badge-no-gutter.p-badge-info"

        self.nukhty3 = "//tbody/tr[1]/td[9]/div[1]/button[1]/*[1]//*[name()='svg']"
        self.add_cn = "//a[normalize-space()='Add Credit Note']"
        # self.cn_number = "//input[@id='customerName']"
        # self.cn_amount = "//input[@placeholder='Enter Amount']"
        self.billing_add_dd = "//*[@id='billingCentreId']"
        self.ba_2 = "//span[normalize-space()='sam']"
        self.save_but = "//button[@type='submit']"
        # self.showcnum= "//div[@class='text-primary-10 font-bold']"
        self.showcnum= 'text-primary-10 font-bold'

    def Opentab(self):
        openfil = self.driver.find_element(By.XPATH, self.open_filter)
        # driver.execute_script("arguments[3].click;", openfil)
        openfil.click()
        time.sleep(3)


    def checkopeninv(self):
        # try:
            self.Opentab()
            # count= self.driver.find_element(By.XPATH,self.open_count)
            count= self.driver.find_elements(By.CLASS_NAME, self.opennumber)
            sisi=count[2].text
            print(sisi)
            s= count[2].text
            print(s)
            hi=type(int(s))
            print(hi)
            # digi= s.isdigit()

            if s== '0':
                print("first create invoice")
                return INVPAGE.ClickOnAddButton()


            elif s != '0':
                print("no action is need")





        # except:
        #     print("jsjsjdjdj")

    # def selectCn(self):
    #     threedash = self.driver.find_element(By.XPATH, self.nukhty3)
    #     threedash.click()
    #     selectCnote = self.driver.find_element(By.XPATH, self.add_cn)
    #     selectCnote.click()
    #     time.sleep(3)

    def fillvalue(self):

        # enteritem=self.driver.find_element(By.XPATH, self.cn_number)
        # enteritem.click()
        time.sleep(3)
        addbillcenter=self.driver.find_element(By.XPATH, self.billing_add_dd)
        addbillcenter.click()
        time.sleep(3)
        selectcenter= self.driver.find_element(By.XPATH, self.ba_2)
        selectcenter.click()
        time.sleep(3)
        save=self.driver.find_element(By.XPATH, self.save_but)
        save.click()
        time.sleep(3)






    def CNtext(self):
        # cnclass = self.driver.find_element(By.XPATH,self.showcnum).text()
        cnclass = self.driver.find_element(By.CLASS_NAME, self.showcnum)
        i= cnclass.text
        print(i)

