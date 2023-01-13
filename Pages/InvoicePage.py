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
from selenium.common import exceptions

WORDS = "".join((random.choice(string.ascii_letters) for i in range(10)))
randinteger = ''.join(["{}".format(randint(0, 9)) for num in range(0, 6)])
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
        # randomcurrency = random.choice(currencies)
        # randomcurrency.click()
        try:
            for cur in currencies:
                if cur.text == 'USD':
                    cur.click()
        except exceptions.StaleElementReferenceException as e:
            print(e)
            # pass
            #         currencyselect[1].click()

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
    def add_an_item(self):
        items = self.driver.find_elements(By.CLASS_NAME, self.ADDINVITEMS)
        self.input_element(self.ADDITEMNAME, WORDS)
        n = 5
        self.input_element(self.ADDITEMCODE, randinteger)
        # type_drop = self.driver.find_elements(By.XPATH,self.ADDITEMTYPEDD)
        # self.driver.execute_script("arguments[0].click()",type_drop[3])
        # # type_drop[3].click()
        # self.click_element(self.ADDITEMTYPE)
        self.input_element(self.ADDITEMUNITPRICEID, randinteger)
        # up = self.driver.find_elements(By.ID,self.ADDITEMUNITPRICEID)
        # up[1].send_keys(self.randinteger)
        # # up[3].send_keys(self.randinteger)
        self.click_element(self.ADDITEMSAVEBUTTON)
        self.wait(2)
        # itemdrop = self.driver.find_elements(By.XPATH, self.INVITEMSDD)
        # itemdrop[1].click()
        # self.driver.find_element(By.XPATH,"//span[contains(text(),'"+WORDS+"')]").click()

    def Add_inv_items(self):
        taxdd = self.driver.find_elements(By.CLASS_NAME, self.TAXDD)
        taxdd[1].click()
        time.sleep(2)
        try:
            items = self.driver.find_elements(By.XPATH,self.ADDINVITEMS)
            print("this is the list of items",len(items))
            items[2].click()
        except:
            self.add_an_item()
    def Save_invoice(self):
        self.click_using_js(self.SAVEBTN)
        self.wait(5)
        # self.wait(2)
        # additem  = self.driver.find_element(By.CLASS_NAME,self.ADDINVITEMS )
        # print(itemlist)
        # for items in itemlist:
        #     print(items.text)
        #     items.click()
        # # random_item = random.choice(itemlist)

    def enter_references(self):
        self.input_element(self.REFERENCE,WORDS)

    def add_item_description(self,desc):
        self.input_element(self.DESCRIPTION,desc)

    def enter_quantity(self):
        self.randinteger = ''.join(["{}".format(randint(0, 9)) for num in range(0, 3)])
        self.input_element(self.QUANTITY, 30)

    def enter_price(self):
            priceamnt = self.driver.find_element(By.XPATH,self.PRICE)
            if priceamnt.text == 0.00:
                self.input_element(self.PRICE,randinteger)
            else:
                print("The amount is prefilled",priceamnt.text)

    def enter_discount(self):
        self.randinteger = ''.join(["{}".format(randint(0, 9)) for num in range(0, 2)])
        self.input_element(self.DISCOUNT,20)

    def select_tax(self,tcomp,trate):
        taxdd = self.driver.find_elements(By.CLASS_NAME,self.TAXDD)
        taxdd[2].click()
        time.sleep(2)
        try:
            taxes = self.driver.find_elements(By.XPATH,self.TAXSELECT)
            taxes[1].click()
        except:
            taxes = self.driver.find_elements(By.XPATH, self.TAXSELECT)
            taxes[0].click()
            self.enter_new_tax(tcomp,trate)

    def enter_new_tax(self,tcomp,trate):
        self.input_element(self.TAXRATENAME,WORDS)
        self.input_element(self.TAXCOMP, tcomp)
        self.input_element(self.TAXRATE, trate)
        self.Save_invoice()

    def invoice_amount(self):
        self.amount = self.get_element_text(self.AMOUNT)
        print(self.amount)






