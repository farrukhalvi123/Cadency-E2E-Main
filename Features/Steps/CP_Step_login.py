import time

from behave import *




@when("user is at customer portal")
def step_impl(context):
    context.cadency.CustomerPortal.go_to_login()
    time.sleep(4)





@then("customer enter {uname} and {pswd}")
def step_impl(context,uname,pswd):
    context.cadency.CustomerPortal.enter_username1(uname)
    context.cadency.CustomerPortal.enter_password1(pswd)


@then("customer clicks login button")
def step_impl(context):
    context.cadency.CustomerPortal.login_button()
