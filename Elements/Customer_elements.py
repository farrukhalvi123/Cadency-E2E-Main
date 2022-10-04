from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class customerelements(BasePage):
    hamburger_icon = (By.XPATH,"//div[@class='tree-container ng-star-inserted']")
    CUSTOMERANDRECEIVABLETAB = (By.XPATH,"//p[normalize-space()='Customers & Receivables']")
    CUSTOMERTAB  =(By.XPATH,"//p[normalize-space()='Customers']")
    ADDCUSTOMER = (By.XPATH,"(//button[@class='p-element p-button-primary button-with-icon btn-150 p-button p-component ng-star-inserted'])[1]")
    TITLE_ADD_CUSTOMER = (By.XPATH,"//span[normalize-space()='Add Customer']")
    CUSTOMERNUMBER = (By.XPATH,"//input[@placeholder='Enter customer number']")
    CUSTOMER_DISPLAY_NAME = (By.ID,"customerDisplayName")
    FIRSTNAME = (By.ID,"firstName")
    LASTNAME = (By.ID,"lastName")
    PHONE = (By.XPATH,"//input[@id='phone']")
    EMAIL = (By.ID,"email")
    CURRENCY = (By.ID,"currencyId")
    WEBSITE = (By.ID,"website")
    CCEMAIL = (By.ID,"ccEmail")
    CUSTOMER_TOGGLE_ACTIVE = "//div[@class='p-inputswitch p-component p-inputswitch-checked']"
    CUSTOMER_TOGGLE_INACTIVE = (By.XPATH,"//div[@class='p-inputswitch p-component']")
    LOGOUPLOAD = ("//input[@type='file']")
    SAVEBUTTON = (By.XPATH,"//button[@type='submit']")
    UPLOADED_IMAGE = (By.XPATH,"//button[@class='p-element p-button p-component p-button-icon-only']")
    CURRENCY_FIELD = (By.ID, "currencyId")
    CURRENCY_SELECT = (By.XPATH,"//div[@class='inline-flex'][normalize-space()='USD']")
    ADDRESSDETAILS = (By.XPATH,"//span[normalize-space()='Address Details']")
    STREETLINE1 = (By.ID,"line1")
    STREETLINE2 = (By.ID, "line2")
    POSTALCODE = (By.ID,"postalCode")
    COUNTRY_FIELD = (By.ID,"countryId")
    COUNTRY_PAK = (By.XPATH,"//div[contains(text(),'Pakistan')]")
    STATEFIELD = (By.ID,"stateId")
    STATEFIELD_SINDH = (By.XPATH,"//li[@aria-label='Sindh']")
    CITYID = (By.ID,"cityId")
    CITYKARACHI = (By.XPATH,"//li[@aria-label='Karachi']")
    CUSTOMERNUMBER_VIEW  = (By.XPATH,"//*[@id='pr_id_2-table']/tbody/tr[1]/td[2]/div/span")
    CUSTOMER_LIST_EMAIL = "paragraph-text-4.wrap-text-all"
    THREEDOTSBUTTON = (By.XPATH,"//tbody/tr[1]/td[7]/div[1]/button[1]")
    EDITCUSTOMER = (By.XPATH,"(//a[normalize-space()='Edit'])[1]")
    EDITCUSTOMERTEXT = (By.XPATH,"//span[normalize-space()='Edit Customer']")
    CUSTOMERPHONE_VIEW = (By.XPATH,'/html/body/cadency-root/cadency-features/div/div/div/div/cadency-customers-list/div/div[2]/p-table/div/div[2]/table/tbody/tr[1]/td[4]/div/div[1]/span')
    CUSTOMEREMAIL_VIEW = (By.XPATH,'/html/body/cadency-root/cadency-features/div/div/div/div/cadency-customers-list/div/div[2]/p-table/div/div[2]/table/tbody/tr[1]/td[4]/div/div[2]/span')
    CUSTOMER_LIST = (By.XPATH,"//tbody")
    FILTERBUTTON = (By.XPATH,"//button[@class='p-element p-button-secondary filter-btn-count button-with-icon btn-150 p-button p-component']")
    SELECTCOUNTRY = (By.XPATH,"//p-dropdown[@placeholder='Select country']")
    SELECTPAK = (By.XPATH,"//li[@aria-label='Pakistan']")
    SELECTINVOICE = (By.XPATH,"//span[@class='ng-tns-c43-48 p-dropdown-label p-inputtext p-placeholder ng-star-inserted']")
    SELECTCURRENT = (By.XPATH,"//span[normalize-space()='Current']")
    SELECTCUSTOMSTATUS = (By.XPATH,"//span[@class='ng-tns-c43-49 p-dropdown-label p-inputtext p-placeholder ng-star-inserted']")
    SELECTACTIVE = (By.XPATH,"//span[normalize-space()='Active']")
    FILTERAPPLY = (By.XPATH,"//button[@class='p-element p-button-primary button-with-icon btn-100 p-button p-component']")
    VIEWCOUNTRY = 'title-heading-4 text-secondary-2 wrap-text-all'
    no_record_text = (By.XPATH,"//td[normalize-space()='No records found']")





















