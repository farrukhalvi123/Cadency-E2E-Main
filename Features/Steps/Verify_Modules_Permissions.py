import time
import pyodbc
import wmi
from selenium.webdriver.common.keys import Keys
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
from socket import *
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from Constants.URLS import TestData
from Pages.Verify_Modules_Permissions import VerifyPermissions


@then("Enters Cred {NinjaTurtle} and {Talha123} and login into system")
def step_impl(context, NinjaTurtle, Talha123):
    # try:
    context.cadency.admin_verify_permissions.enter_addusername(NinjaTurtle)
    context.cadency.admin_verify_permissions.enter_adpassword(Talha123)
    context.cadency.admin_verify_permissions.click_loginbutton()
    time.sleep(3)
    # admin_verify_permission


@then("Open Left Panel")
def step_impl(context):
    context.cadency.admin_verify_permissions.open_left_panel()


@then("Click On Dashboard")
def step_impl(context):
    try:
        context.cadency.admin_verify_permissions.click_on_dashboard()
    except Exception as e:
        print("FAIL > Dashboard Option Not Found")


@then("Click On Onboard Merchants")
def step_impl(context):
    try:
        context.cadency.admin_verify_permissions.click_on_onboardmerchants()
    except Exception as e:
        print("FAIL > Onboard Merchants Option Not Found")


@then("Click On Activity Logs")
def step_impl(context):
    try:
        context.cadency.admin_verify_permissions.click_on_actlogs()
    except Exception as e:
        print("FAIL > Activity Logs Option Not Found")


@then("Click On User Access Control")
def step_impl(context):
    try:
        context.cadency.admin_verify_permissions.click_on_uac()
    except Exception as e:
        print("PASS > User Access Control Option Not Found")


@then("Click On PAYMENT INTEGRATION")
def step_impl(context):
    try:
        context.cadency.admin_verify_permissions.click_on_pi()
    except Exception as e:
        print("PASS > Payment Integration Option Not Found")


@then("Verify Onboarded Merchants Tile")
def step_impl(context):
    try:
        context.cadency.admin_verify_permissions.click_on_obmtile()
    except Exception as e:
        print("Fail > Onboarded Merchants Tile Not Found")


@then("Verify Pending Merchants Tile")
def step_impl(context):
    try:
        context.cadency.admin_verify_permissions.click_on_pmtile()
    except Exception as e:
        print("Fail > OPending Merchants Tile Not Found")


@then("Verify Total Users Tile")
def step_impl(context):
    try:
        context.cadency.admin_verify_permissions.click_on_tutile()
    except Exception as e:
        print("PASS > Total Users Tile Not Found")


@then("Verify Total Teams Tile")
def step_impl(context):
    try:
        context.cadency.admin_verify_permissions.click_on_tttile()
    except Exception as e:
        print("PASS > Total Teams Tile Not Found")


@then("Verify Merchant Summary Tile")
def step_impl(context):
    try:
        context.cadency.admin_verify_permissions.click_on_mstile()
    except Exception as e:
        print("Fail > Merchant Summary Tile Not Found")


@then("Verify My Activities Tile")
def step_impl(context):
    try:
        context.cadency.admin_verify_permissions.click_on_matile()
    except Exception as e:
        print("Fail > My Activities Tile Not Found")


@then("Verify Merchant By Country Tile")
def step_impl(context):
    try:
        context.cadency.admin_verify_permissions.click_on_mbctile()
    except Exception as e:
        print("Fail > Merchants By Country Tile Not Found")


@then("Verify My Task Tile")
def step_impl(context):
    try:
        context.cadency.admin_verify_permissions.click_on_mttile()
    except Exception as e:
        print("Fail > My Task Tile Not Found")


@then("Verify Edit option In Merchants")
def step_impl(context):
    try:
        context.cadency.admin_verify_permissions.verifying_edit_option()
    except Exception as e:
        print("PASS > Edit Button Not Found")


@then("Verify Data Of Labels")
def step_impl(context):
    try:
        context.cadency.admin_verify_permissions.verifying_Labels()
    except Exception as e:
        print("FAIL > Something Went Wrong...")


@then("Verify 1st Row Data")
def step_impl(context):
    # try:
    context.cadency.admin_verify_permissions.verifying_Firstrow()
# except Exception as e:
#     print("FAIL > Something Went Wrong...")
