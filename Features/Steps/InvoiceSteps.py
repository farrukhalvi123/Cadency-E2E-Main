import time
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *


@then("User Navigate To Invoice Tab")
def step_impl(context):
    context.cadency.invoice.ClickOnInvoiceTab()


@then("User Clicks On Add Invoice Button")
def step_impl(context):
    context.cadency.invoice.ClickOnAddButton()
@then("Add Customer")
def step_impl(context):
    try:
        context.cadency.invoice.open_customer_selection_dd()
        context.cadency.invoice.select_customer()
    except:
        context.cadency.invoice.open_customer_selection_dd()
        context.cadency.invoice.add_new_customer()
        context.driver.execute_script('''Then Add Customer Details <custom_disp_name> and <firsname> and <lsname> and <phone> and <website> and <ccemail>
    Then Select Customer currency
    Then Verify Toggle Active - InActive
    Then Upload Picture Logo
    Then Add Address Details <Street1> <street2> <pscode>
    And Click on Save Button''')


@then("Select Currency")
def step_impl(context):
    context.cadency.invoice.select_Currency()


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
    context.cadency.invoice.invoice_date()


@then("Select DueDate")
def step_impl(context):
    context.cadency.invoice.invoice_duedate()


@then("Verify Email is prefilled and disabled")
def step_impl(context):
    context.cadency.invoice.emailfield_status()


@then("Verify Invoice Number is disabled")
def step_impl(context):
    context.cadency.invoice.invoice_num_status()
@then("Add an Item")
def step_impl(context):
    context.cadency.invoice.Add_inv_items()


@then("click on Invoice Save Button")
def step_impl(context):
    context.cadency.invoice.Save_invoice()