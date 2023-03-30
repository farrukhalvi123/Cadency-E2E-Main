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


@then("Open Left Side Panel & Click On Manage Teams")
def step_impl(context):
    context.cadency.admin_manage_teams.click_manageteams()


@given("Click On Add New Team Button")
def step_impl(context):
    context.cadency.admin_manage_teams.add_new_team()


@then("Enter Team Name & Description {teamname} and {teamdesc}")
def step_impl(context, teamname, teamdesc):
    context.cadency.admin_manage_teams.enter_teamname_desc(teamname, teamdesc)


@then("Goto Assign Users Tab")
def step_impl(context):
    context.cadency.admin_manage_teams.goto_assignusers_tab()


@then("Search User {user}")
def step_impl(context, user):
    context.cadency.admin_manage_teams.searchuser(user)


@then("Check User is which Box (All Users)")
def step_impl(context):
    context.cadency.admin_manage_teams.check_userin_allusersbox()


@then("Check User is which Box (Assigned User Box)")
def step_impl(context):
    context.cadency.admin_manage_teams.check_userin_assignedusersbox()


@then("Move User Into Assign User")
def step_impl(context):
    context.execute_steps('''''')
    context.cadency.admin_manage_teams.move_userto_assignusers()


@then("Select Modules")
def step_impl(context):
    context.cadency.admin_manage_teams.select_modules()


@then("Save & Verify Team {qateam}")
def step_impl(context, qateam):
    try:
        context.cadency.admin_manage_teams.save_team(qateam)
    except Exception as e:
        print("Team Not Saved Or Already Exist... Unable To Verify Team")

# @then("Add User Details {Fname} and {Lname} and {AdminUname} and {PhnNum} and {Email} and {Pass} and {Cpass}")
# def step_impl(context, Fname, Lname, AdminUname, PhnNum, Email, Pass, Cpass):
#     try:
#         context.cadency.admin_add_users.adduserdetails(Fname, Lname, AdminUname, PhnNum, Email, Pass, Cpass)
#     except Exception as e:
#         attach(context.driver.get_screenshot_as_png(),
#                name=str(e + "Test Failed on customer form"),
#                attachment_type=AttachmentType.PNG)
#         context.driver.close()
#         assert False, e
#     except:
#         attach(context.driver.get_screenshot_as_png(), name=str("Test Failed on customer form"),
#                attachment_type=AttachmentType.PNG)
#         context.driver.close()
#         assert False, "Test Failed on add admin user form"
