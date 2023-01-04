import time
import pyodbc
import wmi
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
from socket import *
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from Constants.URLS import TestData
from Pages.LoginPage import LoginPage


@then("User Navigates to Admin Portal")
def step_impl(context):
    try:
        context.cadency.admin_man_login.go_to_admin()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(e + "Test Failed on HomePage Verification"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on HomePage Verification"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on HomePage Verification"


@then("Admin User Enters {Uname} and {Pword} and login into system")
def step_impl(context, Uname, Pword):
    # try:

    context.cadency.admin_man_login.enter_adusername(Uname)
    context.cadency.admin_man_login.enter_adpassword(Pword)
    context.cadency.admin_man_login.click_loginbutton()
    time.sleep(3)


@then("Verify User Navigation to Dashboard or Not.")
def step_impl(context):
    currenturl = context.driver.current_url
    DashboardUrl = TestData.CADENCY_MANAGEMENT_DASHBOARD

    if currenturl == DashboardUrl:
        print("Test Case Pass")
    else:
        print("Test Case Fail")


@then("Click on Admin Profile Thumbnail")
def step_impl(context):
    context.cadency.admin_man_login.click_profpic()


@then("AdminLogout")
def step_impl(context):
    context.cadency.admin_man_login.click_Adminlogout()


@then("Check Url after entering incorrect username")
def step_impl(context):

    currenturl = context.driver.current_url
    DashboardUrl = TestData.CADENCY_MANAGEMENT_DASHBOARD

    if currenturl == DashboardUrl:
        print("Test Case Fail")
    else:
        print("Test Case Pass")


@then("Check Url after entering incorrect password")
def step_impl(context):
    currenturl = context.driver.current_url
    DashboardUrl = TestData.CADENCY_MANAGEMENT_DASHBOARD

    if currenturl == DashboardUrl:
        print("Test Case Fail")
    else:
        print("Test Case Pass")

