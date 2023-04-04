import time

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *

@then("Open Right Side Panel")
def step_impl(context):
    time.sleep(10)
    context.cadency.customadd.hover_hamburger()

@then("Go to Customer Tab")
def step_impl(context):
    try:
        time.sleep(2)
        context.cadency.customadd.Go_to_customerTab()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(e + "Test Failed on Customer Tab"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Customer Tab"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Customer Tab"

@then("Click on Add Button")
def step_impl(context):
    try:
        time.sleep(2)
        context.cadency.customadd.click_addbutton()
        context.cadency.customadd.verify_customerform()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(e + "Test Failed on Create Customer form"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Create Customer form"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Create Customer form"


@then("Add Customer Details {custom_disp_name} and {firsname} and {lsname} and {phone} and {website} and {ccemail}")
def step_impl(context,custom_disp_name, firsname,lsname, phone,website, ccemail):
    try:
        context.cadency.customadd.enter_customerDetails(custom_disp_name, firsname,lsname, phone,website, ccemail)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(e + "Test Failed on customer form"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on customer form"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on customer form"

@then("Upload Picture Logo")
def step_impl(context):
    try:
         context.cadency.customadd.upload_logo()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(e + "Test Failed on Upload Picture"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on customer form"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on customer form"


@then("Add Address Details {Street1} {street2} {pscode}")
def step_impl(context, Street1, street2, pscode):
    try:
        context.cadency.customadd.enter_address(Street1, street2, pscode)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(e + "Test Failed on Addres Details"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Addres Details"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Addres Details"


@step("Click on Save Button")
def step_impl(context):
    context.cadency.customadd.click_save()


@then("Verify New User has been added")
def step_impl(context):
    context.cadency.customadd.verify_new_user_successfully_added()

@then("Verify Customer Email")
def step_impl(context):
    context.cadency.customadd.customer_email()


@then("Customer is already added in the system")
def step_impl(context):
    context.cadency.customadd.verify_customers_present()


@then("Click on 3 dots and open edit customer form")
def step_impl(context):
    context.cadency.customadd.edit_Customer()



@then("Edit Customer Details")
def step_impl(context):
    context.execute_steps("""
    Then Add Customer Details Selina and Kyle and alv and 0300 4589878 and https://www.hogoogle.com and aa@aaj.com
    Then Upload Picture Logo
    Then Add Address Details 13231teststreet abcxystreet 2254
    And Click on Save Button""")



@then("Verify Details have been updated")
def step_impl(context):
    context.cadency.customadd.updated_customerdata()


@then("click on Filter")
def step_impl(context):

    context.cadency.customadd.select_filter()


@then("Select Country")
def step_impl(context):
    context.cadency.customadd.select_country()


# @then("Select Invoice Status")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: Then Select Invoice Status')
#
#
# @then("Select customer Status")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: Then Select customer Status')


# @step("Click on Apply Button")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: And Click on Apply Button')


@then("Verify Filter is applied")
def step_impl(context):
    context.cadency.customadd.click_applybutton()
    context.cadency.customadd.verify_customers_of_selected_countries()


@then("Verify Toggle Active - InActive")
def step_impl(context):
    context.cadency.customadd.handle_toggle()


@then("Verify Currency Selected and Disabled")
def step_impl(context):
    context.cadency.customadd.verify_currency_added()


@then("Select Customer currency")
def step_impl(context):
    context.cadency.customadd.select_customer_currency()


@then("View Customer Details")
def step_impl(context):
    context.cadency.customadd.click_view()



@then("Verify Invoice Tiles")
def step_impl(context):
    context.cadency.customadd.verify_invoice_tiles()


@then("Verify Open Invoices")
def step_impl(context):
    context.cadency.customadd.verify_openInvoices()


@then("Identify Number of Existing Customers")
def step_impl(context):
    context.cadency.customadd.customer_number()


@then("Search for {name} and verify results")
def step_impl(context,name):
    context.cadency.customadd.search_customer(name)


@then("Select Invoice Status")
def step_impl(context):
    context.cadency.customadd.apply_invoice_filter()


@then("Select Customer Status")
def step_impl(context):
    context.cadency.customadd.apply_customer_Filter()


@then("Verify Invoices with Current Status")
def step_impl(context):
    context.cadency.customadd.vefify_Current_status_filter()


@then("Verify Closed Invoices")
def step_impl(context):
   context.cadency.customadd.verify_closedInvoices()


@then("Verify Invoices with Payments received")
def step_impl(context):
    context.cadency.customadd.verify_paidinvoices()


@then("Verify Credit Notes")
def step_impl(context):
    context.cadency.customadd.verify_creditnotes()


@then("Verify Number of Tasks")
def step_impl(context):
    context.cadency.customadd.verify_Task()


@then("Verify Customer Details on Listing Page")
def step_impl(context):
    context.cadency.customadd.customer_listings()


@then("Verify Customer Details on Details Page")
def step_impl(context):
    context.cadency.customadd.customer_details()