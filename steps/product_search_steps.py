from behave import *

@given('I am logged in my account')
def step_impl(context):
    context.login_page.open_home_page()
    context.login_page.click_login_button()
    context.login_page.insert_email()
    context.login_page.insert_password()
    context.login_page.click_login_button()

@when('I type the product in the search bar')
def step_impl(context):
    context.product_search_page.product_search()

@when('I click on the search button')
def step_impl(context):
    context.product_search_page.click_search_button()

@then('The search results are displayed containing "{expected_text}')
def step_impl(context):
    context.product_search_page.verify_results()