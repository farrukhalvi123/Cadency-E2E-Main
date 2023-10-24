import time

from selenium.webdriver.common.by import By
from Constants.URLS import TestData

class AdvancePaymentSetting():


    def __init__(self, driver):
        self.driver = driver
        self.settingsicon= "//p-avatar[@class='p-element avatar-square-54 avatar-icon']//*[@class='svg-icon']//*[name()='svg']"
        self.advicon=  "//li[@class='setting-list-item advance-payment-settigs ng-star-inserted']//div[@class='p-avatar p-component']"

        self.dropdown= "//button[@id='p-panel-0-label']"
        self.trans = ("//*[contains(@aria-label, 'collapse button')]")
        #Xpath = // *[contains( @ name, 'btn')]

    def go_to_main(self):
        self.driver.get(TestData.STAGING_MAIN)

    def star(self):
        time.sleep(5)
        advset = self.driver.find_element(By.XPATH, self.settingsicon)
        advset.click()
        advicon = self.driver.find_element(By.XPATH, self.advicon)
        advicon.click()
        time.sleep(5)

    def dropUK(self):
        dd= self.driver.find_elements(By.XPATH,self.trans)
        time.sleep(3)

        for i in dd:
             i.click()
             time.sleep(6)

