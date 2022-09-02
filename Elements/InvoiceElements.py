from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class invoiceelements(BasePage):
    INVOICETAB = (By.XPATH, "//p[normalize-space()='Invoices']")
    ADDINVOICE = (By.XPATH, "//button[@class='p-element p-button-primary button-with-icon btn-150 p-button p-component']")


