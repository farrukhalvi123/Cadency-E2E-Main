import os
import time
from random import randint
from selenium.webdriver.common.by import By
from Constants.URLS import TestData


from Elements.Customer_elements import customerelements



class CustomerPages(customerelements):

    def __init__(self, driver):
        super().__init__(driver)


    def Go_to_customerTab(self):
        self.wait(10)
        try:
            assert "template" in self.driver.current_url
            self.driver.get(TestData.CUSTOMERMANAGEMENT)
        except:
            self.click_using_js(self.CUSTOMERANDRECEIVABLETAB)
            self.wait(1)
            self.click_using_js(self.CUSTOMERTAB)


    def click_addbutton(self):

        self.click_using_js(self.ADDCUSTOMER)

    def verify_customerform(self):
        self.verify_element_display(self.TITLE_ADD_CUSTOMER)
    def customer_number(self):
        # if self.result_str == "": This needs to change when the customer number will be auto generated
            self.result_str = 'CUS-0000-' + ''.join(["{}".format(randint(0, 7)) for num in range(0, 5)])
            self.input_element(self.CUSTOMERNUMBER,self.result_str)
            global cus_number
            cus_number = self.result_str
            print(cus_number)

    def enter_customerDetails(self, cus_dis_name,fname,lname,phno,email,web,ccemail):
        self.input_element(self.CUSTOMER_DISPLAY_NAME, cus_dis_name)
        self.input_element(self.FIRSTNAME, fname)
        self.input_element(self.LASTNAME, lname)
        self.input_element(self.PHONE, phno)
        global phonenum, emailadd
        phonenum = phno
        emailadd = email
        self.input_element(self.EMAIL, email)
        self.input_element(self.WEBSITE, web)
        self.input_element(self.CCEMAIL, ccemail)
        self.click_element(self.CURRENCY_FIELD)
        self.click_using_js(self.CURRENCY_SELECT)

    def upload_logo(self):
        self.wait(2)
        path = os.getcwd()
        element = self.driver.find_element(By.XPATH,self.LOGOUPLOAD)
        self.driver.execute_script("arguments[0].style.display = 'block';", element)
        path3 = os.path.abspath(path + r'\\TestData\\Picture\\new2.jpg')
        element.send_keys(path3)
        time.sleep(3)
        self.get_web_element(self.UPLOADED_IMAGE)
        time.sleep(5)

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

    def customer_alreadypresent(self):
        self.wait(2)
        self.get_element_text(self.CUSTOMERNUMBER_VIEW)

    def verify_new_user_successfully_added(self):
       self.wait(5)

       cust_numb =  self.get_element_text(self.CUSTOMERNUMBER_VIEW)
       print(cust_numb)
       self.assert_equal(cus_number,cust_numb,"New customer is not added")

    def updated_customerdata(self):
        self.wait(8)
        custom_ph = self.get_element_text(self.CUSTOMERPHONE_VIEW)
        custom_email = self.get_element_text(self. CUSTOMEREMAIL_VIEW)
        print(custom_ph)
        print(custom_email)
        print(phonenum,emailadd)
        self.assert_equal(phonenum,custom_ph,"Phone number cannot be viewed")
        self.assert_equal(emailadd,custom_email,"Email Cannot be viewed")
    def edit_Customer(self):
        self.wait(10)
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
        countryname = self.get_element_text(self.SELECTPAK)
        self.click_using_js(self.SELECTPAK)
        time.sleep(5)

    def click_applybutton(self):
        self.click_element(self.FILTERAPPLY)

    def verify_customers_of_selected_countries(self):
       countrylist =  self.driver.find_element(By.XPATH,self.VIEWCOUNTRY)
       print(countrylist.text)
       print(countryname)
       self.assert_equal(countrylist.text,countryname,"Selected Country not found")

    def handle_toggle(self):
        try:
            self.click_element(self.CUSTOMER_TOGGLE_INACTIVE)
        except:
            self.driver.find_element(By.XPATH,self.CUSTOMER_TOGGLE_ACTIVE)
            print("Customer already active")



