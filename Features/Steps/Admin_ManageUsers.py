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
from Pages.LoginPage import LoginPage


@then("Enters Credentials {Talhaadmin} and {Talha123} and login into system")
def step_impl(context, Talhaadmin, Talha123):
    # try:

    context.cadency.admin_man_login.enter_adusername(Talhaadmin)
    context.cadency.admin_man_login.enter_adpassword(Talha123)
    context.cadency.admin_man_login.click_loginbutton()
    time.sleep(3)


@then("Open Left Side Panel")
def step_impl(context):
    context.cadency.admin_add_users.hoverleftnavmenu()
    time.sleep(2)


@given("Click On Add New User Button")
def step_impl(context):
    # try:
    context.cadency.admin_add_users.click_on_addbutton()


@then("Add User Details {Fname} and {Lname} and {AdminUname} and {PhnNum} and {Email} and {Pass} and {Cpass}")
def step_impl(context, Fname, Lname, AdminUname, PhnNum, Email, Pass, Cpass):
    try:
        context.cadency.admin_add_users.adduserdetails(Fname, Lname, AdminUname, PhnNum, Email, Pass, Cpass)
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
        assert False, "Test Failed on add admin user form"


@then("Click On Teams DD")
def step_impl(context):
    context.cadency.admin_add_users.click_on_teamsdd()


@then("Select Team {Teamname}")
def step_impl(context, Teamname):
    context.cadency.admin_add_users.enter_team_name(Teamname)


@then("Select UserType DD")
def step_impl(context):
    try:
        context.cadency.admin_add_users.selectusertype()
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
        assert False, "Test Failed on add admin user form"


@then("Select User Status")
def step_impl(context):
    try:
        context.cadency.admin_add_users.selectuserstatus()
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
        assert False, "Test Failed on add admin user form"


@then("Save")
def step_impl(context):
    try:
        context.cadency.admin_add_users.click_on_savebutton()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(e + "Test Failed on customer form"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        print("Fail > Checking Add User Flow: User Unable To Save")
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on customer form"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on add admin user form"


@given("Enter text in search field {text}")
def step_impl(context, text):
    context.cadency.admin_add_users.check_user_exist(text)


@then("Verify Username if Already Exist")
def step_impl(context):
    try:
        context.cadency.admin_add_users.verify_user()
    except:
        print("Enter In Exception")
    #   context.execute_steps('''Given Click On Add New User Button
    # Then Add User Details Kylian and Mbappe and NinjaTurtle and +923212323777 and ninja@yopmail.com and Talha123 and Talha123
    # Then Click On Teams DD
    # Then Select Team Test
    # Then Select UserType DD
    # Then Select User Status

    # Then Save''')


@then("Verify No Record Found Text")
def step_impl(context):
    try:
        context.cadency.admin_add_users.verify_no_record_found()
        print("Pass > Checking Clear Filter Button: No Record Found On "
              "Dummy Text On Search Bar")
    except:
        print("Fail > Checking Clear Filter Button: Some Records Found "
              "/ On Dummy Text In Search Bar...")


@then("Verify Some Record")
def step_impl(context):
    try:
        context.cadency.admin_add_users.verify_users_found()
        print("Fail > Checking Clear Filter Button: No Record Found "
              "After Clicking On Clear Filter Button")
    except:
        print("Pass > Checking Clear Filter Button: Some Records Found "
              "/ After Clicking On Clear Filter Button...")


@then("Click Clear Filter Button")
def step_impl(context):
    context.cadency.admin_add_users.click_clearfilter_button()


@then("Click On Filter Icon")
def step_impl(context):
    context.cadency.admin_add_users.click_on_filtericon()


@then("Select User Status Filter Option (Active)")
def step_impl(context):
    context.cadency.admin_add_users.select_user_status_active()


@then("Select Filter By Team {test}")
def step_impl(context, test):
    context.cadency.admin_add_users.select_filterby_team(test)


@then("Click on Apply Button")
def step_impl(context):
    context.cadency.admin_add_users.click_on_apply_button()


@then("Check Filter Results")
def step_impl(context):
    try:
        context.cadency.admin_add_users.filter_results()
    except:
        print("User Status Is Inactive, Make it Active First Then Run Again")


@then("Make User Inactive")
def step_impl(context):
    context.cadency.admin_add_users.make_user_inactive("Automationtestuser")


@then("Select User Status Filter Option (InActive)")
def step_impl(context):
    try:
        context.cadency.admin_add_users.select_user_status_Inactive()
    except:
        print("Unable To Change User Status... Something Wrong Here...")
