from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class loginelements(BasePage):
    emailfield = (By.ID,"EmailID")
    password = (By.ID,"EmailPassword")
    loginbtn = (By.XPATH,"//button[@type='button']")
    homepage_logo = (By.XPATH,"//img[@class='svg-icon svg-logo']")
    HomePage = (By.XPATH,"//span[@class='breadcrumb-title']")
    HomePage_sidenavbar = "//div[@class='side-navigation-menu-container half-content']"
    login_successful_popup = (By.ID,"toast-container")
    login_unsuccessful_popup = (By.XPATH,"//*[@id='toast-container']/div/div[1]")
    PROFILETHUMBNAIL = (By.XPATH,"//p-avatar[@class='p-element avatar-square-54']//div[@class='p-avatar p-component']")
    LOGOUT = (By.XPATH,"//span[normalize-space()='Logout']")




