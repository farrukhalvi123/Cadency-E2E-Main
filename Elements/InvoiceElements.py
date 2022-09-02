from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class invoiceelements(BasePage):
    INVOICETAB = (By.XPATH, "//p[normalize-space()='Invoices']")
    ADDINVOICEBTN = (By.XPATH, "//button[@class='p-element p-button-primary button-with-icon btn-150 p-button p-component']")
    CUSTNAMEDD = (By.XPATH, "//button[@class='p-element p-ripple p-autocomplete-dropdown ng-tns-c107-52 p-button p-component p-button-icon-only ng-star-inserted']//span[@class='p-button-icon pi pi-chevron-down']")
    CURRENCYDD = (By.XPATH, "//span[@class='p-dropdown-trigger-icon ng-tns-c43-53 pi pi-chevron-down']")
    EXCHANGERATE = (By.XPATH, "//a[normalize-space()='Modify Rate']")
    REFERENCE = (By.XPATH, "//textarea[@placeholder='Enter reference']")
    ITEMSELECTION = (By.XPATH, "//button[@class='p-element p-ripple p-autocomplete-dropdown ng-tns-c107-56 p-button p-component p-button-icon-only ng-star-inserted']//span[@class='p-button-icon pi pi-chevron-down']")
    DESCRIPTION = (By.XPATH, "//input[@placeholder='Description']")
    QUANTITY = (By.XPATH, "//input[@placeholder='Quantity']")
    PRICE = (By.XPATH, "//input[@placeholder='Price']")
    DISCOUNT = (By.XPATH, "//input[@placeholder='Disc %']")
    TAXDD = (By.XPATH, "//button[@class='p-element p-ripple p-autocomplete-dropdown ng-tns-c107-57 p-button p-component p-button-icon-only ng-star-inserted']//span[@class='p-button-icon pi pi-chevron-down']")
    SAVEBTN = (By.XPATH, "//button[@class='p-element p-button-primary btn-150 p-button p-component']")





