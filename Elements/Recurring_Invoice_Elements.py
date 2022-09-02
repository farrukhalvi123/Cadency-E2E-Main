from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class rec_invoices(BasePage):
    RECINVOICE = (By.XPATH,"//p[normalize-space()='Recurring Invoices']")
    CUSTOMERNAME = (By.XPATH,"//p-autocomplete[@class='p-element p-inputwrapper ng-tns-c107-46 ng-star-inserted ng-touched ng-dirty p-inputwrapper-filled ng-valid']")
    SELECTCUSTOMER = (By.ID,"customerEmail")
    ORDERNUMBER = NUMBEROFCYCLES = (By.ID,"customerName")
    CURRENCYINV = (By.XPATH,"pr_id_23_label")
    CURRENCYUSD = (By.XPATH,"//div[@class='inline-flex'][normalize-space()='USD']")
    FREQUENCY = (By.XPATH,"//input[@placeholder='Select Frequency']")
    FREQUENCYFIRST = (By.ID,"pr_id_24_list")
    FIRSTSENDDATE = (By.XPATH,"//input[@placeholder='Please select first Send Date']")
    ENDDATE = (By.XPATH,"//input[@placeholder='Please select first Send Date']")
    REFERENCEAREA = (By.XPATH,"//textarea[@placeholder='Enter reference']")
    ACTIVETOGGLE = (By.XPATH,"//p-inputswitch[@id='isActive']//span[@class='p-inputswitch-slider']")
    ITEMSELECT = (By.XPATH,"//input[@placeholder='Item']")
    ITEMLIST = (By.CLASS_NAME,"ng-trigger ng-trigger-overlayAnimation ng-tns-c107-52 p-autocomplete-panel p-component ng-star-inserted")
    DESCRIPTION = (By.XPATH,"//input[@placeholder='Description']")
    QUANTITY = (By.XPATH,"//input[@placeholder='Quantity']")
    PRICE = (By.XPATH,"//input[@placeholder='Price']")
    DISCOUNT = (By.XPATH,"//input[@placeholder='Disc %']")
    TAX = (By.XPATH,"//input[@placeholder='Select']")



















