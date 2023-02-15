#
# from selenium.webdriver.common.by import By
#
#
# class VerifyPermissionsElements():
#     USERNAME = (By.ID, "login-email")
#     PASSWORD = (By.XPATH, "//input[@placeholder='Enter Password']")
#     LOGINBUTTON = (By.XPATH, "//button[@type='submit']")
#     LEFTSIDENAVMENU = (By.XPATH, "//div[@class='side-navigation-menu-container half-content']")
#     DASHBOARD = (By.XPATH, "//p[normalize-space()='Dashboard']")
#     USERACCESSCONTROL = (By.XPATH, "//p[normalize-space()='User Access Control']")
#     PAYMENTINTEGRATION = (By.XPATH, "//p[normalize-space()='Payment Integrations']")
#     ONBOARDMERCHANT = (By.XPATH, "//p[normalize-space()='Onboard Merchants']")
#     ACTIVITYLOGS = (By.XPATH, "//p[normalize-space()='Activity Logs']")
#
#     # Verifying Available Dashboard Options
#     ONBOARDMERCHANTTILE = (By.XPATH, "//h3[normalize-space()='Onboarded Merchants']")
#     PENDINGMERCHANTTILE = (By.XPATH, "//h3[normalize-space()='Pending Merchants']")
#     TOTALUSERSTILE = (By.XPATH, "//h3[normalize-space()='Total Users']")
#     TOTALTEAMTILE = (By.XPATH, "//h3[normalize-space()='Total Teams']")
#     MERCHANTSUMMARYTILE = (By.XPATH, "//h3[normalize-space()='Merchant Summary']")
#     MYACTIVITIESTILE = (By.XPATH, "//h3[normalize-space()='My Activities']")
#     MERCHANTCOUNTRIESTILE = (By.XPATH, "//h3[normalize-space()='Merchants By Country']")
#     MYTASKTILE = (By.XPATH, "//h3[normalize-space()='My Task']")
#
#     # Verifying Edit Option in Merchants
#
#     MERCHANTACTIONBUTTON = (By.XPATH,
#                             "//body[1]/app-root[1]/app-features[1]/div[1]/div[1]/div[1]/app-entity-list[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[6]/div[1]/button[1]/i[1]")
#     EDITBUTTON = (By.XPATH, "//a[normalize-space()='Edit']")
#
#     # Verifying Activity Logs (Labels)
#
#     LEVELS = (By.XPATH, "//div[normalize-space()='Levels']")
#     MODULE = (By.XPATH,
#               "//div[@class='col-2 font-semibold flex justify-content-none lg:justify-content-center white-space-nowrap']")
#     DESC = (By.XPATH, "//div[@class='col-4 font-semibold white-space-nowrap']")
#     IPADD = (By.XPATH, "//div[normalize-space()='IP Addess']")
#     LOGGEDBY = (By.XPATH, "//div[@class='col-2 font-semibold white-space-nowrap']")
#     DATETIME = (By.XPATH, "//div[normalize-space()='Date & Time']")
#
#     # Goto Profile
#     CLICKONNAME = (By.XPATH, "//i[@class='pi pi-chevron-down ml-1']")
#     PROFSETTINGS = (By.XPATH, "//a[normalize-space()='Profile Settings']")
#     FNAME = (By.XPATH, "//input[@id='firstName']")
#     LNAME = (By.XPATH, "//input[@id='firstName']")
#
#     # Verifying Activity Logs (1st Row Data)
#
#     INFO = (By.XPATH, "//body/app-root/app-features[@class='ng-star-inserted']/div[@class='feature-container']/div[@class='main-body-content']/div[@class='page-content']/app-activity-logs-list[@class='ng-star-inserted']/div[@class='container-wrapper']/div/div/div[2]/div[1]/div[1]/span[1]")
#     USER = (By.CLASS_NAME, "status-container module-status status-blue3")
#     USERLOGINSUCCESSFULLY = (By.CLASS_NAME, "custom-twolines-ellipsis")
#     IP = (By.CLASS_NAME, "font-semibold lg:hidden")
#     LOGINSUER = (By.CLASS_NAME, "loggedby-text")
