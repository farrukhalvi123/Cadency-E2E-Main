import re
import time

from selenium.webdriver.common.by import By




class Ptop():
 def __init__(self, driver):

        self.driver = driver
        self.open_fil = "//span[@class='p-ink p-ink-active']"
        self.takefirstinv= "//a[@class='p-element title-heading-1 text-primary-3'][position() mod 2 = 1]"
        self.promisedtop="p-element.p-icon-button.promise-to-pay-btn-mini.overlay-primary-7.p-button.p-component.ng-star-inserted"
        self.paydate="//textarea[@id='notes']"
        self.submit="//button[@type='submit']"
        self.close="pi.pi-times"
        self.invoicetag="//p[normalize-space()='Invoice #']"
        self.Ptag="//i[@class='pi pi-info-circle']"
        self.identifyinginvcol="max-width-300.ng-star-inserted"
        self.newptopalltab="//span[@class='cus-minibadge badge promise-to-pay width-90 text-center justify-content-center ng-star-inserted']"


 # self.getclassforinv = "//td[@class='max-width-300 overflow-hidden custom-status-wrapper statusCenter font-bold ng-star-inserted'][position() mod 2 = 1]"


 def Openingtab(self):
    openfil = self.driver.find_element(By.XPATH, self.open_fil)
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
     time.sleep(6)
     cancel_elements = self.driver.find_elements(By.CLASS_NAME, self.close)
     cancel = cancel_elements[1]
     cancel.click()
     time.sleep(15)

     # pinvoice=self.driver.find_element(By.XPATH, self.invoicetag)
     # pinvoice.click()
     # time.sleep(6)

     # try:
         # Replace "expected_element_xpath" with the XPath expression of the element you expect to find
     expected_element = self.driver.find_element(By.XPATH, self.Ptag)
     print('promise to pay')
     assert expected_element.is_displayed(), "Expected element not found on page"
     # except NoSuchElementException:
     #     # If the expected element is not found, an exception will be raised
     #     assert False, "Expected element not found on page"
     time.sleep(15)

 def identifyingallptops(self):

  invoicesforptag= self.driver.find_elements(By.CLASS_NAME , self.identifyinginvcol)
  print(len(invoicesforptag))

  for index,  invidentifyptop in enumerate( invoicesforptag):


      invoice_text = invidentifyptop.text
      if index %9 == 0:
          print(index ,invoice_text)

