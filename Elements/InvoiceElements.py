from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class invoiceelements(BasePage):
    INVOICETAB = (By.XPATH, "//p[normalize-space()='Invoices']")
    ADDINVOICEBTN = (By.XPATH, "//button[@class='p-element p-button-primary button-with-icon btn-150 p-button p-component']")
    CUSTNAMEDD = (By.XPATH, "//span[@class='p-button-icon pi pi-chevron-down']")
    CUSTNAMEDD_VALUE = '//*[starts-with(@class,"p-ripple p-element p-autocomplete-item ng-tns")]'
    CURRENCYDD = (By.ID, "currency")
    CAD = (By.CLASS_NAME,"country-item.ng-star-inserted")
    EXCHANGERATE = (By.XPATH, "//a[normalize-space()='Modify Rate']")
    REFERENCE = (By.XPATH, "//textarea[@placeholder='Enter reference']")
    ITEMSELECTION = (By.XPATH, "//button[@class='p-element p-ripple p-autocomplete-dropdown ng-tns-c107-56 p-button p-component p-button-icon-only ng-star-inserted']//span[@class='p-button-icon pi pi-chevron-down']")
    DESCRIPTION = (By.XPATH, "//input[@placeholder='Description']")
    QUANTITY = (By.XPATH, "//input[@placeholder='Quantity']")
    PRICE = (By.XPATH, "//input[@placeholder='Price']")
    DISCOUNT = (By.XPATH, "//input[@placeholder='Disc %']")
    TAXDD = (By.XPATH, "//button[@class='p-element p-ripple p-autocomplete-dropdown ng-tns-c107-57 p-button p-component p-button-icon-only ng-star-inserted']//span[@class='p-button-icon pi pi-chevron-down']")
    SAVEBTN = (By.XPATH, "//button[@class='p-element p-button-primary btn-150 p-button p-component']")
    INV_EMAIL = (By.ID,"customerEmail")
    INVNUM = (By.ID,"customerName")
    INVDATE = "//input[@placeholder='Please select invoice date']"
    INVDUEDATE = "//input[@placeholder='Please select due date']"
    INVITEMSDD = (By.XPATH,"//input[@placeholder='Item']")
    ADDINVITEMS = (By.XPATH,"//span[normalize-space()='+ Add New Item']")
    ADDITEMNAME = (By.ID,"name")
    ADDITEMCODE = (By.ID,"code")
    ADDITEMTYPEDD = (By.XPATH,"//input[@placeholder='Enter type']")
    ADDITEMTYPE = (By.XPATH,"//li[@aria-label='Inventory']")
    ADDITEMUNITPRICEID = "name"
    ADDITEMUNITPRICETAGNAME = "type"
    ADDITEMSAVEBUTTON = (By.XPATH,"(//button[@type='submit'])[3]")
    SELECTITEM = (By.XPATH,"//span[contains(text(), '"+WORDS+"')]")










