import time

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from behave import *



@then("Go to Settings Gears")
def step_impl(context):
    context.cadency.templates.click_settingsgear()


@then("Click on Templates")
def step_impl(context):
    context.cadency.templates.select_template()
    time.sleep(5)


@then("Click on Add Template")
def step_impl(context):
    context.cadency.templates.click_addtemplate()


@then("User Enter Template {Name}")
def step_impl(context,Name):
    # try:
        context.cadency.templates.enter_templatename(Name)
        time.sleep(5)
    # except Exception as e:
    #     attach(context.driver.get_screenshot_as_png(),
    #            name=str(e + "Test Failed on Homepage"),
    #            attachment_type=AttachmentType.PNG)
    #     context.driver.close()
    #     assert False, e
    #
    # except:
    #     attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on Homepage"),
    #        attachment_type=AttachmentType.PNG)
    # context.driver.close()
    # assert False, "Test Failed on Homepage"
