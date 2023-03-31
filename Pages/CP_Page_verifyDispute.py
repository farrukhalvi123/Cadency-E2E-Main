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
from Constants.URLS import TestData



class Open_dispute_tag():
    def __init__(self,driver):
        self.driver= driver

        self.inv_sp=             "//p[normalize-space()='Invoices']"
        self.panel=              "//div[@aria-label='Dashboard']//div[@class='menu-content ng-star-inserted']"
        self.account_st_opt=     "//p[normalize-space()='Account Statement']"
        self.d_inv=              "//div[@class='in-active wrap-text-all ng-star-inserted']"
        self.d_accstate=         "//div[@class='in-active wrap-text-all ng-star-inserted']"
        # self.d_tagname=          "//span[contains(text(), 'Disputed ')]"
        self.d_tagname  =          "//span[@class='cus-minibadge badge cus-status-red width-90 text-center justify-content-center ng-star-inserted']"
        self.p_tagname=           "//tbody/tr[1]/td[1]/div[1]/span[1]"
        self.Inv_tab=            "//p[normalize-space()='Invoices']"
        # self.getclassforinv=       "//tbody/tr[1]/td[1]/div[1]/div[1]"
        self.getclassforinv= "//td[@class='max-width-300 overflow-hidden custom-status-wrapper statusCenter font-bold ng-star-inserted'][position() mod 2 = 1]"

        # self.p1= "//td[@class='max-width-300 overflow-hidden custom-status-wrapper statusCenter font-bold ng-star-inserted']"
        # self.p1_subclass_for_inv_name=getclassforinv=       "//div[@class='ng-star-inserted']"

    def hovering(self):
               self.driver.find_element(By.XPATH, self.panel).click()
               self.driver.find_element(By.XPATH, self.inv_sp).click()

    def catch_tag(self):
        # save_inv_name = self.driver.find_element(By.XPATH, self.getclassforinv)
        # time.sleep(5)
        # print(save_inv_name.text)
        # time.sleep(5)
        # save_tag_dispute = self.driver.find_element(By.XPATH, self.d_tagname)
        # # save_tag_dispute= save_inv_name.find_element(By.XPATH, self.d_tagname)
        # time.sleep(4)
        # print(save_tag_dispute.text)








        save_inv_name = self.driver.find_element(By.XPATH, self.getclassforinv)
        time.sleep(7)
        # print(save_inv_name)
        texting= save_inv_name.text

        if texting.find('disputed') != 1:
            print('invoice is disputed ')
        else:
            print('inv is not disputed')
        time.sleep(4)

            # save_tag = save_inv_name.find_element(By.XPATH, self.d_tagname)
            # print(save_tag.text)
            # time.sleep(6)


        # save_tag = save_inv_name.find_element(By.XPATH, self.d_tagname)
        # print(save_tag.text)
        # time.sleep(6)
        # assert save_tag.text == "disputed"

        # elements = self.driver.find_elements(By.XPATH, self.getclassforinv)
        # time.sleep(4)
        #
        #
        # for element in elements:
        #     print(element.text)








                    # save_tag = save_inv_name.find_element(By.XPATH, self.d_tagname)



                # save_tag = save_inv_name.find_element(By.XPATH, self.d_tagname)
                # print(save_tag.text)

                # code for printing invoices name of 5 entries

                # p11=self.driver.find_element(By.XPATH, self.p1)
                #
                #     p22= self.driver.find_element(By.XPATH, self.getclassforinv)
                #
                #
                #           for i11 in p22:
                #     print(p22.text)


                # sisi=save_tag
                # print(sisi + 'hoho')
                # print(save_tag.text)






















