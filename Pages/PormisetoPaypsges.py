import time
from selenium.webdriver.common.by import By




class Ptop():
    def __init__(self, driver):

        self.driver = driver
        self.open_filter = "//a[contains(text(), 'Open')]"


def Opentab(self):
    openfil = self.driver.find_element(By.XPATH, self.open_filter)
    # driver.execute_script("arguments[3].click;", openfil)
    openfil.click()
    time.sleep(3)