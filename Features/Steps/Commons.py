from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time

from Constants.URLS import TestData
from Pages.CustomerPages import CustomerPages
from Pages.LoginPage import LoginPage
from Pages.InvoicePage import InvoicePage
from Pages.TemplatePages import TemplatePage


class cadencyweb:
    def __init__(self,driver):
        self.logpage = LoginPage(driver)
        self.customadd = CustomerPages(driver)
        self.invoice = InvoicePage(driver)
        self.template = TemplatePage(driver)


