import os
import time
import random
import string
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Constants.URLS import TestData
import unittest

from Elements.Customer_elements import customerelements



class CustomerPages(customerelements):

    def __init__(self, driver):
        super().__init__(driver)

    def hover_hamburger(self):
        self.wait(2)
        self.move_to_element(self.hamburger_icon)
    def Go_to_customerTab(self):
        self.click_element(self.CUSTOMERANDRECEIVABLETAB)
        self.click_using_js(self.CUSTOMERTAB)
        self.wait(5)

    def customer_number(self):
        self.wait(3)
        custom = self.driver.find_elements(By.CLASS_NAME, self.CUSTOMERGRID)
        print("This is the number of customers", len(custom))


    def click_addbutton(self):
        try:
            self.click_element(self.ADDFIRSTCUSTOMER)
        except:
            self.click_using_js(self.ADDCUSTOMER)

    def verify_customerform(self):
        self.verify_element_display(self.TITLE_ADD_CUSTOMER)
    def customer_email(self):
        # try:
        #     self.verify_element_enable(self.CUSTOMERNUMBER)
        # except:
        # if self.result_str == "": This needs to change when the customer number will be auto generated
            self.result_str = "".join((random.choice(string.ascii_letters) for i in range(10))) + "@yopmail.com"
            print(self.result_str)
            self.input_element(self.EMAIL,self.result_str)
            # global email_address
            # email_address = self.result_str
            # print(email_address)

    def enter_customerDetails(self, cus_dis_name,fname,lname,phno,web,ccemail):
        self.input_element(self.CUSTOMER_DISPLAY_NAME, cus_dis_name)
        self.input_element(self.FIRSTNAME, fname)
        self.input_element(self.LASTNAME, lname)
        self.input_element(self.PHONE, phno)
        global phonenum
        phonenum = phno
        self.input_element(self.WEBSITE, web)
        self.input_element(self.CCEMAIL, ccemail)

    def select_customer_currency(self):
        self.click_element(self.CURRENCY_FIELD)
        self.click_using_js(self.CURRENCY_SELECT)
    def verify_currency_added(self):
        self.get_element_text(self.CURRENCY_FIELD)
        self.verify_element_disabled(self.CURRENCY_FIELD)
        # self.verify_element_disabled(self.CURRENCY_FIELD)


    def upload_logo(self):
        try:
            self.click_element(self.SHOWATTACH)
            path = os.getcwd()
            element = self.driver.find_element(By.XPATH,self.LOGOUPLOAD)
            self.driver.execute_script("arguments[0].style.display = 'block';", element)
            path3 = os.path.abspath(path + r'\\TestData\\Picture\\new2.jpg')
            element.send_keys(path3)
            time.sleep(3)
        except:
            self.click_element(self.REMPICTURE)
            path = os.getcwd()
            element = self.driver.find_element(By.XPATH, self.LOGOUPLOAD)
            self.driver.execute_script("arguments[0].style.display = 'block';", element)
            path3 = os.path.abspath(path + r'\\TestData\\Picture\\new2.jpg')
            element.send_keys(path3)
            time.sleep(3)


    def enter_address(self, st1, st2, postcode):
        self.click_element(self.ADDRESSDETAILS)
        self.input_element(self.STREETLINE1,st1)
        self.input_element(self.STREETLINE2, st2)
        self.input_element(self.POSTALCODE, postcode)
        self.click_element(self.COUNTRY_FIELD)
        self.click_using_js(self.COUNTRY_PAK)
        self.wait(2)
        self.click_element(self.STATEFIELD)
        self.click_using_js(self.STATEFIELD_SINDH)
        self.wait(3)
        self.click_element(self.CITYID)
        self.wait(2)
        self.click_using_js(self.CITYKARACHI)
        self.wait(2)

    def click_save(self):
        self.click_element(self.SAVEBUTTON)
        self.wait(5)

    def customer_alreadypresent(self):
        self.wait(2)
        self.get_element_text(self.CUSTOMERNUMBER_VIEW)

    def verify_new_user_successfully_added(self):
        self.customer_number()
       # self.wait(5)
       # cust_email = []
       # cust_email =  self.driver.find_elements(By.CLASS_NAME,self.CUSTOMER_LIST_EMAIL)
       # # for value in cust_email:
       # print(cust_email[2].text)
       # self.assert_equal(cust_email[2].text,email_address,"New customer is not added")

    def updated_customerdata(self):
        self.wait(8)
        custom_ph = self.get_element_text(self.CUSTOMERPHONE_VIEW)
        # custom_email = self.get_element_text(self.CUSTOMEREMAIL_VIEW)
        print(custom_ph)
        # print(custom_email)
        print(phonenum)
        self.assert_equal(phonenum,custom_ph,"Phone number cannot be viewed")
        # self.assert_equal(emailadd,custom_email,"Email Cannot be viewed")
    def edit_Customer(self):
        self.wait(15)
        self.click_element(self.THREEDOTSBUTTON)
        time.sleep(3)
        self.click_element(self.EDITCUSTOMER)
        self.wait(2)
        self.get_web_element(self.EDITCUSTOMERTEXT)

    def verify_customers_present(self):
        self.get_web_element(self.CUSTOMER_LIST)

    def select_filter(self):
        self.click_using_js(self.FILTERBUTTON)
        self.wait(5)

    def select_country(self):
        self.click_element(self.SELECTCOUNTRY)
        global countryname
        # self.driver.find_element(By.XPATH,"//li[@aria-label='Pakistan']").click()
        countryname = self.driver.find_elements(By.CLASS_NAME,self.SELECTCOUNTRYIES)
        randomcountry = random.choice(countryname)
        randomcountry.click()
        print(randomcountry.text)


    def click_applybutton(self):
        self.click_element(self.FILTERAPPLY)
        self.wait(3)

    def verify_customers_of_selected_countries(self):
        # countrylist = []
            countrylist = self.driver.find_elements(By.CLASS_NAME,self.VIEWCOUNTRY)
            print("Number of customer shown is", len(countrylist))
            for listcount in countrylist:
                print(listcount.text)


       # countrylist =  self.driver.find_element(By.XPATH,self.VIEWCOUNTRY)
       # print(countrylist.text)
       # print(countryname)


    def handle_toggle(self):
        try:
            self.click_element(self.CUSTOMER_TOGGLE_INACTIVE)
        except:
            self.get_web_element(self.CUSTOMER_TOGGLE_ACTIVE)
            print("Customer already active")

    def click_view(self):
        self.click_element(self.THREEDOTSBUTTON)
        self.click_element(self.VIEWCUSTOMER)

    def verify_invoice_tiles(self):
        self.get_web_element(self.INVOICETILES)

    def verify_openInvoices(self):
        self.click_using_js(self.OPENINVOICES)
        # self.click_using_js(self.CLOSEDINVOICES)
        time.sleep(4)
        try:
            # inv = self.driver.find_elements(By.CLASS_NAME,"max-width-300 ng-star-inserted")
            # self.driver.find_element(By.XPATH,"//body[1]/cadency-root[1]/cadency-features[1]/div[1]/div[1]/div[1]/div[1]/cadency-customer-details[1]/div[2]/div[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[2]/div[1]/cadency-master-grid[1]/div[1]/p-table[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/div[1]/div[1]")
            # print(len(self.driver.find_element(By.XPATH,"//body[1]/cadency-root[1]/cadency-features[1]/div[1]/div[1]/div[1]/div[1]/cadency-customer-details[1]/div[2]/div[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[2]/div[1]/cadency-master-grid[1]/div[1]/p-table[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/div[1]/div[1]")))
            invoicenum = self.driver.find_elements(By.CLASS_NAME,"max-width-300.status-column.ng-star-inserted")
            print("These are all the invoices with open status",len(invoicenum))
        except:
            assert "No records found" in self.driver.page_source

    def search_customer(self,name):
        self.input_element(self.SEARCHCUSTOMER,name)
        try:
            customername = self.driver.find_element(By.XPATH,"//a[normalize-space()='"+name+"']")
            print(customername.text)
            self.assert_equal (name,customername.text,"Searched customer found")
            print("Searched Customer Found")
        except:
            assert " No records found " in self.driver.page_source
            print("Searched Customer not Found")

    def apply_invoice_filter(self):
        self.click_element(self.INVOICESTATUSFILTER)
        self.click_element(self.CURRENT_STATUS)
    def apply_customer_Filter(self):
        self.click_element(self.CUSTOMERSTATUSFILTER)
        self.click_element(self.STATUSACTIVE)

    def vefify_Current_status_filter(self):
        try:
            self.get_web_element(self.CURRENTSTATUSONINVOICE)
        except:
            assert " No records found " in self.driver.page_source
            print("No Record Found")
