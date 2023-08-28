import os
import re
from random import *
import time
from datetime import date, datetime, timedelta
import random
import string
import sys
import charset_normalizer
import requests
from PyPDF2 import PdfReader
# from bs4 import BeautifulSoup
from Constants.URLS import TestData
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Constants.URLS import TestData
# from Elements.InvoiceElements import invoiceelements
# from Elements.Customer_elements import customerelements
from selenium.common import exceptions, NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
import csv
import PyPDF2

WORDS = "".join((random.choice(string.ascii_letters) for i in range(10)))
randinteger = ''.join(["{}".format(randint(0, 5)) for num in range(0, 3)])

class InvoicePage():

    def __init__(self, driver):
        self.driver = driver
        self.CUSTOMERNAME = "//div[@class='side-title']"
        # self.invnum = "//a[normalize-space()='" + INV_NUM + "']"
        self.LOGO = "//div[@class='header-container']//img[@alt='Logo image']"
        self.CUSTOMERANDRECEIVABLETAB = "//p[normalize-space()='Customers & Receivables']"
        self.INVOICETAB =  "//p[normalize-space()='Invoices']"
        self.ADDINVOICEBTN = "//button[@class='p-element p-button-primary button-with-icon btn-150 p-button p-component']"
        self.CUSTNAMEDD =  "currency"
        self.CUSTNAMEDD_VALUE =  "(//li[@role='option'])[2]"
        self.CUSTNAMEDD_VALUE1 =  "//span[normalize-space()='+ Add New Customer']"
        self.CURRENCYDD =  "currency"
        self.CURRENCY = "p-ripple.p-element.p-dropdown-item"
        self.EXCHANGERATE =  "//a[normalize-space()='Modify Rate']"
        self.REFERENCE =  "//input[@placeholder='Enter Reference']"
        self.ITEMSELECTION = "//button[@class='p-element p-ripple p-autocomplete-dropdown ng-tns-c107-56 p-button p-component p-button-icon-only ng-star-inserted']//span[@class='p-button-icon pi pi-chevron-down']"
        self.DESCRIPTION =  "//input[@placeholder='Note']"
        self.QUANTITY =  "//input[@placeholder='Quantity']"
        self.PRICE =  "//input[@placeholder='Price']"
        self.DISCOUNT =  "//input[@placeholder='Disc %']"
        self.TAXDD = "//*[contains(@class,'p-element p-ripple p-autocomplete-dropdown ng-tns')]"
        self.TAXSELECT = "//*[contains(@class,'p-ripple p-element p-autocomplete-item ng-tns')]"
        self.SAVEBTN =  "//button[@class='p-element p-button-primary btn-150 p-button p-component']"
        self.INV_EMAIL =  "customerEmail"
        self.INVNUM =  "customerName"
        self.INVDATE = "//input[@placeholder='Please select invoice date']"
        self.INVDUEDATE = "//input[@placeholder='Please select due date']"
        self.INVITEMSDD = '//button[contains(@class,"p-element p-ripple p-autocomplete-dropdown ng-tns")]'
        self.ADDINVITEMS = "//*[contains(@class,'p-ripple p-element p-autocomplete-item ng-tns')]"
        self.ADDITEMNAME =  "name"
        self.ADDITEMCODE =  "code"
        self.ADDITEMTYPEDD = '//*[contains(@class,"p-dropdown-trigger ng-tns")]'
        self.ADDITEMTYPE =  "//li[@aria-label='Inventory']"
        self.ADDITEMUNITPRICEID =  "//input[@placeholder='Enter unit price']"
        self.ADDITEMUNITPRICETAGNAME = "type"
        self.ADDITEMSAVEBUTTON =  "(//button[@type='submit'])[3]"
        self.SELECTITEM =  "//span[contains(text(),'+WORDS+')]"
        self.TAXRATENAME =  "taxRateName"
        self.TAXCOMP =  "//span[normalize-space()='Tax Component']"
        self.TAXRATE =  "//p-inputnumber[@placeholder='Tax %']"
        self.AMOUNT =  "//td[@class='td-amount max-width-100']"
        self.INVSEARCHFIELD =  "//input[@placeholder='Search']"
        # self.INVOICE_NUMBER = "//a[normalize-space()='"+INV_NUM+"']"
        self.CSVICON =  "//div[@class='pages-section']//li[1]//div[1]"
        self.PDFICON =  "//*[contains(@class,'p-element p-button action-pdf btn')]"
        self.ACTIONBUTTON = "//*[contains(@class,'btn-container btn-center ng-star-inserted')]"
        self.STATUS = "//*[contains(@class,'overflow-hidden status-column ng-star-inserted')]"
        self.DOWNLOADINVOICE =  "//a[normalize-space()='Download Invoice']"
        self.CONFIRMATIONBTN = "//button[@type='submit']"
        self.NEXTBTN = "//span[@class='p-paginator-icon pi pi-angle-right']"
        self.PAGING = "//div[@aria-label='dropdown trigger']"
        self.FIFTYITEMS = "//span[normalize-space()='50']"
        self.ALLTILE = "//li[@class='p-highlight ng-star-inserted']"
        self.DISPUTEDTILE = "//div[@class='detailscreen-tabview left-aligned']//li[2]"
        self.OPENTILE = "p-ripple.p-element.p-tabview-nav-link"
        self.DISPUTETAG = "(//span[normalize-space()='Disputed'])"
        self.OPENSTATUS = "status-container.status-blue.ng-star-inserted"
        self.PAIDSTATUS = "status-container.status-green.ng-star-inserted"
        self.PARTIALLYPAIDSTATUS = "status-container.status-orange.ng-star-inserted"
        self.WAITINGFORFUNDSTAB = "status-container.status-orange3.ng-star-inserted"
        self.INVDETAILPAIDSTATUS = "status-container.status-green.ng-star-inserted"
        self.INVDETAILPARTIALPAIDSTATUS = "status-container.mr-2.status-orange.ng-star-inserted"
        self.INVDETAILWFFSTATUS = "status-container.mr-2.status-orange3.ng-star-inserted"
        self.INVDETAILOPENSTATUS = "status-container.mr-2.status-blue.ng-star-inserted"
        self.DUPLICATE = "//a[normalize-space()='Duplicate']"
        self.INVOICEANDCUSTOMER = "p-element.title-heading-1.text-primary-3"
        self.AMOUNT_BALANCE = "max-width-300.amount-column.font-bold.ng-star-inserted"
        self.DELETE = "//a[normalize-space()='Delete']"
        self.DELETEMSG = "//div[@aria-label='Invoice deleted successfully.']"
        self.VIEW = "//a[normalize-space()='View']"
        self.INVAMOUNT = "//div[@class='amount']"
        self.INVNUMBER = "//div[@class='invoice-title']"
        self.INVOICEEDIT = "//button[@class='p-element p-icon-button overlay-primary-6 p-button p-component ng-star-inserted']"
        self.EMAILSEND = "//button[@class='p-element p-icon-button overlay-primary-13 p-button p-component ng-star-inserted']"
        self.EMAILADDRESS = "//a[normalize-space()='selinakyle@yopmail.com']"
        self.EMAILSENDTOLABEL = "//span[@class='label-text']"
        self.DOWNLOADINVOICEBTN = "//div[@class='p-icon-button']"
        self.EMAILBODY = "//div[@class='angular-editor-textarea']"
        self.yop_EMAILFIELD = "loginfmt"
        self.HOTPASS = "passwd"
        self.DONTYESBTN = "idSIButton9"
        self.JUNKMAIL = "//div[@title='Junk Email']"
        self.EMAILS = "zKDWD.YbB6r.IKvQi.IjQyD.JCRRb.G1NES"
        self.SUBJECT = "subject"
        self.TOTALAMNT1 = "//cadency-create-invoice[@class='ng-star-inserted']//li[4]"
        self.TOTALAMNT1c1 = "grid-footer-text"
        self.INV_DETAIL_TOTAL = "total"
        self.INVTOTAL = "td"
        self.RECORDPAYMENT = "Group_19996"
        self.AMOUNTRECIEVED = "//input[@placeholder='Enter amount received']"
        self.PAYMENTDATE = "//input[@placeholder='Select date']"
        self.PAYMENTMODEID = "paymentTypeId"
        self.REFERENCENUMBERID = "referenceNumber"
        self.ENTERNOTE = "//textarea[@placeholder='Enter note']"
        self.BANKTRANSFER = "//span[normalize-space()='Bank Transfer']"
        self.ATTACHMENTS = "//button[@title='More actions']"
        self.DOWNLOADBTN = "//span[normalize-space()='Download']"
        self.EXPORT_INVOICE = "//button[@class='p-element p-icon-button overlay-primary-15 p-button p-component']"
        self.REMINDER = "//button[@class='p-element p-icon-button overlay-secondary-21 p-button p-component ng-star-inserted']"
        self.DISPUTE_ICON = "//button[@class='p-element p-icon-button overlay-primary-8 p-button p-component ng-star-inserted']"
        self.EMAILSENT_NOTIF = "//div[@id='toast-container']"
        self.DISP_INV_NUM = "//input[@id='InvoiceNumber']"
        self.CUSTOM_NAME = "CustomerName"
        self.REASON = "//li[@aria-label='Invoice InAccurate']"
        self.DISPUTEAMOUNT = "minmaxfraction"
        self.note = "Message"
        self.INVOICE_DETAILS = "max-width-300.ng-star-inserted"
        self.INV_CUSTOMER_NAME = "wrap-text-all.ng-star-inserted"
        self.Count_Footer= "//div[contains(@class, 'p-dropdown-trigger')][1]"
            # "p-dropdown-trigger.ng-tns-c73-102"
        self.Show_50Invs= "//span[contains(text(), '50')]"
        self.count_ALL_Ribn = "//span[@class='ml-1 p-badge p-component p-badge-info']"
        self.diabledbut = "//button[@class='p-ripple p-element p-paginator-next p-paginator-element p-link p-disabled']"
        self.inv_num_details= "//a[@class='p-element title-heading-1 text-primary-3'][position() mod 2 = 1]"
    #     //td[position() mod 2 = 1]















    def ClickOnInvoiceTab(self):
        CART = self.driver.find_element(By.XPATH,self.CUSTOMERANDRECEIVABLETAB)
        self.driver.execute_script("arguments[0].click()",CART)
        INVT= self.driver.find_element(By.XPATH,self.INVOICETAB)
        self.driver.execute_script("arguments[0].click()", INVT)
        time.sleep(10)
    def close_leftsidemenu(self):
        self.logo = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,self.LOGO)))
        # self.logo = self.driver.find_element(By.XPATH,self.LOGO)
        action = ActionChains(self.driver)
        action.move_to_element(self.logo).perform()
        time.sleep(6)

    def ClickOnAddButton(self):
        element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH,self.ADDINVOICEBTN)))
        # self.driver.find_element(By.XPATH,self.ADDINVOICEBTN).click()
        self.driver.execute_script("arguments[0].click()",element)
    def open_customer_selection_dd(self):
        time.sleep(2)
        inv_dd = self.driver.find_element(By.ID,self.CUSTNAMEDD)
        inv_dd.click()

    def select_customer(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.CUSTNAMEDD_VALUE).click()
        global custname
        custname = self.driver.find_element(By.XPATH,self.CUSTNAMEDD_VALUE)
        print(custname.text)

    def add_new_customer(self):
        self.driver.find_element(By.XPATH,self.CUSTNAMEDD_VALUE1)
        # if len(self.get_all_elements(self.CUSTNAMEDD_VALUE)) > 0 :
        #     customers = self.driver.find_elementself.CUSTNAMEDD_VALUE)
        #     print(customers.text)
        #     customers[1].click()
        #
        # time.sleep(3)
        # customername = self.driver.find_elementsself.CUSTNAMEDD_VALUE)
        # for cust in customername:
        #     cust.click()
        #     print(cust.text)
        #     break





        # if cust == self.driver.find_elementsself.CUSTNAMEDD_VALUE):
        #      cust[1].click()
        #      break


    def select_Currency(self):
        self.driver.find_element(By.ID,self.CURRENCYDD)
        time.sleep(5)
        currencies = self.driver.find_elements(By.CLASS_NAME,self.CURRENCY)
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
        self.driver.find_element(By.ID,self.INV_EMAIL).is_enabled()

    def invoice_num_status(self):
        self.driver.find_element(By.ID,self.INVNUM).is_enabled()

    def invoice_date(self):
        global current_time
        current_time = date.today().strftime('%m/%d/%Y')
        datefield = self.driver.find_element(By.XPATH,self.INVDATE)
        time.sleep(2)
        datefield.send_keys(Keys.CONTROL + 'a' + Keys.NULL, current_time,Keys.ENTER)
        time.sleep(5)

    def invoice_duedate(self):
        dom = float (''.join(["{}".format(randint(0, 9)) for num in range(0, 2)]))
        current_time = date.today()
        day = timedelta(days = dom)
        dudate = (current_time+day).strftime('%m/%d/%Y')
        datefield = self.driver.find_element(By.XPATH,self.INVDUEDATE)
        datefield.send_keys(Keys.CONTROL + 'a' + Keys.NULL, dudate, Keys.ENTER)
        time.sleep(2)
    def add_an_item(self):
        items = self.driver.find_elements(By.XPATH,self.ADDINVITEMS).click()
        self.driver.find_element(By.ID,self.ADDITEMNAME).send_keys(WORDS)
        n = 5
        self.driver.find_element(By.ID, self.ADDITEMCODE).send_keys(randinteger)
        self.driver.find_element(By.XPATH, self.ADDITEMUNITPRICEID).send_keys(randinteger)
        self.driver.find_element(By.XPATH,self.ADDITEMSAVEBUTTON).click()
        time.sleep(2)


    def Add_inv_items(self):
        taxdd = self.driver.find_elements(By.XPATH,self.TAXDD)
        taxdd[0].click()
        time.sleep(2)
        try:
            items = self.driver.find_elements(By.XPATH,self.ADDINVITEMS)
            print("this is the list of items",len(items))
            items[2].click()
        except:
            self.add_an_item()
    def Save_invoice(self):
        SaveINV = self.driver.find_element(By.XPATH,self.SAVEBTN)
        self.driver.execute_script("arguments[0].click()",SaveINV)
        time.sleep(5)

    def enter_references(self):
        self.driver.find_element(By.XPATH,self.REFERENCE).send_keys(WORDS)

    def add_item_description(self,desc):
        self.driver.find_element(By.XPATH,self.DESCRIPTION).clear()
        self.driver.find_element(By.XPATH,self.DESCRIPTION).send_keys(desc)

    def enter_quantity(self):
        global quantity
        self.randinteger = ''.join(["{}".format(randint(0, 9)) for num in range(0, 2)])
        quantity = int (self.randinteger)
        self.driver.find_element(By.XPATH, self.QUANTITY).clear()
        self.driver.find_element(By.XPATH,self.QUANTITY).send_keys(quantity)

    def enter_price(self):
        global amnt
        # # priceamnt = self.get_element_text(self.PRICE)
        # print("this is the price amount",priceamnt)
        # if priceamnt == 0.00:
        amnt = int (randinteger)
        self.driver.find_element(By.XPATH, self.PRICE).clear()
        self.driver.find_element(By.XPATH,self.PRICE).send_keys(amnt)
        # else:
        #     print("The amount is prefilled",priceamnt)

    def enter_discount(self):
        global disc
        self.randdisc = round(random.uniform(1.00, 99.99), 2)
        disc = int (self.randdisc)
        print(disc)
        self.driver.find_element(By.XPATH, self.DISCOUNT).clear()
        self.driver.find_element(By.XPATH,self.DISCOUNT).send_keys(disc)

    def select_tax(self,tcomp,trate):
        try:
            taxdd = self.driver.find_elements(By.XPATH,self.TAXDD)
            taxdd[1].click()
            time.sleep(5)
        except:
            taxdd = self.driver.find_elements(By.XPATH, self.TAXDD)
            taxdd[1].click()
            time.sleep(5)
        try:
            taxes = self.driver.find_elements(By.XPATH,self.TAXSELECT)
            print("This is the selected tax",taxes[2].text)
            taxes[2].click()
            global select_tax
            select_tax = taxes[2].text
        except:
            taxes = self.driver.find_elements(By.XPATH,self.TAXSELECT)
            taxes[0].click()
            self.enter_new_tax(tcomp,trate)

    def enter_new_tax(self,tcomp,trate):
        self.driver.find_element(By.ID,self.TAXRATENAME).send_keys(WORDS)
        self.driver.find_element(By.XPATH,self.TAXCOMP).send_keys(tcomp)
        self.driver.find_element(By.XPATH,self.TAXRATE, trate)
        self.Save_invoice()

    def invoice_amount(self):
        self.amount = self.driver.find_element(By.XPATH,self.AMOUNT)
        print(self.amount.text)

    def total_amount(self):
        # int (amnt)
        # int (quantity)
        amount = amnt * quantity
        print (amnt)
        print(quantity)
        print(amount)
        discount = (amount) * disc/100
        discounted_amount = amount - discount
        print(discounted_amount)
        tax1 =  str (select_tax)
        final_tax =  ''.join(x for x in tax1  if x.isdigit())
        ftax = int (final_tax)
        print(ftax)
        tax_percentage = discounted_amount * ftax/100
        # print(tax_percentage)
        final_total = tax_percentage + discounted_amount
        global totalamt
        totalamt = round(final_total,2)
        print(totalamt)
        time.sleep(10)

    def verify_total_amount(self):
        # amount = self.driver.find_elements(By.CLASS_NAME,self.INVAMOUNT)
        currency = " ".format(float(totalamt))
        print(currency)
        assert currency in self.driver.page_source

    def search_invoice(self):
        global INV_NUM
        INV_NUM = "INV-0000" + ''.join(["{}".format(randint(0, 9)) for num in range(0, 2)])
        print(INV_NUM)
        self.driver.find_element(By.XPATH,self.INVSEARCHFIELD).send_keys(INV_NUM + Keys.ENTER)
        time.sleep(5)

    def Verify_Searched_Invoice(self):
        try:
            INVOICE_NUMBER = self.driver.find_element(By.XPATH,"//a[normalize-space()='"+INV_NUM+"']")
            print(INVOICE_NUMBER.text)
            assert INVOICE_NUMBER.text == INV_NUM

        except:
            assert "No records found" in self.driver.page_source
            print("No Record found")
    def clickCSVIcon(self):
        self.driver.find_element(By.XPATH,self.CSVICON).click()

    def Download_Excelfile(self):
        time.sleep(5)
        download_dir = os.getcwd() + '\\TestData\\TestExcelsandPDFS\\'
        time.sleep(5)
        file_path = max([download_dir + '/' + f for f in os.listdir(download_dir)], key=os.path.getctime)
        file_name = os.path.basename(file_path)
        print(file_name)
        with open(download_dir + file_name, "rb") as f:
            reader = csv.reader(f)
            print(reader)
            for row in reader:
                print(row)

    def clickPDFIcon(self):
        self.driver.find_element(By.XPATH,self.PDFICON).click()
    def verify_pdffile(self):
        self.download_dir = os.getcwd() + '\\TestData\\TestExcelsandPDFS'
        time.sleep(5)
        print(self.download_dir)
        self.file_path = max([self.download_dir + '\\' + f for f in os.listdir(self.download_dir)])
        self.file_name = os.path.basename(self.file_path)
        print(self.file_name)
        self.pdf_file = open(self.download_dir + '\\' + self.file_name, 'rb')
        self.reader = PdfReader(self.pdf_file)
        self.pdf_text = ''
        for page in range(len(self.reader.pages)):
            self.pdf_text += self.reader.pages[page].extract_text()
            print(self.pdf_text)


    def download_oneinvoice(self):
        time.sleep(4)
        actionbtns =  self.driver.find_elements(By.XPATH,self.ACTIONBUTTON)
        for act in actionbtns:
            status = self.driver.find_elements(By.XPATH,self.STATUS)
            for stat in status:
                if stat.text == 'Open':
                    print(stat.text)
                    act.click()
                    self.driver.find_element(By.XPATH,self.DOWNLOADINVOICE)
                    time.sleep(5)
                    self.verify_pdffile()
                    break
            break


        time.sleep(5)

    def ALLtab(self):
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH,self.ALLTILE).click()
            time.sleep(6)
        except exceptions.StaleElementReferenceException as e:
            print(e)
        # self.driver.execute_script("arguments[0].click()", element)

    def Disputedtab(self):
        try:
            self.driver.find_element(By.XPATH,self.DISPUTEDTILE).click()
            time.sleep(3)
        except exceptions.StaleElementReferenceException as e:
            print(e)
        # self.driver.execute_script("arguments[0].click()", element)

    def OpentabINV(self):
        try:
            opentab = self.driver.find_elements(By.CLASS_NAME,self.OPENTILE)
            opentab[3].click()
            time.sleep(3)
        except exceptions.StaleElementReferenceException as e:
            print(e)

    time.sleep(10)
        # self.driver.execute_script("arguments[0].click()", element)
    def paging_50(self):
        paging = self.driver.find_element(By.XPATH, self.PAGING)
        self.driver.execute_script("arguments[0].click()", paging)
        self.driver.find_element(By.XPATH, self.FIFTYITEMS).click()
        time.sleep(5)

    def verify_numberof_invoices(self):
        try:
            self.paging_50()
            # paging = self.driver.find_element(By.XPATH, self.PAGING)
            # self.driver.execute_script("arguments[0].click()", paging)
            # self.driver.find_element(By.XPATH, self.FIFTYITEMS).click()
            # time.sleep(2)
            num_invoices = self.driver.find_elements(By.XPATH,self.ACTIONBUTTON)
            global num_total
            num_total = len(num_invoices)
            if num_total >= 50:
                    self.driver.find_element(By.XPATH, self.NEXTBTN).click()
                    print("Total number of invoices:", num_total)
            elif num_total <= 50:
                print("Total number of invoices:", num_total)
        except:
            print("there are 0 invoice present in this tab.")

    def disputed_invoices(self):
        self.verify_numberof_invoices()
        disputetag = self.driver.find_elements(By.XPATH,self.DISPUTETAG)
        print("this is the number of dispute invoices",len(disputetag))
        assert num_total == len(disputetag) ,"Dispute tags and invoices are not equal"


    def open_invoices(self):
        self.verify_numberof_invoices()
        Invoiceopen  = self.driver.find_elements(By.CLASS_NAME,self.OPENSTATUS)
        print("this is the number of open invoices",len(Invoiceopen))
        print("num_total count = ", num_total)
        assert len(Invoiceopen ) == num_total, "Open invoices donot match"


    def PaidtabINV(self):
        try:
            time.sleep(1)
            opentab = self.driver.find_elements(By.CLASS_NAME,self.OPENTILE)
            time.sleep(10)
            opentab[4].click()
            time.sleep(3)
        except exceptions.StaleElementReferenceException as e:
            print(e)

    def paid_invoices(self):
        self.verify_numberof_invoices()
        paid_invoice = self.driver.find_elements(By.CLASS_NAME,self.PAIDSTATUS)
        print("this is the number of open invoices",len(paid_invoice))
        assert len(paid_invoice) == num_total, "Paid invoices donot match"

    def PartiallyPaidtabINV(self):
        try:
            opentab = self.driver.find_elements(By.CLASS_NAME, self.OPENTILE)
            opentab[5].click()
            time.sleep(3)
        except exceptions.StaleElementReferenceException as e:
            print(e)

    def partially_paid_invoices(self):
        self.verify_numberof_invoices()
        partiallypaid_invoice = self.driver.find_elements(By.CLASS_NAME,self.PARTIALLYPAIDSTATUS)
        print("this is the number of open invoices",len(partiallypaid_invoice))
        assert len(partiallypaid_invoice) == num_total, "Partially Paid invoices donot match"


    def WaitingfofundsTab(self):
        try:
            opentab = self.driver.find_elements(By.CLASS_NAME, self.OPENTILE)
            opentab[7].click()
            time.sleep(3)
        except exceptions.StaleElementReferenceException as e:
            print(e)

    def waitingforfunds_invoices(self):
        self.verify_numberof_invoices()
        waitingforfunds_invoice = self.driver.find_elements(By.CLASS_NAME,self.WAITINGFORFUNDSTAB)
        print("this is the number of open invoices",len(waitingforfunds_invoice))
        print("num_total count = ", num_total)
        assert len(waitingforfunds_invoice) == num_total, "Partially Paid invoices donot match"


    def click_moreoptions(self):
        moreoption = WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located((By.XPATH,self.ACTIONBUTTON)))
        moreoption[0].click()

    def duplicate_invoice(self):
        INVNUMBER = self.driver.find_elements(By.CLASS_NAME, self.INVOICEANDCUSTOMER)
        print(INVNUMBER[0].text)
        AMOUNTBALANCE = self.driver.find_elements(By.CLASS_NAME, self.AMOUNT_BALANCE)
        print(AMOUNTBALANCE[0].text)
        self.click_moreoptions()
        dup = self.driver.find_element(By.XPATH,self.DUPLICATE)
        self.driver.execute_script("arguments[0].click()",dup)
        time.sleep(1)
        price = self.driver.find_element(By.XPATH, self.PRICE)
        print(price.text)
        self.Save_invoice()
        AMOUNTBALANCE = self.driver.find_elements(By.CLASS_NAME, self.AMOUNT_BALANCE)
        assert AMOUNTBALANCE[0].text == AMOUNTBALANCE[2].text, "Invoice is not duplicate"
        Invoiceopen = self.driver.find_elements(By.CLASS_NAME,self.OPENSTATUS)
        assert Invoiceopen[0].text == "Open"

    def delete_invoice(self):
        self.driver.find_element(By.XPATH,self.DELETE).click()
        self.driver.find_element(By.XPATH,self.CONFIRMATIONBTN).click()
        time.sleep(1)
        deletemsg = self.driver.find_element(By.XPATH,self.DELETEMSG)
        assert deletemsg.text == "Invoice deleted successfully.", "Pop up did not appear"

    def view_invoice(self):
        INVNUMBER = self.driver.find_elements(By.CLASS_NAME, self.INVOICEANDCUSTOMER)
        print(INVNUMBER[0].text)
        global INVM
        INVM = INVNUMBER[0].text
        AMOUNTBALANCE = self.driver.find_elements(By.CLASS_NAME, self.AMOUNT_BALANCE)
        print(AMOUNTBALANCE[0].text)
        self.AMNTBAL = AMOUNTBALANCE[0].text
        self.driver.find_element(By.XPATH,self.VIEW).click()
        time.sleep(4)


    def verify_invoice_Details(self):
            amount = self.driver.find_element(By.XPATH,self.INVAMOUNT)
            invnumber = self.driver.find_element(By.XPATH,self.INVNUMBER)
            print(amount.text)
            print(invnumber.text)
            # assert self.AMNTBAL == amount.text ,"Amount is not equal or invoice listings and details are not the same"
            # assert self.INVM == invnumber.text,"Invoice number does not match or invoice listings and details are not the same"

    def editinvoice(self):
        edit = self.driver.find_element(By.XPATH,self.INVOICEEDIT)
        edit.click()
        time.sleep(2)

    def Verify_Send_Email(self): # this is only downloading invoice.
        senderemail = self.driver.find_element(By.XPATH,self.EMAILADDRESS)
        print(senderemail.text)
        emailsend = self.driver.find_element(By.XPATH,self.EMAILSEND)
        self.driver.execute_script("arguments[0].click()",emailsend)
        time.sleep(1)
        sendlabel = self.driver.find_element(By.XPATH, self.EMAILSENDTOLABEL)
        print(sendlabel.text)
        assert senderemail.text == sendlabel.text,"sender email donot match"
        self.driver.find_element(By.XPATH,self.DOWNLOADINVOICEBTN).click()
        subject  = self.driver.find_element(By.ID,self.SUBJECT)
        subject.clear()
        subject.send_keys("This is a dummy invoice")
        self.body = self.driver.find_element(By.XPATH,self.EMAILBODY)
        print(self.body.text)
        global subjecttext
        subjecttext = subject.text
        time.sleep(5)
        self.download_dir2 = os.getcwd() + '\\TestData\\TestExcelsandPDFS\\'
        time.sleep(5)
        self.file_path2 = max([self.download_dir2 + '\\' + f for f in os.listdir(self.download_dir2)])
        self.file_name2 = os.path.basename(self.file_path2)
        print(self.file_name2)
        self.pdf_file2 = open(self.download_dir2 + '\\' + self.file_name2, 'rb')
        self.reader2 = PdfReader(self.pdf_file2)
        self.pdf_text2 = ''
        for page in range(len(self.reader2.pages)):
            self.pdf_text2 += self.reader2.pages[page].extract_text()
            print(self.pdf_text2)
    def send_email(self):
        self.driver.find_element(By.XPATH,self.CONFIRMATIONBTN).click()
        time.sleep(5)
        notif = self.driver.find_element(By.XPATH,self.EMAILSENT_NOTIF)
        slice = notif.text[2::]
        print(slice)
        assert slice in self.driver.page_source

    def verify_sent_email(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://outlook.office365.com/mail/inbox")
        driver.maximize_window()
        time.sleep(10)
        driver.find_element(By.NAME, self.yop_EMAILFIELD).send_keys("datasoft_autotest@hotmail.com")
        driver.find_element(By.NAME, self.yop_EMAILFIELD).send_keys(Keys.ENTER)
        time.sleep(4)
        driver.find_element(By.NAME,self.HOTPASS).send_keys("Cadency@123")
        driver.find_element(By.NAME,self.HOTPASS).send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element(By.ID,self.DONTYESBTN).click()
        time.sleep(3)
        driver.find_element(By.XPATH,self.JUNKMAIL).click()
        self.emaillist = driver.find_elements(By.CLASS_NAME,self.EMAILS)
        self.emaillist[0].click()


    def verify_edited_invoice(self):
        time.sleep(3)
        finaltotal = self.driver.find_element(By.XPATH,self.TOTALAMNT1)
        # finaltotal = total[3].find_elements(By.CLASS_NAME,self.TOTALAMNT1c1)
        # for ftotal in finaltotal:
        #     time.sleep(2)
        print(finaltotal.text)
        string = finaltotal.text
        pattern = r'[0-9,.]+'
        matches = re.findall(pattern, string)
        global result
        result = ''.join(matches)
        print("This is the final",result)
    def invoice_Edited_successfully(self):
        inv_det_total = self.driver.find_element(By.ID,self.INV_DETAIL_TOTAL)
        inv_det = inv_det_total.find_elements(By.TAG_NAME,self.INVTOTAL)
        global invoicetotal
        invoicetotal = inv_det[1].text
        if invoicetotal.startswith("$"):
            invoicetotal = invoicetotal[1:]
            famount = re.sub('[^0-9.]', '', invoicetotal)
            print(famount)
            print(totalamt)
    def record_payment_btn(self):
        self.driver.find_element(By.ID,self.RECORDPAYMENT).click()
        time.sleep(1)
    def fill_record_payments_form(self):
        self.driver.find_element(By.XPATH, self.AMOUNTRECIEVED).clear()
        self.driver.find_element(By.XPATH,self.AMOUNTRECIEVED).send_keys(randinteger)
        current_time = date.today().strftime('%m/%d/%Y')
        self.driver.find_element(By.XPATH,self.PAYMENTDATE).send_keys(Keys.CONTROL + 'a' + Keys.NULL, current_time,Keys.ENTER)
        self.driver.find_element(By.ID,self.PAYMENTMODEID).click()
        self.driver.find_element(By.XPATH,self.BANKTRANSFER).click()
        self.driver.find_element(By.ID, self.REFERENCENUMBERID).clear()
        self.driver.find_element(By.ID,self.REFERENCENUMBERID).send_keys(WORDS)
        self.driver.find_element(By.XPATH,self.ENTERNOTE).send_keys("This is a note")
        self.driver.find_element(By.XPATH,self.SAVEBTN).click()
        time.sleep(2)

    def record_full_payment_form(self):
        current_time = date.today().strftime('%m/%d/%Y')
        self.driver.find_element(By.XPATH, self.PAYMENTDATE).send_keys(Keys.CONTROL + 'a' + Keys.NULL, current_time,
                                                                       Keys.ENTER)
        self.driver.find_element(By.ID, self.PAYMENTMODEID).click()
        self.driver.find_element(By.XPATH, self.BANKTRANSFER).click()
        self.driver.find_element(By.ID, self.REFERENCENUMBERID).clear()
        self.driver.find_element(By.ID, self.REFERENCENUMBERID).send_keys(WORDS)
        self.driver.find_element(By.XPATH, self.ENTERNOTE).send_keys("This is a note")
        self.driver.find_element(By.XPATH, self.SAVEBTN).click()
        time.sleep(2)


    def verify_status_InvoiceDetail(self):
        try:
            Invoicepaid = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, self.INVDETAILPAIDSTATUS)))
            if Invoicepaid == True:
                assert Invoicepaid.text == 'Paid', "Full Amount has not been paid"
        except (NoSuchElementException, TimeoutException):
            try:
                Invoicepartialpaid = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, self.INVDETAILPARTIALPAIDSTATUS)))
                if Invoicepartialpaid == True:
                    assert Invoicepartialpaid.text == 'Partially Paid', "Full Amount has not been paid"
            except (NoSuchElementException, TimeoutException):
                try:
                    Invoicewff = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.CLASS_NAME, self.INVDETAILWFFSTATUS)))
                    if Invoicewff == True:
                        assert Invoicewff.text == 'Waiting For Funds', "Full Amount has not been paid"
                except (NoSuchElementException, TimeoutException):
                    pass
        finally:
            Invoiceopen = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, self.INVDETAILOPENSTATUS)))
            if Invoiceopen == True:
                assert Invoiceopen.text == 'Open', "Full Amount has not been paid"
            else:
                print("Error has occurred in invoice status")


    def verify_Thankyouemail_Contents(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://outlook.office365.com/mail/inbox")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.NAME, self.yop_EMAILFIELD).send_keys("datasoft_autotest@hotmail.com")
        driver.find_element(By.NAME, self.yop_EMAILFIELD).send_keys(Keys.ENTER)
        time.sleep(4)
        driver.find_element(By.NAME, self.HOTPASS).send_keys("Cadency@123")
        driver.find_element(By.NAME, self.HOTPASS).send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element(By.ID, self.DONTYESBTN).click()
        time.sleep(3)
        driver.find_element(By.XPATH, self.JUNKMAIL).click()
        time.sleep(2)
        self.emaillist = driver.find_elements(By.CLASS_NAME, self.EMAILS)
        print(len(self.emaillist))
        self.emaillist[0].click()
        time.sleep(10)
        driver.find_element(By.XPATH,self.ATTACHMENTS).click()
        driver.find_element(By.XPATH,self.DOWNLOADBTN).click()
        time.sleep(2)

    def click_reminder(self):
        sub = self.driver.find_element(By.XPATH,self.REMINDER)
        self.driver.execute_script("arguments[0].click()",sub)
    def Show_MaxCount_Inv(self):
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.Count_Footer).click()
            time.sleep(2)
            element_1= self.driver.find_element(By.XPATH, self.Show_50Invs)
            time.sleep(2)
            element_1.click()
            time.sleep(3)
        except exceptions.StaleElementReferenceException as e:
            print(e)

    def countRibbon_ALLtab(self):

        column_elements = self.driver.find_elements(By.XPATH, "//a[@class='p-element title-heading-1 text-primary-3']")
        odd_column_elements = [element for index, element in enumerate(column_elements) if index % 2 == 0]
        odd_columns_texts = [element.text for element in odd_column_elements]
        print("Odd Column Texts:", odd_columns_texts)
        length = len(odd_columns_texts)
        print("Length of Odd Column Texts:", length)

        # inv_details1 = self.driver.find_elements(By.XPATH, self.inv_num_details)
                  # time.sleep(5)
                  # count = len(inv_details1)
                  # time.sleep(5)
                  # print("Total count:", count)
                  # for element in inv_details1:
                  #  text = element.text
                  #  print("Element text:", text)
                  #  time.sleep(5)


                # self.Nextbutton_footer = "//span[@class='p-paginator-icon pi pi-angle-right']"
                #
                # for _ in range(5):
                #     try:
                #         susu = self.driver.find_element(By.XPATH, self.Nextbutton_footer)
                #         susu.click()
                #         time.sleep(3)
                #     except NoSuchElementException:
                #         break


    # def countRibbon_ALLtab(self):
    #
    #
    #                   # disabled_footerbutton= self.driver.find_element(By.XPATH, self.diabledbut)
    #                 self.Nextbutton_footer = "//span[@class='p-paginator-icon pi pi-angle-right']"
    #                 susu = self.driver.find_element(By.XPATH, self.Nextbutton_footer)
    #                 time.sleep(4)
    #                 # disabled_footerbutton = self.driver.find_element(By.XPATH, self.diabledbut)
    #                 time.sleep(4)
    #
    #
    #                 while susu== True:
    #                     time.sleep(4)
    #                     susu = self.driver.find_element(By.XPATH, self.Nextbutton_footer)
    #                     time.sleep(4)
    #                     susu.click()
    #                     time.sleep(3)








                    # element_found= False
                    # NextButton_foot = None
                    #
                    #
                    # while not element_found:
                    #     try:
                    #
                    #         exNtButton_foot = self.driver.find_element(By.XPATH, self.Nextbutton_footer)
                    #         element_found= True
                    #
                    #     except:
                    #         time.sleep(4)
                    # if NextButton_foot is not None:
                    #
                    #         NextButton_foot.click()
                    #         time.sleep(4)






         # global num_total
         # try:
         #    randomvariable=self.driver.find_elements(By.XPATH, self.count_ALL_Ribn)
         #    get_countdigits = int(randomvariable[0].text)
         #    print(get_countdigits)
         #
         #
         #    count=0
         #
         #    while get_countdigits>0 :
         #        num_invoices_on1page = self.driver.find_elements(By.XPATH, self.ACTIONBUTTON)
         #        # global num_total
         #        num_total = len(num_invoices_on1page)
         #        get_countdigits= get_countdigits-num_total
         #
         #        print("hiiiii", num_total)
         #
         #        count= count+num_total #50 in count
         #
         #
         #
         #        while count == num_total:  #get_countdigits == count:
         #
         #              self.Nextbut_footer = "//button[@class='p-ripple p-element p-paginator-next p-paginator-element p-link']"

         #              time.sleep(3)
         #              NextButton_footer= self.driver.find_element(By.XPATH,self.Nextbut_footer)
         #              time.sleep(3)
         #              NextButton_footer.click()
         #              num_invoices_on1page = self.driver.find_elements(By.XPATH, self.ACTIONBUTTON)
         #              # global num_total
         #              num_total = len(num_invoices_on1page)
         #              print("under iffff 2nd page", num_total)
         #
         #              time.sleep(3)
         #              count = count + num_total  # 50 in count
         #              # count += num_total
         #              print("total", count)
         #        break
         #===================================================
        #
        #     counter=0
        #
        #
        #     while counter < get_countdigits:
        #         num_invoices_on1page = self.driver.find_elements(By.XPATH, self.ACTIONBUTTON)
        #         num_total = len(num_invoices_on1page)
        #         print(num_total)
        #
        #         assert num_total == min(50, get_countdigits-counter)
        #         counter += num_total
        #         self.Nextbut_footer = "//button[@class='p-ripple p-element p-paginator-next p-paginator-element p-link']"
        #         NextButton_footer= self.driver.find_element(By.XPATH,self.Nextbut_footer)
        #         NextButton_footer.click()
        #
        #         assert counter == get_countdigits
        #
        #
        #     # if num_total < get_countdigits:
        #     #     self.Nextbutton_footer = "//span[@class='p-paginator-icon pi pi-angle-right']"
        #     # else:
        #     #     print('gggg')
        #
        #
        #     # self.Nextbutton_footer = "//span[@class='p-paginator-icon pi pi-angle-right']"
        #     # counter=0
        #
        #
        #
        #
         # except exceptions.StaleElementReferenceException as e:
         #     print(e)



    # def Condition_NextButton(self):


    def click_on_dispute(self):
        self.driver.find_element(By.XPATH,self.DISPUTE_ICON).click()
    def verify_custom_invoice_num(self):
        global invnumber
        invnumber = self.driver.find_element(By.XPATH, self.INVNUMBER)
        print(invnumber.text)
        global customname
        customname = self.driver.find_element(By.XPATH,self.CUSTOMERNAME)
        print(customname.text)

    def verify_invoice_number(self):
       time.sleep(5)
       inv =  self.driver.find_element(By.XPATH,self.DISP_INV_NUM)
       value = self.driver.execute_script("return arguments[0].value;", inv)
       print("This is invoice number on dispute form",value)
       print("This is invoice number on invoice detail",invnumber.text)
       assert value == invnumber.text, "Invoice number donot match"

    def verify_Customer_Name(self):
        customer = self.driver.find_element(By.ID,self.CUSTOM_NAME)
        value = self.driver.execute_script("return arguments[0].value;",customer)
        assert value == customname.text,"Customer Name donot match"

    def select_reason(self):
        reasondd = self.driver.find_elements(By.XPATH,self.ADDITEMTYPEDD)
        reasondd[1].click()
        self.driver.find_element(By.XPATH,self.REASON).click()

    def add_disputeamount(self):
        self.driver.find_element(By.ID, self.DISPUTEAMOUNT).clear()
        self.driver.find_element(By.ID,self.DISPUTEAMOUNT).send_keys(randinteger)

    def add_a_note(self):
        self.driver.find_element(By.ID,self.note).send_keys(WORDS)

    def search_customer(self,Name):
        self.driver.find_element(By.XPATH, self.INVSEARCHFIELD).send_keys(Name + Keys.ENTER)
        global searchname
        searchname = Name
        time.sleep(4)

    def verify_searched_name(self):
        global all
        INV_DET = self.driver.find_elements(By.CLASS_NAME,self.INVOICE_DETAILS)
        all_names = []
        for all1 in INV_DET:
            try:
                CUSTNAME = all1.find_elements(By.CLASS_NAME, self.INV_CUSTOMER_NAME)
                for all in CUSTNAME:
                    all_names.append(all.text)
            except StaleElementReferenceException:
                # Handle the exception as per your requirements
                print("Stale element reference encountered.")
        searchedname = searchname
        for name in all_names:
            assert name == searchedname, f"The name '{name}' does not match the target name '{searchedname}'"
            print(f"All names in the list match the target name: {searchedname}")

    def export_invoice(self):
        sub = self.driver.find_element(By.XPATH, self.EXPORT_INVOICE)
        self.driver.execute_script("arguments[0].click()", sub)
        self.verify_pdffile()
        # pdf_file_path = os.getcwd() + '\\TestData\\TestExcelsandPDFS'
        # with open(pdf_file_path, 'rb') as file:
        #     pdf_reader = PyPDF2.PdfReader(file)
        #     page = pdf_reader.getPage(0)  # Assuming you want to read the first page
        #     text_from_pdf = page.extract_text()
        # expected_columns_headers = ["Invoice Number", "Invoice to","Total"]
        # elements = []
        # for column_header in expected_columns_headers:
        #     try:
        #         element = self.driver.find_element(By.XPATH,
        #                                       f'//td[contains(text(), "{column_header}")]')  # Modify the locator as per your HTML structure
        #         elements.append(element)
        #     except NoSuchElementException:
        #         pass
        #

