import time
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *


@then("User Navigate To Invoice Tab")
def step_impl(context):
    context.invoice.ClickOnInvoiceTab()


@then("User Clicks On Add Invoice Button")
def step_impl(context):
    context.invoice.ClickOnAddButton()
@then("Add Customer")
def step_impl(context):
    context.invoice.select_customer()


@then("Select Currency")
def step_impl(context):
    context.invoice.select_Currency()


@then("Select Exchange Rate")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Select Exchange Rate')


@then("Enter Reference")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Enter Reference')


@then("Select InvoiceDate")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Select InvoiceDate')


@then("Select DueDate")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Select DueDate')