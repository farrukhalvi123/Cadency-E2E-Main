import time
from behave import *

use_step_matcher("re")


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
