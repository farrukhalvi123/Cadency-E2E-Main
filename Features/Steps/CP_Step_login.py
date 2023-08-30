import time

from behave import *




@when("user is at customer portal")
def step_impl(context):
    context.cadency.Cportal_login.go_to_login()
    time.sleep(4)






@then("customer enter {uname} and {pswd}")
def step_impl(context,uname,pswd):
    context.cadency.Cportal_login.enter_username1(uname)
    context.cadency.Cportal_login.enter_password1(pswd)


@then("customer clicks login button")
def step_impl(context):
    context.cadency.Cportal_login.login_button()


@then("Open a new tab")
def step_impl(context):
    context.cadency.Cportal_login.open_newtab()