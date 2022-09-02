import time

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *
from webdriver_manager.chrome import ChromeDriverManager


@given("User is at login Page")
def step_impl(context):
    try:
        context.loginPage.verify_hompage()
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
    try:
         context.loginPage.enter_username(Uname)
         context.loginPage.enter_password(Pword)
    except Exception as e:
        attach(context.driver.get_screenshot_as_png(),
               name=str(e + "Test Failed on Login"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, e
    except:
        attach(context.driver.get_screenshot_as_png(), name=str("TTest Failed on Login"),
               attachment_type=AttachmentType.PNG)
        context.driver.close()
        assert False, "Test Failed on Login"


@then("User Clicks on Login Button")
def step_impl(context):
    try:
     context.loginPage.click_login()
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
        context.loginPage.verify_postloginhomepage()
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
    context.loginPage.click_profilethumbnail()

@then("Logout")
def step_impl(context):
    context.loginPage.click_logout()
