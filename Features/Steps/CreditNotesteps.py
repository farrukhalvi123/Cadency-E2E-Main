from behave import *




@then("click on Open")
def  openfilter(context):
    context.cadency.creditnote.Opentab()


# @then("click on three dots and click to apply credit notes")
# def threedots(context):
#     context.cadency.creditnote.selectCn()



@then("enter values")
def tofillform(context):
    context.cadency.creditnote.fillvalue()


# @then("get first CN no from text")
# def getCNtext(context):
#     context.cadency.creditnote.CNtext()


@then("check if there are any open invoices")
def step_impl(context):
   context.cadency.creditnote.checkopeninv()