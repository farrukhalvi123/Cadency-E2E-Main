from behave import *




@then("click on Open")
def  openfilter(context):
    context.cadency.creditnote.Opentab()


@then("click on three dots and click to apply credit notes")
def threedots(context):
    context.cadency.creditnote.selectCn()
