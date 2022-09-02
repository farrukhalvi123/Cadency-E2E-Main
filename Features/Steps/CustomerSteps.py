import time

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
@then("Go to Customer Tab")
def step_impl(context):
    try:
        context.customadd.Go_to_customerTab()
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
        context.customadd.click_addbutton()
        context.customadd.verify_customerform()
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


@then("Add Customer Details {custom_disp_name} and {firsname} and {lsname} and {phone} and {mail} and {website} and {ccemail}")
def step_impl(context,custom_disp_name, firsname,lsname, phone,mail,website, ccemail):
    try:
        context.customadd.enter_customerDetails(custom_disp_name, firsname,lsname, phone,mail,website, ccemail)
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
         context.customadd.upload_logo()
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
        context.customadd.enter_address(Street1, street2, pscode)
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
    context.customadd.click_save()


@then("Verify New User has been added")
def step_impl(context):
    context.customadd.verify_new_user_successfully_added()

@then("Verify Customer Number")
def step_impl(context):
    context.customadd.customer_number()


@then("Customer is already added in the system")
def step_impl(context):
    context.customadd.verify_customers_present()


@then("Click on 3 dots and open edit customer form")
def step_impl(context):
    context.customadd.edit_Customer()



@then("Edit Customer Details")
def step_impl(context):
    context.execute_steps("""Then Verify Customer Number 
    Then Add Customer Details amir and amir and alv and 0300 4589876 and aa@aaj.com and https://www.hogoogle.com and aa@aaj.com
    Then Upload Picture Logo
    Then Add Address Details 13231teststreet abcxystreet 2254
    And Click on Save Button""")



@then("Verify Details have been updated")
def step_impl(context):
    context.customadd.updated_customerdata()


@then("click on Filter")
def step_impl(context):

    context.customadd.select_filter()


@then("Select Country")
def step_impl(context):

    context.customadd.select_country()


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
    context.customadd.click_applybutton()
    context.customadd.verify_customers_of_selected_countries()


@then("Verify Toggle Active - InActive")
def step_impl(context):
    context.customadd.handle_toggle()