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
        self.click_using_js(self.CUSTOMERANDRECEIVABLETAB)
        self.click_using_js(self.INVOICETAB)
        print("Click hogya bhai")

    def ClickOnAddButton(self):
        self.click_using_js(self.ADDINVOICE)