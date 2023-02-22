from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time

from Constants.URLS import TestData
from Pages.Admin_LoginPage import AdminLoginPage
from Pages.CustomerPages import CustomerPages
from Pages.LoginPage import LoginPage
from Pages.InvoicePage import InvoicePage
from Pages.Admin_ForgotPass import AdminForgotPass
from Pages.Admin_ManageUsers import AdminAddUsers
from Pages.Admin_ManageTeams import ManageTeams
from Pages.TemplatePages import TemplatePage
from Pages.Admin_VerifyModules_Permissions import VerifyPermissions
from Pages.Admin_OnboardMerchant import OnboardingMerchant


class cadencyweb:
    def __init__(self, driver):
        self.driver = driver
        # Merchant Portal Pages
        self.logpage = LoginPage(driver)
        self.customadd = CustomerPages(driver)
        self.invoice = InvoicePage(driver)
        self.templates = TemplatePage(driver)
        # Admin Portal Pages
        self.admin_man_login = AdminLoginPage(driver)
        self.admin_forgot_pass = AdminForgotPass(driver)
        self.admin_add_users = AdminAddUsers(driver)
        self.admin_manage_teams = ManageTeams(driver)
        self.admin_verify_permissions = VerifyPermissions(driver)
        self.admin_onboarding_merchant = OnboardingMerchant(driver)
