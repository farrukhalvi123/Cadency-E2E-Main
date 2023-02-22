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
from Features.Steps.Commons import cadencyweb


@then("Click On Add Merchant")
def step_impl(context):
    context.cadency.admin_onboarding_merchant.click_addmerchant_button()


@then("Fill Onboard Merchant Form {Name}, {Business_Phone}, {Website}, {Email}, {Zipcode}")
def step_impl(context, Name, Business_Phone, Website, Email, Zipcode):
    context.cadency.admin_onboarding_merchant.filling_form(Name, Business_Phone, Website, Email, Zipcode)


@then("Select Business Type")
def step_impl(context):
    context.cadency.admin_onboarding_merchant.select_businesstype()


@then("Select Industry")
def step_impl(context):
    context.cadency.admin_onboarding_merchant.select_industry()


@then("Select Merchant Country")
def step_impl(context):
    context.cadency.admin_onboarding_merchant.select_merchant_country()


@then("Select Merchant State/Province")
def step_impl(context):
    context.cadency.admin_onboarding_merchant.select_merchant_state()


@then("Select Merchant City")
def step_impl(context):
    context.cadency.admin_onboarding_merchant.select_merchant_city()


@then("Select Merchant Currency")
def step_impl(context):
    context.cadency.admin_onboarding_merchant.select_merchant_currency()


@then("Select Merchant Invoice Mode")
def step_impl(context):
    context.cadency.admin_onboarding_merchant.select_merchant_invoicemode()


@then("Select Merchant Status")
def step_impl(context):
    context.cadency.admin_onboarding_merchant.select_merchant_status()


@then("Enable Billing Center")
def step_impl(context):
    context.cadency.admin_onboarding_merchant.enable_bc()


@then("Upload Merchant Logo")
def step_impl(context):
    context.cadency.admin_onboarding_merchant.upload_merchant_logo()


@then("Save Merchant")
def step_impl(context):
    context.cadency.admin_onboarding_merchant.save_merchant()