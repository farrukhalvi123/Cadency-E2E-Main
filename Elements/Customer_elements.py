# from Pages.BasePage import BasePage
# from selenium.webdriver.common.by import By
#
#
# class customerelements(BasePage):
#     hamburger_icon = "//div[@class='tree-container ng-star-inserted']"
#     CUSTOMERANDRECEIVABLETAB = "//p[normalize-space()='Customers & Receivables']"
#     CUSTOMERTAB  ="//p[normalize-space()='Customers']"
#     CUSTOMERNAME = "title-heading-3 text-primary-3"
#     NOCUSTOMERFOUND = "//div[@class='title-heading-5']"
#     ADDFIRSTCUSTOMER = "//button[@class='p-element p-button-primary button-with-icon btn-120 p-button p-component']"
#     ADDCUSTOMER = "(//button[@class='p-element p-button-primary button-with-icon btn-150 p-button p-component ng-star-inserted'])[1]"
#     TITLE_ADD_CUSTOMER = "//span[normalize-space()='Add Customer']"
#     CUSTOMERNUMBER = "//input[@placeholder='Enter customer number']"
#     CUSTOMER_DISPLAY_NAME = "customerDisplayName"
#     FIRSTNAME = "firstName"
#     LASTNAME = "lastName"
#     PHONE = "//input[@id='phone']"
#     EMAIL = "email"
#     CURRENCY = "currencyId"
#     WEBSITE = "website"
#     CCEMAIL = "ccEmail"
#     CUSTOMER_TOGGLE_ACTIVE = "//div[@class='p-inputswitch p-component p-inputswitch-checked']"
#     CUSTOMER_TOGGLE_INACTIVE = "//div[@class='p-inputswitch p-component']"
#     SHOWATTACH = "//a[normalize-space()='+ Show/Add attachment']"
#     LOGOUPLOAD = "//input[@type='file']"
#     SAVEBUTTON = "//button[@type='submit']"
#     UPLOADED_IMAGE = "//button[@class='p-element p-button p-component p-button-icon-only']"
#     CURRENCY_FIELD =  "currencyId"
#     CURRENCY_SELECT = "//div[@class='inline-flex'][normalize-space()='USD']"
#     ADDRESSDETAILS = "//span[normalize-space()='Address Details']"
#     STREETLINE1 = "line1"
#     STREETLINE2 =  "line2"
#     POSTALCODE = "postalCode"
#     COUNTRY_FIELD = "countryId"
#     COUNTRY_PAK = "//div[contains(text(),'Pakistan')]"
#     STATEFIELD = "/html/body/cadency-root/cadency-features/div/div/div/div/cadency-customers-list/div/cadency-add-customer/div/form/p-sidebar/div/div[2]/div/div[2]/p-tabview/div/div[2]/p-tabpanel[2]/div/form/div/div[4]/div/p-dropdown/div/div[2]"
#     STATEFIELD_SINDH = "//li[@aria-label='Sindh']"
#     CITYID = "/html/body/cadency-root/cadency-features/div/div/div/div/cadency-customers-list/div/cadency-add-customer/div/form/p-sidebar/div/div[2]/div/div[2]/p-tabview/div/div[2]/p-tabpanel[2]/div/form/div/div[5]/div/p-dropdown/div/div[2]"
#     CITYKARACHI = "//li[@aria-label='Karachi']"
#     CUSTOMERNUMBER_VIEW  = "//*[@id='pr_id_2-table']/tbody/tr[1]/td[2]/div/span"
#     CUSTOMER_LIST_EMAIL = "paragraph-text-4.wrap-text-all"
#     THREEDOTSBUTTON = "//tbody/tr[1]/td[7]/div[1]/button[1]"
#     EDITCUSTOMER = "(//a[normalize-space()='Edit'])[1]"
#     EDITCUSTOMERTEXT = "//span[normalize-space()='Edit Customer']"
#     CUSTOMERPHONE_VIEW = '/html/body/cadency-root/cadency-features/div/div/div/div/cadency-customers-list/div/div/div[2]/p-table/div/div[2]/table/tbody/tr[1]/td[4]/div/div[1]/span'
#     CUSTOMEREMAIL_VIEW = '/html/body/cadency-root/cadency-features/div/div/div/div/cadency-customers-list/div/div[2]/p-table/div/div[2]/table/tbody/tr[1]/td[4]/div/div[2]/span'
#     CUSTOMER_LIST = "//tbody"
#     FILTERBUTTON = "//button[@class='p-element p-button-secondary filter-btn-count button-with-icon btn-150 p-button p-component']"
#     SELECTCOUNTRY = "//p-dropdown[@placeholder='Select country']"
#     SELECTCOUNTRYIES = "p-ripple.p-element.p-dropdown-item"
#     SELECTINVOICE = "//span[@class='ng-tns-c43-48 p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"
#     SELECTCURRENT = "//span[normalize-space()='Current']"
#     SELECTCUSTOMSTATUS = "//span[@class='ng-tns-c43-49 p-dropdown-label p-inputtext p-placeholder ng-star-inserted']"
#     SELECTACTIVE = "//span[normalize-space()='Active']"
#     FILTERAPPLY = "//button[@class='p-element p-button-primary button-with-icon btn-100 p-button p-component']"
#     VIEWCOUNTRY = 'title-heading-4.text-secondary-1.wrap-text-all.no-break-word'
#     no_record_text = "//td[normalize-space()='No records found']"
#     VIEWCUSTOMER = "//a[normalize-space()='View']"
#     INVOICETILES = "//ul[@role='tablist']"
#     OPENINVOICES = "//span[contains(text(),'Open Invoices')]"
#     CLOSEDINVOICES = "//span[contains(text(),'Closed Invoices')]"
#     INVOICESLIST = "max-width-300.ng-star-inserted"
#     STATUSTILE ="status-container status-orange3 ng-star-inserted"
#     CUSTOMERGRID = "td-contact-info.max-width-300.min-width-250"
#     REMPICTURE = By.XPATH,"//button[@class='p-element p-button-info p-1 lg:p-2 p-button-secondary delete-custom-uploader p-button p-component']"
#     SEARCHCUSTOMER = "searchText"
#     INVOICESTATUSFILTER = "//p-dropdown[@placeholder='Select invoice status']"
#     CURRENT_STATUS = "//li[@aria-label='Current']"
#     CUSTOMERSTATUSFILTER = "//p-dropdown[@placeholder='Select customer status']"
#     STATUSACTIVE = "//span[normalize-space()='Active']"
#     CURRENTSTATUSONINVOICE = "//div[@class='status-container status-green']"
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
