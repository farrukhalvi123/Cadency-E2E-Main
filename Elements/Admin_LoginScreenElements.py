from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class AdminportalElements(BasePage):
    USERNAME = (By.ID, "login-email")
    PASSWORD = (By.XPATH, "//input[@placeholder='Enter Password']")
    LOGINBUTTON = (By.XPATH, "//button[@type='submit']")
    PROFILEPICCLICK = (By.XPATH, "//span[@class='p-button-link ml-2 font-semibold flex align-items-center']")
    LOGOUTBUTTON = (By.XPATH, "//a[normalize-space()='Logout']")
    FORGOT_PASSWORD = (By.XPATH, "//span[normalize-space()='Forgot Password?']")

    # General Elements
    LEFTSIDENAVMENU = (By.XPATH, "//div[@class='side-navigation-menu-container half-content']")

    # Add New User
    USERACCESSCONTROL = (By.XPATH, "//p[normalize-space()='User Access Control']")
    MANAGEUSERS = (By.XPATH, "//p[normalize-space()='Manage Users']")
    ADDBUTTON = (By.XPATH, "//span[normalize-space()='Add +']")
    FIRSTNAME = (By.ID, "firstName")
    LASTNAME = (By.ID, "lastName")
    ADDUSER_USERNAME = (By.ID, "username")
    PHONE = (By.ID, "phone")
    EMAIL = (By.ID, "email")
    ADDUSER_PASSWORD = (By.XPATH, "//input[@placeholder=' Enter your Password']")
    ADDUSER_CONFPASSWORD = (By.XPATH, "//input[@placeholder=' Enter your Confirm Password']")
    TEAMSDD = (By.XPATH, "//*[contains(@class,'p-multiselect-label ng-tns')]")  # Dynamic XPATH
    TEAMSTYPEAREA = (By.XPATH, "//input[@role='textbox']")
    SELECTTESTTEAMCHECKBOX = (By.XPATH, "//span[normalize-space()='test']")
    SELECTTEST2TEAMCHECKBOX = (By.XPATH, "//label[normalize-space()='test3']")
    USERTYPEDD = (By.XPATH, "//*[contains(@class,'p-dropdown-trigger-icon ng-tns')]")  # Dynamic XPATH
    SUPERADMIN = (By.XPATH, "//span[normalize-space()='Super Admin']")
    STANDARD = (By.XPATH, "//span[normalize-space()='Standard']")
    STATUS_ACTIVE = (By.XPATH, "//span[normalize-space()='Active']")
    STATUS_INACTIVE = (By.XPATH, "//span[normalize-space()='Inactive']")
    SAVEBUTTON = (By.XPATH, "//span[normalize-space()='Save']")

    # Users Listing Page Elements
    MANAGEUSERSSEARCHBAR = (By.XPATH, "//input[@id='searchText']")
    MBAPPEXPATH = (By.XPATH, "//h3[normalize-space()='Kylian Mbappe']")
    NORECORDFOUND = (By.XPATH, "//div[@class='title-heading-3']")
    CLEARFILTERBUTTON = (By.XPATH, "//span[normalize-space()='Clear Filter']")
    ACTIONBUTTON = (By.XPATH, "//i[@class='pi pi-ellipsis-v text-orange-500']")
    EDITBUTTON = (By.XPATH, "//a[normalize-space()='Edit']")

    # Filter Elements
    FILTERICON = (By.XPATH, "//i[@class='pi pi-filter']")
    USERSTATUSEDD = "//*[contains(@class,'p-dropdown-trigger-icon ng-tns')]"  # Dynamic XPATH
    SELECTACTIVE = (By.XPATH, "//span[normalize-space()='Active']")
    SELECTINACTIVE = (By.XPATH, "//span[normalize-space()='Inactive']")
    TEAMSEARCHBAR = (By.XPATH, "//*[contains(@class,'p-dropdown-filter p-inputtext p-component ng-tns')]")  # Dynamic XPATH
    ENTERTEAMNAME = (By.XPATH, "//span[normalize-space()='test']")
    APPLYBUTTON = (By.XPATH, "//button[normalize-space()='Apply']")
