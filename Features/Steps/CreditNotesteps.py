from behave import *
import time



@then("click on Open")
def openfilter(context):
    context.cadency.creditnote.Opentab()


@then("click on three dots and click to apply credit notes")
def threedots(context):
    context.cadency.creditnote.selectCn()


@then("enter values")
def tofillform(context):
    context.cadency.creditnote.fillvalue()


# @then("get first CN no from text")
# def getCNtext(context):
#     context.cadency.creditnote.CNtext()
@then("take to CN page")
def Cnpage(context):
    context.cadency.creditnote.CNmodule()
    time.sleep(5)


@then("take first CN number")
def firstCN(context):
    context.cadency.creditnote.firstcnnumber()

