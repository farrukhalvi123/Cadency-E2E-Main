from behave import *
import time




@then("click on Open")
def openfilter(context):
    context.cadency.creditnote.Opentab()


@then("click on three dots and click to apply credit notes")
def threedots(context):
    context.cadency.creditnote.selectCn()


@then("enter values and save")
def tofillform(context):
    context.cadency.creditnote.fillvalue()


# @then("get first CN no from text")
# def getCNtext(context):
#     context.cadency.creditnote.CNtext()
@then("take to CN page")
def Cnpage(context):
    time.sleep(3)
    context.cadency.creditnote.CNmodule()
    time.sleep(3)



@then("get first CN no from text")
def step_impl(context):
    context.cadency.creditnote.takecn()