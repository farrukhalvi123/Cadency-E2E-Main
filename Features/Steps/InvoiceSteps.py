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





@then("Enter Reference")
def step_impl(context):
    context.cadency.invoice.enter_references()


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
@then("Select an Item")
def step_impl(context):
    context.cadency.invoice.Add_inv_items()


@then("click on Invoice Save Button")
def step_impl(context):
    context.cadency.invoice.Save_invoice()


@then("Verify Invoice has been Created")
def step_impl(context):
    context.cadency.invoice.verify_invoiceCreated()


@then("Add Item {Description}")
def step_impl(context, Description):
    context.cadency.invoice.add_item_description(Description)
    time.sleep(2)



@step("Add Items Quantity")
def step_impl(context):
   context.cadency.invoice.enter_quantity()
   time.sleep(2)


@step("Adding Item Price")
def step_impl(context):
    context.cadency.invoice.enter_price()


@step("Adding Items Discount")
def step_impl(context):
    context.cadency.invoice.enter_discount()


@step("Select Tax")
def step_impl(context):
    context.cadency.invoice.select_tax("gst", "20%")


@then("Verify Amount")
def step_impl(context):
    context.cadency.invoice.invoice_amount()

@then("Verify Total Amount")
def step_impl(context):
    context.cadency.invoice.total_amount()


@then("Verify amount on detail page")
def step_impl(context):
    context.cadency.invoice.verify_total_amount()


@then("Enter Invoice Number in Search Field")
def step_impl(context):
    context.cadency.invoice.search_invoice()


@then("Verify Searched Invoice is Found")
def step_impl(context):
    context.cadency.invoice.Verify_Searched_Invoice()


@then("Click on Download Invoices in Excel")
def step_impl(context):
   context.cadency.invoice.clickCSVIcon()


@then("Click on Download Invoices in PDF")
def step_impl(context):
    context.cadency.invoice.verify_pdffile()


@then("Select Action Button")
def step_impl(context):
   context.cadency.invoice.download_oneinvoice()


@then("Click on PDF File Download")
def step_impl(context):
    context.cadency.invoice.clickPDFIcon()


@then("Verify Downloaded CSV")
def step_impl(context):
    context.cadency.invoice.Download_Excelfile()