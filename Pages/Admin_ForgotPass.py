
from selenium.webdriver.common.by import By
class AdminForgotPass():

    def __init__(self, driver):
        self.driver = driver
        self.FORGOT_PASSWORD = "//span[normalize-space()='Forgot Password?']"

    def click_on_forgotpass(self):
        forgetpwd = self.driver.find_element(By.XPATH,self.FORGOT_PASSWORD)
        self.driver.execute_script("arguments[0].click()", forgetpwd)