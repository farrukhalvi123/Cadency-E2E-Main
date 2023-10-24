class TestData:
    BROWSER = "chrome"
    PLATFORM = "local"
    ENVIRONMENT = "Staging" # there are only three enviornments, DEV, STAGING and PRODUCTION
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
    LOCAL_MAIN_USERNAME = "clarkkent"
    LOCAL_MAIN_PASSWORD = "Cadency@123"
    STAGING_MAIN_USERNAME = "jaxsonbriggs"
    STAGING_MAIN_PASSWORD = "7sItGjWVfZgc"
    LOCAL_CUSTOMER_USERNAME = "selinakyle@yopmail.com"
    LOCAL_CUSTOMER_PASSWORD = "Cadency@123"
    STAGING_CUSTOMER_USERNAME = "Tbm"
    STAGING_CUSTOMER_PASSWORD = "Talha123"
    LOCAL_ADMIN_USERNAME = "admin"
    LOCAL_ADMIN_PASSWORD = "123"
    STAGING_ADMIN_USERNAME = "farrukhalvi"
    STAGING_ADMIN_PASSWORD = 'Cadency@123'
    def __init__(self,driver):
        self.driver = driver
        self.emailfield = "EmailID"
        self.password = "EmailPassword"
        self.loginbtn = "//button[@type='submit']"
        self.username_tb = "//input[@placeholder='Enter Username']"
        self.password_tb = " //input[@placeholder='Enter Password']"
        self.login_btn = "//span[normalize-space()='Login']"









