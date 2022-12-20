import time
import pyodbc
import wmi
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
from socket import *
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

from Pages.LoginPage import LoginPage


@given("User is at login Page")
def step_impl(context):
    try:
        context.cadency.logpage.verify_hompage()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(e + "Test Failed on HomePage Verification"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on HomePage Verification"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on HomePage Verification"

@then("User Enters {Uname} and {Pword}")
def step_impl(context,Uname,Pword):
    # try:

         context.cadency.logpage.enter_username(Uname)
         context.cadency.logpage.enter_password(Pword)
    # except Exception as e:
    #     attach(context.driver.get_screenshot_as_png(),
    #            name=str(e + "Test Failed on Login"),
    #            attachment_type=AttachmentType.PNG)
    #     context.driver.close()
    #     assert False, e
    # except:
    #     attach(context.driver.get_screenshot_as_png(), name=str("TTest Failed on Login"),
    #            attachment_type=AttachmentType.PNG)
    #     context.driver.close()
    #     assert False, "Test Failed on Login"


@then("User Clicks on Login Button")
def step_impl(context):
    try:
     context.cadency.logpage.click_login()
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(e + "Test Failed on Login Button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Login Button"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Login Button"



@then("Verify User Navigation to HomePage or Error.")
def step_impl(context):
     try:
        context.cadency.logpage.verify_postloginhomepage()
     except Exception as e:
         attach(context.driver.get_screenshot_as_png(),
                name=str(e + "Test Failed on Homepage"),
                attachment_type=AttachmentType.PNG)
         context.driver.close()
         assert False, e
     except:
         attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Homepage"),
                attachment_type=AttachmentType.PNG)
         context.driver.close()
         assert False, "Test Failed on Homepage"

@then("Click on Profile Thumbnail")
def step_impl(context):
    context.cadency.logpage.click_profilethumbnail()

@then("Logout")
def step_impl(context):
    context.cadency.logpage.click_logout()


@then("click on forgot password")
def step_impl(context):
    context.cadency.logpage.click_forgetpass()


@then("Enter {Email} to recover password")
def step_impl(context,Email):
    context.cadency.logpage.enter_email(Email)
@then("Click on Send button")
def step_impl(context):
    context.cadency.logpage.click_send()

@then("Verify Forgot Password {Email}")
def step_impl(context,Email):
    context.cadency.logpage.enter_email(Email)
    context.cadency.logpage.click_send()
    time.sleep(5)
    print(Email)
    ip = '10.4.4.21'
    username = 'CADENCY/Farrukh.alvi'
    password = 'Lb9QcNLH'
    try:
        print("Establishing connection to %s" % ip)
        connection = wmi.WMI(ip, user=username, password=password)
        print("Connection established")
    except wmi.x_wmi:
        print("Your Username and Password of " + getfqdn(ip) + " are wrong.")
    cnxn_str = (r"DRIVER= 10.4.4.21 ;"
                r"SERVER=CADENCYDEV002\\SQLEXPRESS;"
                "User ID=sa;"
                "Password=#cadencyct786; "
                "Trusted_Connection=yes;")
    cnxn = pyodbc.connect(cnxn_str)
    sql = 'Select forgotPasswordToken from users where email = %s'
    data1 = pd.read_sql(sql, (Email))
    dataresult = data1.fetchall()
    print(dataresult[0])
    context.cadency.logpage.enter_code(dataresult[0])





# @then("Fetch New OTP Code")
# def step_impl(context):
#     try:



@then("Enter New Password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Enter New Password')


@then("Enter Current Password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Enter Current Password')


@then("Click on Change password Button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Click on Change password Button')


@then("User Navigates to Merchant Portal")
def step_impl(context):
    context.cadency.logpage.go_to_main()