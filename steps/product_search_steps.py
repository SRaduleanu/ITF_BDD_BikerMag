from behave import *

# steps for T5 scenario
@given('I am logged in my account')
def step_impl(context):
    context.login_page.open_home_page()
    context.login_page.click_login_button()
    context.login_page.insert_email()
    context.login_page.insert_password()
    context.login_page.click_sign_in_button()

@when('I type the product in the search bar')
def step_impl(context):
    context.product_search_page.product_search()

@when('I click on the search button')
def step_impl(context):
    context.product_search_page.click_search_button()

@then('The search results are displayed containing "Toate produsele"')
def step_impl(context):
    context.product_search_page.verify_results()

# steps for T6 scenario
@given('I am logged in my BikerMag account')
def step_impl(context):
    context.login_page.open_home_page()
    context.login_page.click_login_button()
    context.login_page.insert_email()
    context.login_page.insert_password()
    context.login_page.click_sign_in_button()

@when('I search for a product')
def step_impl(context):
    context.product_search_page.product_search2()

@when('I click on a category')
def step_impl(context):
    context.product_search_page.category_click()

@when('I click on the desired size')
def step_impl(context):
    context.product_search_page.filter_by_size()

@then('The filter results are displayed')
def step_impl(context):
    context.product_search_page.verify_filter_results()