
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ManageTeams():

    def __init__(self, driver):
        self.driver = driver
        self.USERNAME = "login-email"
        self.PASSWORD = "//input[@placeholder='Enter Password']"
        self.LOGINBUTTON = "//button[@type='submit']"
        self.PROFILEPICCLICK = "//span[@class='p-button-link ml-2 font-semibold flex align-items-center']"
        self.LOGOUTBUTTON = "//a[normalize-space()='Logout']"
        self.FORGOT_PASSWORD = "//span[normalize-space()='Forgot Password?']"

        # General Elements
        self.LEFTSIDENAVMENU = "//div[@class='side-navigation-menu-container half-content']"
        self.USERACCESSCONTROL = "//p[normalize-space()='User Access Control']"
        self.MANAGETEAMS = "//p[normalize-space()='Manage Teams']"
        self.MANAGETEAMSEARCHBAR = "//input[contains(@placeholder,'Search by Team Name')]"

        # Add New Team Page Elements
        self.ADDBUTTON = "//span[contains(text(),'Add +')]"
        self.TEAMNAME = "teamname"
        self.TEAMDESC = "//textarea[@placeholder=' Description (Optional)']"
        self.ASSIGNUSERTAB = "//span[normalize-space()='Assign Users']"
        self.ASSIGNUSERSEARCHBAR = "//div[@class='p-picklist-list-wrapper p-picklist-source-wrapper']//input[@role='textbox']"
        self.ASSIGNUSERSEARCHUSERFOUND = "//h5[normalize-space()='Kylian Mbappe']"
        self.MOVESINGLEBUTTON = "//span[@class='p-button-icon pi pi-angle-right']"
        self.MOVEDOUBLEBUTTON = "//span[@class='p-button-icon pi pi-angle-double-right']"
        self.BACKMOVESINGLEBUTTON = "//span[@class='p-button-icon pi pi-angle-left']"
        self.BACKMOVEDOUBLEBUTTON = "//span[@class='p-button-icon pi pi-angle-double-left']"
        self.ALLUSERSBOX = "cdk-drop-list-0"  # ID
        self.ASSIGNEDUSERBOX = "cdk-drop-list-1"  # ID
        self.MODULESTAB = "//span[normalize-space()='Modules']"
        self.SAVEDQATEAMNAME = "//label[normalize-space()='QA Team']"

        # Modules Check Boxes
        self.APPLYALLPERMISSIONSCHECK = "//p-checkbox[@inputid='ApplyDefault']//div[@class='p-checkbox-box']"
        self.DASHBOARD = "//div[@id='p-panel-0-titlebar']//div[@class='checkbox max-width-31 md-space']//div[@class='p-checkbox-box']"
        self.PAYMENTINTEGRATION = "//div[@id='p-panel-1-titlebar']//div[@class='checkbox max-width-31 md-space']//div[@class='p-checkbox-box']"
        self.ONBOARDMERCHANTS = "//div[@id='p-panel-2-titlebar']//div[@class='checkbox max-width-31 md-space']//div[@class='p-checkbox-box']"
        self.ACTIVITYLOGS = "//div[@id='p-panel-3-titlebar']//div[@class='checkbox max-width-31 md-space']//div[@class='p-checkbox-box']"
        self.OTHERCHECKBOXES = "group1"  # Name associated with all checkboxes
        self.SAVETEAM = "//span[normalize-space()='Save']"
        self.SEARCHEDQATEAM = "//label[normalize-space()='QA Team']"

    def click_manageteams(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.LEFTSIDENAVMENU)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.USERACCESSCONTROL)))
        self.driver.execute_script("arguments[0].click()", element)
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.MANAGETEAMS)))
        self.driver.execute_script("arguments[0].click()", element)
        time.sleep(2)

    def add_new_team(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.ADDBUTTON)))
        self.driver.execute_script("arguments[0].click()", element)

    def enter_teamname_desc(self, teamname, teamdesc):
        time.sleep(5)
        self.driver.find_element(By.ID, self.TEAMNAME).send_keys(teamname)
        self.driver.find_element(By.XPATH, self.TEAMDESC).send_keys(teamdesc)
        time.sleep(3)

    def goto_assignusers_tab(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.ASSIGNUSERTAB)))
        self.driver.execute_script("arguments[0].click()", element)

    def searchuser(self, user):
        self.driver.find_element(By.XPATH, self.ASSIGNUSERSEARCHBAR).send_keys(user)

    def check_userin_allusersbox(self):
        username = self.driver.find_element(By.ID, self.ALLUSERSBOX)
        alluserbox = username.find_elements(By.CLASS_NAME,
                                            "p-ripple.p-element.cdk-drag.p-picklist-item.ng-star-inserted")
        if (len(alluserbox)) == 1:
            print("Pass > User found in All User Box")
        else:
            print("Fail > User not found in All User Box")

    def check_userin_assignedusersbox(self):
        username = self.driver.find_element(By.ID, self.ASSIGNEDUSERBOX)
        alluserbox = username.find_elements(By.CLASS_NAME,
                                            "p-ripple.p-element.cdk-drag.p-picklist-item.ng-star-inserted")
        # print(len(alluserbox))
        if (len(alluserbox)) == 1:
            print("Pass > User found in Assigned User Box")
        else:
            print("Fail > User not found in Assigned User Box")

    def move_userto_assignusers(self):
        self.driver.find_element(By.XPATH, self.ASSIGNUSERSEARCHUSERFOUND).click()
        self.driver.find_element(By.XPATH, self.MOVESINGLEBUTTON).click()
        time.sleep(4)

    def select_modules(self):
        self.driver.find_element(By.XPATH, self.MODULESTAB).click()
        self.driver.find_element(By.XPATH, self.DASHBOARD).click()
        getnames = self.driver.find_elements(By.NAME,
                                             self.OTHERCHECKBOXES)  # Getting NAME which is associated with all checkboxes
        getnames[20].click()  # Click on NAME+20th indexing checkbox
        time.sleep(2)
        getnames[32].click()  # Click on NAME+32nd indexing checkbox
        time.sleep(2)

    def save_team(self, qateam):
        self.driver.find_element(By.XPATH, self.SAVETEAM).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.MANAGETEAMSEARCHBAR).click()
        self.driver.find_element(By.XPATH, self.MANAGETEAMSEARCHBAR).send_keys(qateam)
        time.sleep(2)
        getteamname = self.driver.find_element(By.XPATH, self.SEARCHEDQATEAM)
        if getteamname.text == "QA Team":
            print("Team Save & Verified Successfully... ")
