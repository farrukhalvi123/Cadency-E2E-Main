from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from Elements.LoginElements import loginelements
from allure_commons._allure import attach
from allure_commons.types import AttachmentType



class TestData:
    global Environment
    BROWSER = "chrome"
    PLATFORM = "local"
    ENVIRONMENT = "Dev" # there are only three enviornments, DEV, STAGING and PRODUCTION
    CADENCY_MAIN = "http://10.4.4.20:6120/login"
    CADENCY_MANAGEMENT = "http://10.4.4.20:6121/login"
    CUSTOMERMANAGEMENT = "http://10.4.4.20:6122/dashboard"
    CUSTOMERINVOICES = "http://10.4.4.20:6120/customers-receivables/customer-invoices"
    CADENCY_MANAGEMENT_DASHBOARD = "http://10.4.4.20:6121/dashboard"
    STAGING_MAIN = "https://staging.main.cadency.io/"
    STAGING_MANAGEMENT = "https://staging.management.cadency.io/"
    STAGING_CUSTOMER = "https://staging.customer.cadency.io/"
    STAGING_CHECKOUT = "https://staging.checkout.cadency.io/"
    CADENCY_MAIN_INV_DETAILS = "http://10.4.4.20:6120/customers-receivables/customer-invoices"
    def __init__(self,driver):
        self.driver = driver
        self.emailfield = "EmailID"
        self.password = "EmailPassword"
        self.loginbtn = "//button[@type='submit']"
        self.username_tb = "//input[@placeholder='Enter Username']"
        self.password_tb = " //input[@placeholder='Enter Password']"
        self.login_btn = "//span[normalize-space()='Login']"









