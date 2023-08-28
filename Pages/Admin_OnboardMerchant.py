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


class OnboardingMerchant():

    def __init__(self, driver):
        self.driver = driver

        self.ADDMERCHANTBUTTON = "//span[normalize-space()='Add Merchant']"
        self.LEGALBUSINESSNAME = "name"
        self.BUSINESSTYPEDD = '//*[contains(@class,"p-dropdown-trigger-icon")]'  # same class for INDUSTRY, COUNTRY, STATE, CITY, CURRENCY, INVOICE MODE
        self.SELECTBUSINESS = "//span[normalize-space()='Company']"
        self.SELECTINDUSTRY = "//span[normalize-space()='Financial services and insurance']"
        self.COUNTRYTEXTBOX = '//*[contains(@class,"p-dropdown-filter p-inputtext p-component ng-tns")]'  # same search text bar class for COUNTRY, STATE, CITY, CURRENCY
        self.SELECTCOUNTRY = "//span[normalize-space()='Swaziland']"
        self.SELECTSTATE = "//span[normalize-space()='Manzini']"
        self.SELECTCITY = "//span[normalize-space()='Manzini']"
        self.SELECTCURRENCY = "//span[normalize-space()='USD']"
        self.SELECTINVOICEMODE = "//span[normalize-space()='Normal']"
        self.MERCHANTSTATUS = "//div[@aria-label='Active']"
        self.BUSINESSPHONE = "phone"
        self.WEBSITE = '//*[contains(@placeholder,"Enter website")]'
        self.EMAIL = '//*[contains(@placeholder,"Enter your Email")]'
        self.ZIPCODE = '//*[contains(@placeholder,"Enter Zip Code")]'
        self.ALLOWBILLINGCENTER = "p-inputswitch.p-component"
        self.MERCHANTLOGOUPLOAD = "//input[@type='file']"
        self.MERCHANTLOGO = "//div[@class='icon-wrap']"
        self.SAVEBUTTON = "//span[normalize-space()='Save']"

        # Filters Elements

        self.ONBOARDMERCHANTFILTERS = '//*[contains(@type,"button")]'
        self.ENTITYSTATUSFILTER_ACTIVE = "//span[normalize-space()='Active']"
        self.APPLYBUTTON = "//button[normalize-space()='Apply']"
        self.CLEARBUTTON = "//button[normalize-space()='Clear']"

    def click_addmerchant_button(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.ADDMERCHANTBUTTON)))
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(3)

    def filling_form(self, Name, Business_Phone, Website, Email, Zipcode):
        self.driver.find_element(By.ID, self.LEGALBUSINESSNAME).send_keys(Name)
        time.sleep(1)
        self.driver.find_element(By.ID, self.BUSINESSPHONE).send_keys(Business_Phone)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.WEBSITE).send_keys(Website)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.EMAIL).send_keys(Email)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.ZIPCODE).send_keys(Zipcode)
        time.sleep(1)

    def select_businesstype(self):
        businessdd = self.driver.find_elements(By.XPATH, self.BUSINESSTYPEDD)
        businessdd[0].click()
        self.driver.find_element(By.XPATH, self.SELECTBUSINESS).click()

    def select_industry(self):
        industrydd = self.driver.find_elements(By.XPATH, self.BUSINESSTYPEDD)
        industrydd[1].click()
        time.sleep(2)
        element = self.driver.find_element(By.XPATH, self.SELECTINDUSTRY)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(2)

    def select_merchant_country(self):
        countrydd = self.driver.find_elements(By.XPATH, self.BUSINESSTYPEDD)
        countrydd[2].click()
        time.sleep(1)
        countrytextbox = self.driver.find_element(By.XPATH, self.COUNTRYTEXTBOX)
        countrytextbox.send_keys("Swaziland")
        self.driver.find_element(By.XPATH, self.SELECTCOUNTRY).click()

    def select_merchant_state(self):
        time.sleep(5)
        statedd = self.driver.find_elements(By.XPATH, self.BUSINESSTYPEDD)
        statedd[3].click()
        time.sleep(1)
        statetextbox = self.driver.find_element(By.XPATH, self.COUNTRYTEXTBOX)
        statetextbox.send_keys("Manzini")
        self.driver.find_element(By.XPATH, self.SELECTSTATE).click()
        time.sleep(3)

    def select_merchant_city(self):
        citydd = self.driver.find_elements(By.XPATH, self.BUSINESSTYPEDD)
        citydd[4].click()
        time.sleep(1)
        citytextbox = self.driver.find_element(By.XPATH, self.COUNTRYTEXTBOX)
        citytextbox.send_keys("Manzini")
        self.driver.find_element(By.XPATH, self.SELECTCITY).click()
        time.sleep(3)

    def select_merchant_currency(self):
        currencydd = self.driver.find_elements(By.XPATH, self.BUSINESSTYPEDD)
        currencydd[5].click()
        time.sleep(1)
        currencytextbox = self.driver.find_element(By.XPATH, self.COUNTRYTEXTBOX)
        currencytextbox.send_keys("USD")
        self.driver.find_element(By.XPATH, self.SELECTCURRENCY).click()
        time.sleep(3)

    def select_merchant_invoicemode(self):
        invmodedd = self.driver.find_elements(By.XPATH, self.BUSINESSTYPEDD)
        invmodedd[6].click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.SELECTINVOICEMODE).click()
        time.sleep(3)

    def select_merchant_status(self):
        self.driver.find_element(By.XPATH, self.MERCHANTSTATUS).click()
        time.sleep(3)

    def enable_bc(self):
        bcbutton = self.driver.find_elements(By.CLASS_NAME, self.ALLOWBILLINGCENTER)
        bcbutton[0].click()
        time.sleep(3)

    def upload_merchant_logo(self):
        path = os.getcwd()
        element = self.driver.find_element(By.XPATH, self.MERCHANTLOGOUPLOAD)
        self.driver.execute_script("arguments[0].style.display = 'block';", element)
        path3 = os.path.abspath(path + r'\\TestData\\Picture\\qa.jpg')
        element.send_keys(path3)
        time.sleep(3)

    def save_merchant(self):
        self.driver.find_element(By.XPATH, self.SAVEBUTTON).click()
        time.sleep(6)

    def click_merchant_filters(self):
        element = self.driver.find_elements(By.XPATH, self.ONBOARDMERCHANTFILTERS)
        element[5].click()
        time.sleep(3)

    def select_entity_status_filters(self):
        esdd = self.driver.find_elements(By.XPATH, self.BUSINESSTYPEDD)
        esdd[1].click()
        time.sleep(3)

    # self.driver.find_elements(By.CLASS_NAME, self.ENTITYSTATUSFILTER_ACTIVE).click()

    def select_entity_country_filters(self):
        esdd = self.driver.find_elements(By.XPATH, self.BUSINESSTYPEDD)
        esdd[2].click()
        self.driver.find_element(By.XPATH, self.COUNTRYTEXTBOX).send_keys("Swaziland")
        self.driver.find_element(By.XPATH, self.SELECTCOUNTRY).click()

    def click_clearbutton_filters(self):
        self.driver.find_element(By.XPATH, self.CLEARBUTTON).click()

    def click_applybutton_filters(self):
        self.driver.find_element(By.XPATH, self.APPLYBUTTON).click()
        time.sleep(3)
