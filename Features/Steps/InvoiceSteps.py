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
        context.driver.execute_steps('''Then Add Customer Details <custom_disp_name> and <firsname> and <lsname> and <phone> and <website> and <ccemail>
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


@then("Go to Disputed Tab and verify disputed invoices")
def step_impl(context):
    context.cadency.invoice.Disputedtab()
    context.cadency.invoice.disputed_invoices()

@then("Verify Number of Invoices")
def step_impl(context):
    context.cadency.invoice.verify_numberof_invoices()

@then("Go to All Tab")
def step_impl(context):
    context.cadency.invoice.ALLtab()


@then("Go to Open Tab")
def step_impl(context):
    context.cadency.invoice.OpentabINV()

@then("verify All Open Invoices")
def step_impl(context):
    context.cadency.invoice.open_invoices()


@then("Go to Paid Tab")
def step_impl(context):
    context.cadency.invoice.PaidtabINV()


@then("verify All Paid Invoices")
def step_impl(context):
    context.cadency.invoice.paid_invoices()


@then("Go to Partially Paid Invoices")
def step_impl(context):
    context.cadency.invoice.PartiallyPaidtabINV()


@then("Verify Partially Paid Invoices")
def step_impl(context):
    context.cadency.invoice.partially_paid_invoices()


@then("Go to Waiting for Funds Invoices")
def step_impl(context):
    context.cadency.invoice.WaitingfofundsTab()


@then("Verify Waiting for Funds Invoice")
def step_impl(context):
    context.cadency.invoice.waitingforfunds_invoices()


@then("Click on More Options on an invoice")
def step_impl(context):
    context.cadency.invoice.click_moreoptions()


@then("Duplicate an Invoice")
def step_impl(context):
   context.cadency.invoice.duplicate_invoice()


@then("Delete the Invoice")
def step_impl(context):
    context.cadency.invoice.delete_invoice()


@then("Click on View")
def step_impl(context):
    context.cadency.invoice.view_invoice()


@then("Verify Invoice Details")
def step_impl(context):
    context.cadency.invoice.verify_invoice_Details()


@then("Close Left Side Menu")
def step_impl(context):
    context.cadency.invoice.close_leftsidemenu()


@then("Click on Edit Invoice")
def step_impl(context):
    context.cadency.invoice.editinvoice()


@then("Edit Invoice from Detail Page")
def step_impl(context):
    context.execute_steps('''
    Then Enter Reference
    Then Select DueDate
    Then Add Item This is test invoice description
    And Add Items Quantity
    And Adding Item Price
    And Adding Items Discount
    And Select Tax
    Then Verify Amount
    Then Verify Total Amount''')
    context.cadency.invoice.verify_edited_invoice()

@then("Verify Email Sending Details")
def step_impl(context):
        context.cadency.invoice.Verify_Send_Email()




@then("Send Email")
def step_impl(context):
   context.cadency.invoice.send_email()


@then("Verify Sent Email")
def step_impl(context):
   context.cadency.invoice.verify_sent_email()

@then("Verify Invoice Edited Successfully")
def step_impl(context):
    context.cadency.invoice.invoice_Edited_successfully()


@then("Click on Record Payment")
def step_impl(context):
    context.cadency.invoice.record_payment_btn()


@then("Record Payments")
def step_impl(context):
    context.cadency.invoice.fill_record_payments_form()


@then("Record Full Payments")
def step_impl(context):
    context.cadency.invoice.record_full_payment_form()
    context.cadency.invoice.verify_status_InvoiceDetail()


@then("Verify Sent Email and attachment")
def step_impl(context):
   context.cadency.invoice.verify_Thankyouemail_Contents()


@then("Click on Send Reminder")
def step_impl(context):
    context.cadency.invoice.click_reminder()
    time.sleep(5)


@then("Click on Dispute Icon")
def step_impl(context):
    context.cadency.invoice.click_on_dispute()


@then("Verify Invoice Number")
def step_impl(context):
    context.cadency.invoice.verify_invoice_number()


@then("Get Invoice Number and Customer Name")
def step_impl(context):
    context.cadency.invoice.verify_custom_invoice_num()


@then("Verify Customer Name")
def step_impl(context):
    context.cadency.invoice.verify_Customer_Name()


@then("Select reason to dispute")
def step_impl(context):
    context.cadency.invoice.select_reason()


@then("Add amount to dispute")
def step_impl(context):
    context.cadency.invoice.add_disputeamount()


@then("Add a note")
def step_impl(context):
    context.cadency.invoice.add_a_note()

@then("Enter Customer {Name} into Search Field")
def step_impl(context,Name):
   context.cadency.invoice.searchfor_customer(Name)
   time.sleep(10)


@then("Verify list of customer name")
def step_impl(context):
    context.cadency.invoice.verify_search_name()


@then("Click on Export Invoice and verify exported text")
def step_impl(context):
    context.cadency.invoice.export_invoice()


@then("Invoice has Been Created")
def step_impl(context):
    context.execute_steps('''Then User Clicks On Add Invoice Button
    Then Add Customer
    Then Select Currency
    Then Verify Email is prefilled and disabled
    Then Verify Invoice Number is disabled
    Then Enter Reference
    Then Select InvoiceDate
    Then Select DueDate
    Then Select an Item
    Then Add Item This is test invoice description
    And Add Items Quantity
    And Adding Item Price
    And Adding Items Discount
    And Select Tax
    Then Verify Amount
    Then Verify Total Amount
    Then Click on Save Button
    Then Verify amount on detail page''')


@then("Verify Invoice Amount")
def step_impl(context):
    context.cadency.invoice.verify_customer_invoice_amount()


@then("Click on Invoice Sort Button")
def step_impl(context):
   context.cadency.invoice.click_invoicesort()



@then("Verify Invoices are sorted in Descending order")
def step_impl(context):
   time.sleep(4)
   context.cadency.invoice.verifyInvoicesorted()