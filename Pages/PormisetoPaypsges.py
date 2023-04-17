import time
from selenium.webdriver.common.by import By




class Ptop():
 def __init__(self, driver):

        self.driver = driver
        self.open_filter = "//a[contains(text(), 'Open')]"
        self.takefirstinv= "//a[@class='p-element title-heading-1 text-primary-3'][position() mod 2 = 1]"
        self.promisedtop="p-element.p-icon-button.promise-to-pay-btn-mini.overlay-primary-7.p-button.p-component.ng-star-inserted"
        self.paydate="//textarea[@id='notes']"
        self.submit="//button[@type='submit']"

 # self.getclassforinv = "//td[@class='max-width-300 overflow-hidden custom-status-wrapper statusCenter font-bold ng-star-inserted'][position() mod 2 = 1]"


 def Opentab(self):
    openfil = self.driver.find_element(By.XPATH, self.open_filter)
    openfil.click()
    time.sleep(3)

 def medo(self):
    invone=self.driver.find_element(By.XPATH, self.takefirstinv)
    print(invone.text)
    invone.click()
    time.sleep(3)
 def pptop(self):
     ptopay=self.driver.find_element(By.CLASS_NAME, self.promisedtop)
     time.sleep(4)
     ptopay.click()
     time.sleep(4)
     paymentdate=self.driver.find_element(By.XPATH, self.paydate)
     paymentdate.send_keys('promise to pay')
     time.sleep(3)
     save=self.driver.find_element(By.XPATH, self.submit)
     save.click()
     time.sleep(3)

 # def tagcheck(self):
 #     tagging=
