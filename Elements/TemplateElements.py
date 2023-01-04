from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class TemplateElements(BasePage):
    SETTINGCOGS = (By.ID,"Group_19806")
    TEMPLATETILE = (By.XPATH,"//div[contains(text(),'Templates')]")
    ADDTEMPLATE = (By.XPATH,"//button[@class='p-element p-button-primary button-with-icon btn-150 p-button p-component ng-star-inserted']")
    TEMPLATENAME = (By.ID,"TemplateName")