import datetime
import os
import re
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
        self.OPENCN = "//p[@class='paragraph-text-navigation active']"

        self.open_filter = "//a[contains(text(), 'Open')]"

        self.nukhty3 = "//tbody/tr[1]/td[9]/div[1]/button[1]/*[1]//*[name()='svg']"
        self.add_cn = "//a[normalize-space()='Add Credit Note']"
        # self.cn_number = "//input[@id='customerName']"
        # self.cn_amount = "//input[@placeholder='Enter Amount']"
        self.billing_add_dd = "//*[@id='billingCentreId']"
        self.ba_2 = "//span[normalize-space()='sam']"
        self.save_but = "//button[@type='submit']"

        self.creditmodel="//p[normalize-space()='Credit Notes']"
        self.searchnote = "text-primary-10.font-bold"
        self.click_receive_tag = "//p[normalize-space()='Customers & Receivables']"
        # self.showcnum= "//div[@class='text-primary-10 font-bold']"

    def click_drop_CR(self):
        self.driver.find_element(By.XPATH, self.click_receive_tag).click()


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
        time.sleep(3)

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


    def CNmodule(self):
         creditnotepage = self.driver.find_element(By.XPATH, self.creditmodel)
         creditnotepage.click()
         time.sleep(3)

    def takecn(self):
        cnno = self.driver.find_elements(By.CLASS_NAME, self.searchnote)
        newcnn = cnno[1].text
        print(newcnn)
        ext_cn= newcnn.split("-")[1]
        print(ext_cn)



        # digi = newcnn.isdigit()
        # print(digi)
        # print(newcnn)
        # res = [int(i) for i in newcnn.split() if i.isdigit()]
        # print(res)
        # abc = "CRN 00004"
        # res1 = [int(i) for i in abc.split() if i.isdigit()]
        # print(res1)
    # def CNtext(self):
    #     cnclass = self.driver.find_element(By.XPATH,self.showcnum).text()
    #     print(cnclass)
    #

    def go_to_creditnotes(self):
        self.driver.find_element(By.XPATH,self.OPENCN).click()
        time.sleep(5)