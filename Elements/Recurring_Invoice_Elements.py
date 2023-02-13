from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class rec_invoices(BasePage):
    RECINVOICE = "//p[normalize-space()='Recurring Invoices']"
    CUSTOMERNAME = "//p-autocomplete[@class='p-element p-inputwrapper ng-tns-c107-46 ng-star-inserted ng-touched ng-dirty p-inputwrapper-filled ng-valid']"
    SELECTCUSTOMER = "customerEmail"
    ORDERNUMBER = NUMBEROFCYCLES = "customerName"
    CURRENCYINV = "pr_id_23_label"
    CURRENCYUSD = "//div[@class='inline-flex'][normalize-space()='USD']"
    FREQUENCY = "//input[@placeholder='Select Frequency']"
    FREQUENCYFIRST = "pr_id_24_list"
    FIRSTSENDDATE = "//input[@placeholder='Please select first Send Date']"
    ENDDATE = "//input[@placeholder='Please select first Send Date']"
    REFERENCEAREA = "//textarea[@placeholder='Enter reference']"
    ACTIVETOGGLE = "//p-inputswitch[@id='isActive']//span[@class='p-inputswitch-slider']"
    ITEMSELECT = "//input[@placeholder='Item']"
    ITEMLIST = "ng-trigger ng-trigger-overlayAnimation ng-tns-c107-52 p-autocomplete-panel p-component ng-star-inserted"
    DESCRIPTION = "//input[@placeholder='Description']"
    QUANTITY = "//input[@placeholder='Quantity']"
    PRICE = "//input[@placeholder='Price']"
    DISCOUNT = "//input[@placeholder='Disc %']"
    TAX = "//input[@placeholder='Select']"



















