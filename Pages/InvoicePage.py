import os
from random import *
import time
from datetime import date, datetime, timedelta
import random
import string
from PyPDF2 import PdfReader
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Constants.URLS import TestData
# from Elements.InvoiceElements import invoiceelements
# from Elements.Customer_elements import customerelements
from selenium.common import exceptions
import csv
import PyPDF2

WORDS = "".join((random.choice(string.ascii_letters) for i in range(10)))
randinteger = ''.join(["{}".format(randint(0, 9)) for num in range(0, 6)])
class InvoicePage():

    def __init__(self, driver):
        self.driver = driver
        # self.invnum = "//a[normalize-space()='" + INV_NUM + "']"
        self.CUSTOMERANDRECEIVABLETAB = "//p[normalize-space()='Customers & Receivables']"
        self.INVOICETAB =  "//p[normalize-space()='Invoices']"
        self.ADDINVOICEBTN = "//button[@class='p-element p-button-primary button-with-icon btn-150 p-button p-component']"
        self.CUSTNAMEDD =  "(//span[@class='p-button-icon pi pi-chevron-down'])[1]"
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
        self.INVAMOUNT = "grid-footer-text"
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
        self.DUPLICATE = "//a[normalize-space()='Duplicate']"
        self.INVOICEANDCUSTOMER = "p-element.title-heading-1.text-primary-3"
        self.AMOUNT_BALANCE = "max-width-300.amount-column.font-bold.ng-star-inserted"
        self.DELETE = "//a[normalize-space()='Delete']"
        self.DELETEMSG = "//div[@aria-label='Invoice deleted successfully.']"

    def ClickOnInvoiceTab(self):
        CART = self.driver.find_element(By.XPATH,self.CUSTOMERANDRECEIVABLETAB)
        self.driver.execute_script("arguments[0].click()",CART)
        INVT= self.driver.find_element(By.XPATH,self.INVOICETAB)
        self.driver.execute_script("arguments[0].click()", INVT)
        time.sleep(20)

    def ClickOnAddButton(self):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH,self.ADDINVOICEBTN)))
        # self.driver.find_element(By.XPATH,self.ADDINVOICEBTN).click()
        self.driver.execute_script("arguments[0].click()",element)
    def open_customer_selection_dd(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.CUSTNAMEDD).click()

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
        taxdd[1].click()
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
        taxdd = self.driver.find_elements(By.XPATH,self.TAXDD)
        taxdd[2].click()
        time.sleep(5)
        try:
            taxes = self.driver.find_elements(By.XPATH,self.TAXSELECT)
            print("This is the selected tax",taxes[1].text)
            taxes[1].click()
            global select_tax
            select_tax = taxes[1].text
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
        totalamt = final_total
        print(final_total)
        time.sleep(10)

    def verify_total_amount(self):
        amount = self.driver.find_elements(By.CLASS_NAME,self.INVAMOUNT)
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
        time.sleep(4)
        time.sleep(5)
        with open(download_dir + file_name, "r") as f:
            reader = csv.reader(f)
            print(reader)
            for row in reader:
                print(row)

    def clickPDFIcon(self):
        self.driver.find_element(By.XPATH,self.PDFICON).click()
    def verify_pdffile(self):
        download_dir = os.getcwd() + '\\TestData\\TestExcelsandPDFS\\'
        time.sleep(5)
        file_path = max([download_dir + '\\' + f for f in os.listdir(download_dir)])
        file_name = os.path.basename(file_path)
        print(file_name)
        pdf_file = open(download_dir + '\\' + file_name, 'rb')
        reader = PdfReader(pdf_file)
        number_of_pages = len(reader.pages)
        page = reader.pages[0]
        text = page.extract_text()
        print(text.encode('utf-8'))


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
            self.driver.find_element(By.XPATH,self.ALLTILE).click()
            time.sleep(3)
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

    def verify_numberof_invoices(self):
        # try:
        paging = self.driver.find_element(By.XPATH, self.PAGING)
        self.driver.execute_script("arguments[0].click()", paging)
        self.driver.find_element(By.XPATH, self.FIFTYITEMS).click()
        time.sleep(2)
        num_invoices = self.driver.find_elements(By.XPATH,self.ACTIONBUTTON)
        global num_total
        num_total = len(num_invoices)
        if num_total == 50:
                self.driver.find_element(By.XPATH, self.NEXTBTN).click()
                print("Total number of invoices:", num_total)
        elif num_total <= 50:
            print("Total number of invoices:", num_total)

    def disputed_invoices(self):
        self.verify_numberof_invoices()
        disputetag = self.driver.find_elements(By.XPATH,self.DISPUTETAG)
        print("this is the number of dispute invoices",len(disputetag))
        assert num_total == len(disputetag) ,"Dispute tags and invoices are not equal"


    def open_invoices(self):
        self.verify_numberof_invoices()
        Invoiceopen  = self.driver.find_elements(By.CLASS_NAME,self.OPENSTATUS)
        print("this is the number of open invoices",len(Invoiceopen))
        assert len(Invoiceopen ) == num_total, "Open invoices donot match"


    def PaidtabINV(self):
        try:
            opentab = self.driver.find_elements(By.CLASS_NAME,self.OPENTILE)
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
            opentab[6].click()
            time.sleep(3)
        except exceptions.StaleElementReferenceException as e:
            print(e)

    def waitingforfunds_invoices(self):
        self.verify_numberof_invoices()
        waitingforfunds_invoice = self.driver.find_elements(By.CLASS_NAME,self.WAITINGFORFUNDSTAB)
        print("this is the number of open invoices",len(waitingforfunds_invoice))
        assert len(waitingforfunds_invoice) == num_total, "Partially Paid invoices donot match"
    def INV_DETAILS(self):
        global INVNUMBER, AMOUNTBALANCE

    def click_moreoptions(self):
        self.INV_DETAILS()
        moreoption = self.driver.find_elements(By.XPATH,self.ACTIONBUTTON)
        moreoption[1].click()

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
        time.sleep(1
                   )
        deletemsg = self.driver.find_element(By.XPATH,self.DELETEMSG)
        assert deletemsg.text == "Invoice deleted successfully.", "Pop up did not appear"










