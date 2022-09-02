import time
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *


@then("User Navigate To Invoice Tab")
def step_impl(context):
    context.invoice.ClickOnInvoiceTab()


@then("User Clicks On Add Invoice Button")
def step_impl(context):
    context.Invoice.ClickOnAddButton()
