import time
from behave import *


from behave import *




@when("customer at dashboard and hover over side panel and click invoice option")
def hovering_sidepanel(context):
        context.cadency.Verify_DisputeTag.hovering()
        time.sleep(5)


@then("search dispute tagged invoice and save the catched inv number")
def step_impl(context):
        context.cadency.Verify_DisputeTag.catch_tag()
        time.sleep(6)
