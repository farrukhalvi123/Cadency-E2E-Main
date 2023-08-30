import time
from behave import *


# @then("click on Open")
# def openingfilter(context):
#     context.cadency.PromisetoPay.Opentab()
#     time.sleep(3)

@then("take first invoice")
def firstinvoice(context):
    context.cadency.PromisetoPay.medo()
    time.sleep(3)


@then("click on promise to pay button")
def promisetop(context):
    context.cadency.PromisetoPay.pptop()
    time.sleep(3)


# @then("verify Ptop")
# def tag(context):
#    context.cadency.PromisetoPay.tagcheck()
@then("identifying all ptop invoice with invoice no")
def invnptop(context):
    context.cadency.PromisetoPay.identifyingallptops()



@then("go to new tab")
def step_impl(context):
    context.cadency.PromisetoPay.goingtonewtab()



@then("going to invoice section from Cportal and towards open tab")
def step_impl(context):
    context.cadency.PromisetoPay.towardsinvoice_opentab()


@then("select country from dropdown")
def step_impl(context):
    context.cadency.PromisetoPay.Checkout()


@then("Payment method via paysafe")
def step_impl(context):
    context.cadency.PromisetoPay.select_payfe()


@then("make a Payment {CardholderName} and {CardNumber} and {Expirydate} and {CVV}")
def step_impl(context, CardholderName,CardNumber,Expirydate,CVV):
    context.cadency.PromisetoPay.Cardholder_Name(CardholderName)
    context.cadency.PromisetoPay.Card_Number(CardNumber)
    context.cadency.PromisetoPay.Expiry_date(Expirydate)
    context.cadency.PromisetoPay.CVV_no(CVV)