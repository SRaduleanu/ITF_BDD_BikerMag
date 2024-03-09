from behave import *

# steps for T7 scenario
@given('I am logged into My account')
def step_impl(context):
    context.my_account_page.open_account_page()

@when('I click on Adrese')
def step_impl(context):
    context.my_account_page.click_adrese()

@when('I click on Adauga adresa noua')
def step_impl(context):
    context.my_account_page.click_adauga_adresa_noua()

@when('I fill in the address necessary fields')
def step_impl(context):
    context.my_account_page.fill_in_fields()

@when('I click on Salveaza')
def step_impl(context):
    context.my_account_page.click_salveaza()

@then('I verify that the address was saved successfully')
def step_impl(context):
    context.my_account_page.verify_address_added()

# steps for T8 scenario
@given('I am logged into the account')
def step_impl(context):
    context.my_account_page.open_account_page()

@when('I click on Adrese menu')
def step_impl(context):
    context.my_account_page.click_adrese()

@when('I click on Stergere')
def step_impl(context):
    context.my_account_page.delete_address()

@then('I verify that the address was deleted successfully')
def step_impl(context):
    context.my_account_page.verify_delete()