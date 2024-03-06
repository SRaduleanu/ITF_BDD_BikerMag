from behave import *

@given('I am on the BikerMag homepage and I want to initiate the login process with invalid password')
def step_impl(context):
    context.login_page.open_home_page()

@when('I click on "Intra in cont" button')
def step_impl(context):
    context.login_page.click_login_button()

@when('I enter my valid email')
def step_impl(context):
    context.login_page.insert_email()

@when('I enter my invalid password "{user_password}"')
def step_impl(context, user_password):
    context.login_page.insert_invalid_password(user_password)

@when('I click on "Intra in cont" authentication button')
def step_impl(context):
    context.login_page.click_sign_in_button()

@then('I receive an "{login_error}"')
def step_impl(context, login_error):
    context.login_page.login_failed(login_error)

@when('I enter my valid password')
def step_impl(context):
    context.login_page.insert_password()

@when('I click on "Intra in cont" authentication')
def step_impl(context):
    context.login_page.click_sign_in_button()

@then('I am redirected to my account page')
def step_impl(context):
    context.login_page.my_account_page()

@when('I check to see if I am logged in')
def step_impl(context):
    context.login_page.verify_login()

@when('I click on my account')
def step_impl(context):
    context.login_page.click_my_account()

@when('I click on logout')
def step_impl(context):
    context.login_page.click_logout()

@then('I check to see if I am no longer logged in')
def step_impl(context):
    context.login_page.verify_logout()