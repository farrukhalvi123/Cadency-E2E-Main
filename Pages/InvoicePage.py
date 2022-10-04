import os
import time
from random import randint
from selenium.webdriver.common.by import By
from Constants.URLS import TestData
from Elements.InvoiceElements import invoiceelements
from Elements.Customer_elements import customerelements


class InvoicePage(invoiceelements, customerelements):

    def __init__(self, driver):
        super().__init__(driver)

    def ClickOnInvoiceTab(self):
        try:
            assert "template" in self.driver.current_url
            self.driver.get(TestData.CUSTOMERINVOICES)
            self.wait(5)
        except:
            self.click_using_js(self.CUSTOMERANDRECEIVABLETAB)
            self.click_using_js(self.INVOICETAB)
            print("Click hogya bhai")
            self.wait(5)

    def ClickOnAddButton(self):
        self.click_using_js(self.ADDINVOICEBTN)
        self.wait(5)

    def select_customer(self):
        self.click_element(self.CUSTNAMEDD)
        self.wait(3)
        customername = self.driver.find_elements(By.CLASS_NAME,self.CUSTNAMEDD_VALUE)
        print(customername)
        # for cust in customername:
        #     print(cust)
            # if cust == "Amir":
            #     cust.click()
            #     break


    def select_Currency(self):
        self.click_using_js(self.CURRENCYDD)
        self.wait(2)
        currencyselect = self.driver.find_elements(By.CLASS_NAME,self.CAD)
        currencyselect[1].click()

