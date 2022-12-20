from random import *
import time
from datetime import date, datetime, timedelta
import random
import string
from selenium.webdriver import Keys
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
            self.wait(5)

    def ClickOnAddButton(self):
        self.click_using_js(self.ADDINVOICEBTN)
        self.wait(5)
    def open_customer_selection_dd(self):
        self.click_element(self.CUSTNAMEDD)

    def select_customer(self):
        self.click_element(self.CUSTNAMEDD_VALUE)
        time.sleep(2)

    def add_new_customer(self):
        self.click_element(self.CUSTNAMEDD_VALUE1)
        # if len(self.get_all_elements(self.CUSTNAMEDD_VALUE)) > 0 :
        #     customers = self.driver.find_element(By.CLASS_NAME,self.CUSTNAMEDD_VALUE)
        #     print(customers.text)
        #     customers[1].click()
        #
        # self.wait(3)
        # customername = self.driver.find_elements(By.XPATH,self.CUSTNAMEDD_VALUE)
        # for cust in customername:
        #     cust.click()
        #     print(cust.text)
        #     break





            # if cust == self.driver.find_elements(By.XPATH,self.CUSTNAMEDD_VALUE):
            #      cust[1].click()
            #      break


    def select_Currency(self):
        self.click_element(self.CURRENCYDD)
        self.wait(5)
        currencies = self.driver.find_elements(By.CLASS_NAME,self.CAD)
        for cur in currencies:
            if cur.text == 'CAD':
                cur.click()
        # currencyselect[1].click()

    def emailfield_status(self):
        self.verify_element_disabled(self.INV_EMAIL)

    def invoice_num_status(self):
        self.verify_element_disabled(self.INVNUM)

    def invoice_date(self):
        global current_time
        current_time = date.today().strftime('%m/%d/%Y')
        datefield = self.driver.find_element(By.XPATH,self.INVDATE)
        datefield.send_keys(Keys.CONTROL + 'a' + Keys.NULL, current_time,Keys.ENTER)
        # self.input_element(self.INVDATE,Keys.CONTROL + 'A')
        # self.input_element(self.INVDATE, Keys.DELETE)
        # self.input_element(self.INVDATE, current_time)
        # self.input_element(self.INVDATE,Keys.ENTER)
        time.sleep(5)

    def invoice_duedate(self):
        current_time = date.today()
        day = timedelta(days = 90)
        dudate = (current_time+day).strftime('%m/%d/%Y')
        datefield = self.driver.find_element(By.XPATH,self.INVDUEDATE)
        datefield.send_keys(Keys.CONTROL + 'a' + Keys.NULL, dudate, Keys.ENTER)


    def Add_inv_items(self):
        itemdrop = self.driver.find_elements(By.XPATH,self.INVITEMSDD)
        itemdrop[1].click()
        self.click_element(self.ADDINVITEMS)
        WORDS = "".join((random.choice(string.ascii_letters) for i in range(10)))
        self.input_element(self.ADDITEMNAME,WORDS)
        n = 5
        self.randinteger = ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])
        self.input_element(self.ADDITEMCODE,self.randinteger)
        type_drop = self.driver.find_elements(By.XPATH,self.ADDITEMTYPEDD)
        type_drop[3].click()
        self.click_element(self.ADDITEMTYPE)
        up = self.driver.find_elements(By.ID,self.ADDITEMUNITPRICEID)
        up[1].send_keys(self.randinteger)
        # up[3].send_keys(self.randinteger)
        self.click_element(self.ADDITEMSAVEBUTTON)
        self.wait(2)
        # itemdrop = self.driver.find_elements(By.XPATH, self.INVITEMSDD)
        # itemdrop[1].click()
        # self.driver.find_element(By.XPATH,"//span[contains(text(),'"+WORDS+"')]").click()
    def Save_invoice(self):
        self.click_using_js(self.SAVEBTN)
        self.wait(2)
        # self.wait(2)
        # additem  = self.driver.find_element(By.CLASS_NAME,self.ADDINVITEMS )
        # print(itemlist)
        # for items in itemlist:
        #     print(items.text)
        #     items.click()
        # # random_item = random.choice(itemlist)