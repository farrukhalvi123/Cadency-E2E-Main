import re
import time

from selenium.webdriver.common.by import By
from Pages.CP_Page_verifyDispute import Open_dispute_tag




class Ptop():
 def __init__(self, driver):

        self.driver = driver
        self.open_fil = "//span[@class='p-ink p-ink-active']"
        self.takefirstinv= "p-element.title-heading-1.text-primary-3"
        self.promisedtop="p-element.p-icon-button.promise-to-pay-btn-mini.overlay-primary-7.p-button.p-component.ng-star-inserted"
        self.paydate="//textarea[@id='notes']"
        self.submit="//button[@type='submit']"
        self.close="pi.pi-times"
        self.invoicetag="//p[normalize-space()='Invoice #']"
        self.Ptag="//tbody/tr[1]/td[1]/div[1]/span[1]"
        self.identifyinginvcol="max-width-300.ng-star-inserted"
        self.newptopalltab="//span[@class='cus-minibadge badge promise-to-pay width-90 text-center justify-content-center ng-star-inserted']"
        self.hovering = "//a[@class='toogle-icon full-content']"
        self.ptoptab="p-ripple.p-element.p-tabview-nav-link"
        self.ACtionB="//button[@class='p-element more-vert-btn p-button p-component']"
        self.View="//a[normalize-space()='View']"
        # self.Invoice_section="//p[normalize-space()='Invoices']"
        # self.towards_opentab="//a[@id='p-tabpanel-9-label']"
        self.justpanel=Open_dispute_tag(driver)
        self.threedot_Action="//tbody/tr[1]/td[9]/div[2]/button[1]"
        self.paynowto_checkout="//a[normalize-space()='Pay Now']"
        self.drop_down="//span[@class='p-dropdown-trigger-icon ng-tns-c4207907238-0 pi pi-chevron-down']"
        self.select_country="//span[@class='shipcountry-item cmn-dropdown-item'][normalize-space()='United States']"
        self.by_swift="//div[@class='transfer-method-content-box ng-star-inserted']//div[1]//a[1]"
        # self.paysafe="//a[@id='p-tabpanel-4-label']//div[@class='p-radiobutton-box']"
        # self.by_visa="//div[@id='p-tabpanel-4']//a[@class='inner-cards']"
        self.Pay_now ="//button[@class='p-element p-button-primary p-button p-component']"
        self.time_line="//tbody/tr[1]/td[7]/div[1][1]/span[1]/i[1]"
        self.action2="//div[@class='p-component-overlay p-sidebar-mask p-component-overlay-enter p-component-overlay-leave']"
        self.Viewagain="//a[normalize-space()='View']"
        self.Record_manually="//button[@class='p-element p-icon-button overlay-primary-7 p-button p-component ng-star-inserted']"
        self.payment_mode="paymentTypeId"
        self.by_cashpayment = "//span[@class='ng-star-inserted'][normalize-space()='Visa']"
        self.save_recordpayemnt="//button[@type='submit']"
        self.alltab="p-ripple p-element p-tabview-nav-link"

        # self.Cardholder_name="//input[@placeholder='Cardholder Name']"
        # self.Cardno="//p[normalize-space()='Card Number']"
        # self.dateofexpiry="//input[@id='expiry-date']"
        # self.CVV_number="cvv"
        # self.Paynow_B="//button[@class='p-element p-button-primary btn-100 p-button p-component']"


 # self.getclassforinv = "//td[@class='max-width-300 overflow-hidden custom-status-wrapper statusCenter font-bold ng-star-inserted'][position() mod 2 = 1]"


 def Openingtab(self):
    openfil = self.driver.find_element(By.XPATH, self.open_fil)
    openfil.click()
    time.sleep(3)

 def medo(self):
    invone=self.driver.find_element(By.CLASS_NAME, self.takefirstinv)
    print(invone.text)
    invone.click()
    # for inv in invone:
    #     print(inv.text)
    #     inv[0].click()
    time.sleep(5)
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
     # cancel_elements = self.driver.find_elements(By.CLASS_NAME, self.close)
     # cancel = cancel_elements[1]
     # cancel.click()
     # time.sleep(15)

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


 def goingtonewtab(self):
      self.driver.execute_script("window.open();")
      self.driver.switch_to.window(self.driver.window_handles[1])

 def towardsinvoice_opentab(self):
     # hover=self.driver.find_element(By.XPATH,self.hovering)
     # hover.click()
     # time.sleep(5)
     self.justpanel.hovering()
     # invoicesection=self.driver.find_element(By.XPATH,self.Invoice_section)
     # self.driver.execute_script("arguments[0].click()",)
     # invoicesection.click()
     # time.sleep(5)
     # opentab=self.driver.find_element(By.XPATH,self.towards_opentab)
     # opentab.click()
     time.sleep(10)
     ActionB=self.driver.find_element(By.XPATH,self.threedot_Action)
     ActionB.click()
     time.sleep(10)
     PAYNOWB=self.driver.find_element(By.XPATH,self.paynowto_checkout)
     PAYNOWB.click()
     time.sleep(10)
     self.driver.switch_to.window(self.driver.window_handles[1])
     time.sleep(5)





 def Checkout(self):
     selectionbydropdown=self.driver.find_element(By.XPATH,self.drop_down)
     selectionbydropdown.click()
     time.sleep(5)
     choosecountry=self.driver.find_element(By.XPATH,self.select_country)
     choosecountry.click()
     time.sleep(5)
     bySwift=self.driver.find_element(By.XPATH,self.by_swift)
     bySwift.click()
     time.sleep(7)
     PAYNW = self.driver.find_element(By.XPATH, self.Pay_now)
     PAYNW.click()
     time.sleep(10)
     assert "Invoice Awaiting Payment" in self.driver.page_source
     print ('Invoice Awaiting Payment >> identified ')
     time.sleep(10)
     self.driver.switch_to.window(self.driver.window_handles[0])
     self.driver.refresh()
     time.sleep(10)
     timeline_dropdown=self.driver.find_element(By.XPATH,self.time_line)
     timeline_dropdown.click()
     time.sleep(5)
     assert "Promise Fulfilled" in self.driver.page_source
     print('Promise Fulfilled ')
     time.sleep(5)

 def Manuallyrecordpayment(self):
     # time.sleep(3)
     # actionthreedots=self.driver.find_element(By.XPATH,self.action2)
     # actionthreedots.click()
     # time.sleep(3)
     # viewss=self.driver.find_element(By.XPATH,self.Viewagain)
     # viewss.click()
     # time.sleep(3)
     byrecordpayment=self.driver.find_element(By.XPATH,self.Record_manually)
     byrecordpayment.click()
     time.sleep(5)
     paymodedd = self.driver.find_element(By.ID, self.payment_mode)
     paymodedd.click()
     time.sleep(5)
     bycash=self.driver.find_element(By.XPATH,self.by_cashpayment)
     bycash.click()
     time.sleep(3)
     savedmanually=self.driver.find_element(By.XPATH,self.save_recordpayemnt)
     savedmanually.click()
     time.sleep(5)
     cancel_elements = self.driver.find_elements(By.CLASS_NAME, self.close)
     cancel = cancel_elements[1]
     cancel.click()
     time.sleep(5)
     alltabone=self.driver.find_element(salltab









 # def select_payfe(self):
 #     paysafeV=self.driver.find_element(By.XPATH,self.paysafe)
 #     paysafeV.click()
 #     time.sleep(10)
 #     byvisa=self.driver.find_element(By.XPATH,self.by_visa)
 #     byvisa.click()
 #     time.sleep(10)
 #     PAYNW=self.driver.find_element(By.XPATH,self.Pay_now)
 #     PAYNW.click()
 #     time.sleep(10)
 #
 # def Cardholder_Name(self,cdholdername):
 #     cardholderN=self.driver.find_element(By.XPATH,self.Cardholder_name)
 #     cardholderN.clear()
 #     time.sleep(5)
 #     cardholderN.send_keys(cdholdername)
 #
 # def Card_Number(self,CDnum):
 #     Card_Numberforcard=self.driver.find_element(By.XPATH,self.Cardno)
 #     # Card_Numberforcard.clear()
 #     time.sleep(5)
 #     Card_Numberforcard.send_keys(CDnum)
 #
 # def Expiry_date(self,dateE):
 #     Edate=self.driver.find_element(By.XPATH,self.dateofexpiry)
 #     Edate.clear()
 #     time.sleep(5)
 #     Edate.send_keys(dateE)
 #
 # def CVV_no(self,noCVV):
 #     CVVnumber=self.driver.find_element(By.ID,self.CVV_number)
 #     CVVnumber.clear()
 #     time.sleep(5)
 #     CVVnumber.send_keys(noCVV)
 #     P_now=self.driver.find_element(By.XPATH,self.Paynow_B)
 #     P_now.click()
 #     time.sleep(5)
