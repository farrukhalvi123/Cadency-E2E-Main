from behave import *




@given("click on sprocket")
def step_impl(context):
 context.cadency.advpayset.star()


@given("click on dropdown")
def step_impl(context):
 context.cadency.advpayset.dropUK()