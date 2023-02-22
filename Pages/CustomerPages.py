import os
import time
import random
import string
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Constants.URLS import TestData
import unittest



class CustomerPages(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.hamburger_icon = "//div[@class='tree-container ng-star-inserted']"
        self.CUSTOMERANDRECEIVABLETAB = "//p[normalize-space()='Customers & Receivables']"
        self.CUSTOMERTAB = "//p[normalize-space()='Customers']"
        self.CUSTOMERNAME = "title-heading-3 text-primary-3"
        self.NOCUSTOMERFOUND = "//div[@class='title-heading-5']"
        self.ADDFIRSTCUSTOMER = "//button[@class='p-element p-button-primary button-with-icon btn-120 p-button p-component']"
        self.ADDCUSTOMER = "(//button[@class='p-element p-button-primary button-with-icon btn-150 p-button p-component ng-star-inserted'])[1]"
        self.TITLE_ADD_CUSTOMER = "//span[normalize-space()='Add Customer']"
        self. CUSTOMERNUMBER = "//input[@placeholder='Enter customer number']"
        self.CUSTOMER_DISPLAY_NAME = "customerDisplayName"
        self.FIRSTNAME = "firstName"
        self.LASTNAME = "lastName"
        self.PHONE = "//input[@id='phone']"
        self.EMAIL = "email"
        self.CURRENCY = "currencyId"
        self.WEBSITE = "website"
        self.CCEMAIL = "ccEmail"
        self.CUSTOMER_TOGGLE_ACTIVE = "//div[@class='p-inputswitch p-component p-inputswitch-checked']"
        self.CUSTOMER_TOGGLE_INACTIVE = "//div[@class='p-inputswitch p-component']"
        self.SHOWATTACH = "//a[normalize-space()='+ Show/Add attachment']"
        self.LOGOUPLOAD = "//input[@type='file']"
        self.SAVEBUTTON = "//button[@type='submit']"
        self.UPLOADED_IMAGE = "//button[@class='p-element p-button p-component p-button-icon-only']"
        self.CURRENCY_FIELD = "currencyId"
        self.CURRENCY_SELECT = "//div[@class='inline-flex'][normalize-space()='USD']"
        self.ADDRESSDETAILS = "//span[normalize-space()='Address Details']"
        self.STREETLINE1 = "line1"
        self.STREETLINE2 = "line2"
        self.POSTALCODE = "postalCode"
        self.COUNTRY_FIELD = "countryId"
        self.COUNTRY_PAK = "//div[contains(text(),'Pakistan')]"
        self.STATEFIELD = "/html/body/cadency-root/cadency-features/div/div/div/div/cadency-customers-list/div/cadency-add-customer/div/form/p-sidebar/div/div[2]/div/div[2]/p-tabview/div/div[2]/p-tabpanel[2]/div/form/div/div[4]/div/p-dropdown/div/div[2]"
        self.STATEFIELD_SINDH = "//li[@aria-label='Sindh']"
        self.CITYID = "/html/body/cadency-root/cadency-features/div/div/div/div/cadency-customers-list/div/cadency-add-customer/div/form/p-sidebar/div/div[2]/div/div[2]/p-tabview/div/div[2]/p-tabpanel[2]/div/form/div/div[5]/div/p-dropdown/div/div[2]"
        self.CITYKARACHI = "//li[@aria-label='Karachi']"
        self.CUSTOMERNUMBER_VIEW = "//*[@id='pr_id_2-table']/tbody/tr[1]/td[2]/div/span"
        self.CUSTOMER_LIST_EMAIL = "paragraph-text-4.wrap-text-all"
        self.THREEDOTSBUTTON = "more-icon"
        self.EDITCUSTOMER = "//a[normalize-space()='Edit']"
        self.EDITCUSTOMERTEXT = "//span[normalize-space()='Edit Customer']"
        self.CUSTOMERPHONE_VIEW = '/html/body/cadency-root/cadency-features/div/div/div/div/cadency-customers-list/div/div/div[2]/p-table/div/div[2]/table/tbody/tr[1]/td[4]/div/div[1]/span'
        self.CUSTOMEREMAIL_VIEW = '/html/body/cadency-root/cadency-features/div/div/div/div/cadency-customers-list/div/div[2]/p-table/div/div[2]/table/tbody/tr[1]/td[4]/div/div[2]/span'
        self.CUSTOMER_LIST = "//tbody"
        self.FILTERBUTTON = "//button[@class='p-element p-button-secondary filter-btn-count button-with-icon btn-150 p-button p-component']"
        self.SELECTCOUNTRY = "//p-dropdown[@placeholder='Select country']"
        self.SELECTCOUNTRYIES = "p-ripple.p-element.p-dropdown-item"
        self.SELECTINVOICE = "//span[@class='ng-tns-c43-48 p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"
        self.SELECTCURRENT = "//span[normalize-space()='Current']"
        self.SELECTCUSTOMSTATUS = "//span[@class='ng-tns-c43-49 p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"
        self.SELECTACTIVE = "//span[normalize-space()='Active']"
        self.FILTERAPPLY = "//button[@class='p-element p-button-primary button-with-icon btn-100 p-button p-component']"
        self.VIEWCOUNTRY = 'title-heading-4.text-secondary-1.wrap-text-all.no-break-word'
        self.no_record_text = "//td[normalize-space()='No records found']"
        self.VIEWCUSTOMER = "//a[normalize-space()='View']"
        self.INVOICETILES = "//ul[@role='tablist']"
        self.OPENINVOICES = "//li[@class='p-highlight ng-star-inserted']"
        self.INVOICEWFWSTAT = "status-container.status-orange3.ng-star-inserted"
        self.INVOICEPAIDSTATUS = "status-container.status-green.ng-star-inserted"
        self.INVOPENSTAT = "status-container.status-blue.ng-star-inserted"
        self.CLOSEDINVOICES = "p-tabpanel-1-label"
        self.PAYMENTINVOICES = "p-tabpanel-2-label"
        self.INVOICESLIST = "max-width-300.ng-star-inserted"
        self.STATUSTILE = "status-container status-orange3 ng-star-inserted"
        self.CUSTOMERGRID = "user-profile-box.ng-star-inserted"
        self.REMPICTURE = "//button[@class='p-element p-button-info p-1 lg:p-2 p-button-secondary delete-custom-uploader p-button p-component']"
        self.SEARCHCUSTOMER = "searchText"
        self.INVOICESTATUSFILTER = "//p-dropdown[@placeholder='Select invoice status']"
        self.CURRENT_STATUS = "//li[@aria-label='Current']"
        self.CUSTOMERSTATUSFILTER = "//p-dropdown[@placeholder='Select customer status']"
        self.STATUSACTIVE = "//span[normalize-space()='Active']"
        self.CURRENTSTATUSONINVOICE = "//div[@class='status-container status-green']"
        self.PAGINGDD = "//div[@aria-label='dropdown trigger']"
        self.FIFTYITEMS = "p-highlighted-option"

    def hover_hamburger(self):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.hamburger_icon)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
    def Go_to_customerTab(self):
        self.driver.find_element(By.XPATH,self.CUSTOMERANDRECEIVABLETAB).click()
        customertab = self.driver.find_element(By.XPATH,self.CUSTOMERTAB)
        self.driver.execute_script("arguments[0].click()",customertab)
        time.sleep(5)

    def customer_number(self):
        time.sleep(5)
        element = self.driver.find_elements(By.CLASS_NAME,self.CUSTOMERGRID)
        print("This is the number of customers", len(element))


    def click_addbutton(self):
        try:
            time.sleep(10)
            self.driver.find_element(By.XPATH,self.ADDFIRSTCUSTOMER).click()
        except:
            addcustom = self.driver.find_element(By.XPATH,self.ADDCUSTOMER)
            self.driver.execute_script("arguments[0].click()",addcustom)

    def verify_customerform(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.TITLE_ADD_CUSTOMER).is_displayed()
    def customer_email(self):
        # try:
        #     self.verify_element_enable(self.CUSTOMERNUMBER)
        # except:
        # if self.result_str == "": This needs to change when the customer number will be auto generated
            self.result_str = "".join((random.choice(string.ascii_letters) for i in range(10))) + "@yopmail.com"
            print(self.result_str)
            self.driver.find_element(By.ID,self.EMAIL).send_keys(self.result_str)
            # global email_address
            # email_address = self.result_str
            # print(email_address)

    def enter_customerDetails(self, cus_dis_name,fname,lname,phno,web,ccemail):

        self.driver.find_element(By.ID, self.CUSTOMER_DISPLAY_NAME).clear()
        self.driver.find_element(By.ID, self.CUSTOMER_DISPLAY_NAME).send_keys(cus_dis_name)
        self.driver.find_element(By.ID, self.FIRSTNAME).clear()
        self.driver.find_element(By.ID, self.FIRSTNAME).send_keys(fname)
        self.driver.find_element(By.ID, self.LASTNAME).clear()
        self.driver.find_element(By.ID, self.LASTNAME).send_keys(lname)
        self.driver.find_element(By.XPATH, self.PHONE).clear()
        self.driver.find_element(By.XPATH, self.PHONE).send_keys(phno)
        global phonenum
        phonenum = phno
        self.driver.find_element(By.ID, self.WEBSITE).clear()
        self.driver.find_element(By.ID, self.WEBSITE).send_keys(web)
        self.driver.find_element(By.ID, self.CCEMAIL).clear()
        self.driver.find_element(By.ID, self.CCEMAIL).send_keys(ccemail)

    def select_customer_currency(self):
        self.driver.find_element(By.ID, self.CURRENCY_FIELD).click()
        curr_select = self.driver.find_element(By.XPATH,self.CURRENCY_SELECT)
        self.driver.execute_script("arguments[0].click()",curr_select)

    def verify_currency_added(self):
        curr_field = self.driver.find_element(By.ID,self.CURRENCY_FIELD)
        return curr_field.is_enabled()
        # self.verify_element_disabled(self.CURRENCY_FIELD)


    def upload_logo(self):
        try:
            self.driver.find_element(By.XPATH,self.SHOWATTACH)
            path = os.getcwd()
            element = self.driver.find_element(By.XPATH,self.LOGOUPLOAD)
            self.driver.execute_script("arguments[0].style.display = 'block';", element)
            path3 = os.path.abspath(path + r'\\TestData\\Picture\\new2.jpg')
            element.send_keys(path3)
            time.sleep(3)
        except:
            self.driver.find_element(By.XPATH,self.REMPICTURE)
            path = os.getcwd()
            element = self.driver.find_element(By.XPATH,self.LOGOUPLOAD)
            self.driver.execute_script("arguments[0].style.display = 'block';", element)
            path3 = os.path.abspath(path + r'\\TestData\\Picture\\new2.jpg')
            element.send_keys(path3)
            time.sleep(3)


    def enter_address(self, st1, st2, postcode):
        self.driver.find_element(By.XPATH,self.ADDRESSDETAILS).click()
        self.driver.find_element(By.ID, self.STREETLINE1).send_keys(st1)
        self.driver.find_element(By.ID, self.STREETLINE2).send_keys(st2)
        self.driver.find_element(By.ID, self.POSTALCODE).send_keys(postcode)
        self.driver.find_element(By.ID,self.COUNTRY_FIELD).click()
        element = self.driver.find_element(By.XPATH, self.COUNTRY_PAK)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.STATEFIELD).click()
        time.sleep(2)
        element = self.driver.find_element(By.XPATH, self.STATEFIELD_SINDH)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.CITYID).click()
        time.sleep(2)
        element = self.driver.find_element(By.XPATH, self.CITYKARACHI)
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(2)

    def click_save(self):
        self.driver.find_element(By.XPATH,self.SAVEBUTTON).click()
        time.sleep(5)

    def customer_alreadypresent(self):
        time.sleep(2)
        cust_numb = self.driver.find_element(By.XPATH,self.CUSTOMERNUMBER_VIEW)
        return cust_numb.text

    def verify_new_user_successfully_added(self):
        self.customer_number()
       # time.sleep(5)
       # cust_email = []
       # cust_email =  self.driver.find_elementsself.CUSTOMER_LIST_EMAIL)
       # # for value in cust_email:
       # print(cust_email[2].text)
       # self.assert_equal(cust_email[2].text,email_address,"New customer is not added")

    def updated_customerdata(self):
        time.sleep(8)
        custom_ph = self.driver.find_element(By.XPATH,self.CUSTOMERPHONE_VIEW)
        # custom_email = self.get_element_text(self.CUSTOMEREMAIL_VIEW)
        print(custom_ph.text)
        # print(custom_email)
        print(phonenum)
        self.assertEqual(custom_ph.text, phonenum, "Phone number cannot be viewed")
        # assert phonenum == custom_ph,"Phone number cannot be viewed"
        # self.assert_equal(emailadd,custom_email,"Email Cannot be viewed")
    def edit_Customer(self):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID,self.THREEDOTSBUTTON)))
        element.click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.EDITCUSTOMER).click()
        time.sleep(2)
        editcustom = self.driver.find_element(By.XPATH,self.EDITCUSTOMERTEXT)
        return editcustom.text


    def verify_customers_present(self):
        editcustomlist = self.driver.find_element(By.XPATH,self.CUSTOMER_LIST)
        return editcustomlist.text

    def select_filter(self):
        element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.FILTERBUTTON)))
        element.click()
        #
        # self.driver.execute_script("arguments[0].click()", element)
        time.sleep(5)

    def select_country(self):
        self.driver.find_element(By.XPATH,self.SELECTCOUNTRY).click()
        time.sleep(5)
        global countryname
        # self.driver.find_element"//li[@aria-label='Pakistan']").click()
        countryname = self.driver.find_elements(By.CLASS_NAME,self.SELECTCOUNTRYIES)
        randomcountry = random.choice(countryname)
        randomcountry.click()
        print(randomcountry.text)


    def click_applybutton(self):
        self.driver.find_element(By.XPATH,self.FILTERAPPLY)
        time.sleep(3)

    def verify_customers_of_selected_countries(self):
        # countrylist = []
            countrylist = self.driver.find_elements(By.CLASS_NAME,self.VIEWCOUNTRY)
            print("Number of customer shown is", len(countrylist))
            for listcount in countrylist:
                print(listcount.text)


       # countrylist =  self.driver.find_elementself.VIEWCOUNTRY)
       # print(countrylist.text)
       # print(countryname)


    def handle_toggle(self):
        try:
            self.driver.find_element(By.XPATH,self.CUSTOMER_TOGGLE_INACTIVE)
        except:
            self.driver.find_element(By.XPATH,self.CUSTOMER_TOGGLE_ACTIVE)
            print("Customer already active")

    def click_view(self):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, self.THREEDOTSBUTTON)))
        element.click()
        self.driver.find_element(By.XPATH,self.VIEWCUSTOMER).click()

    def verify_invoice_tiles(self):
        self.driver.find_element(By.XPATH,self.INVOICETILES)
        time.sleep(1)
        print("i am going inside open invoices")

    def verify_openInvoices(self):
        time.sleep(2)
        element = self.driver.find_element(By.XPATH,self.OPENINVOICES)
        element.click()
        self.driver.find_element(By.XPATH, self.PAGINGDD).click()
        self.driver.find_element(By.ID, self.FIFTYITEMS).click()
        print("i am already inside open invoices")
        # self.driver.execute_script("arguments[0].click();", element)
        time.sleep(4)
        try:
            invoicestatwfw = self.driver.find_elements(By.CLASS_NAME,self.INVOPENSTAT)
            print("Number of Open invoice is",len(invoicestatwfw))
            invoicestatopen = self.driver.find_elements(By.CLASS_NAME, self.INVOICEWFWSTAT)
            print("Number of Waiting for Funds invoices",len(invoicestatopen))

        except:
            assert "No records found" in self.driver.page_source
            print("No records found")


    def verify_closedInvoices(self):
        self.driver.find_element(By.ID,self.CLOSEDINVOICES).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.PAGINGDD).click()
        self.driver.find_element(By.ID, self.FIFTYITEMS).click()
        time.sleep(5)
        try:
            invoicestatpaid = self.driver.find_elements(By.CLASS_NAME,self.INVOICEPAIDSTATUS)
            print(len(invoicestatpaid))
        except:
            assert "No records found" in self.driver.page_source
            print("No records found")


    def search_customer(self,name):

        self.driver.find_element(By.ID,self.SEARCHCUSTOMER).send_keys(name)
        try:
            time.sleep(2)
            customername = self.driver.find_element(By.XPATH,"//a[normalize-space()='"+name+"']")
            print(customername.text)
            assert name == customername.text,"Searched customer found"
            print("Searched Customer Found")
        except:
            assert " No records found " in self.driver.page_source
            print("Searched Customer not Found")

    def apply_invoice_filter(self):
        self.driver.find_element(By.XPATH,self.INVOICESTATUSFILTER).click()
        self.driver.find_element(By.XPATH,self.CURRENT_STATUS).click()
    def apply_customer_Filter(self):
        self.driver.find_element(By.XPATH,self.CUSTOMERSTATUSFILTER).click()
        self.driver.find_element(By.XPATH,self.STATUSACTIVE).click()

    def vefify_Current_status_filter(self):
        try:
            invstat = self.driver.find_element(By.XPATH, self.CURRENTSTATUSONINVOICE)
            return invstat.text
        except:
            assert " No records found " in self.driver.page_source
            print("No Record Found")

    def verify_paidinvoices(self):
        self.driver.find_element(By.ID,self.PAYMENTINVOICES).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.PAGINGDD).click()
        self.driver.find_element(By.ID, self.FIFTYITEMS).click()
        time.sleep(5)
        try:
            invoicestatpaid = self.driver.find_elements(By.CLASS_NAME, self.INVOICEPAIDSTATUS)
            print(len(invoicestatpaid))
        except:
            assert "No records found" in self.driver.page_source
            print("No records found")

