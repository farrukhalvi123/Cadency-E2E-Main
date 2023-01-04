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


@then("Click on forgot password button")
def step_impl(context):
    context.cadency.admin_forgot_pass.click_on_forgotpass()
    time.sleep(5)
