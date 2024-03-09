from behave import *

# steps for T9 scenario
@given('I am logged into my account!')
def step_impl(context):
    context.my_account_page.open_account_page()

@when('I search for the cheapest product')
def step_impl(context):
    context.favorites_and_cart_page.category_click()
    context.favorites_and_cart_page.ascending_sort()
    context.favorites_and_cart_page.click_cheapest_product()

@when('I add it to favorites')
def step_impl(context):
    context.favorites_and_cart_page.add_to_favorites()

@then('Check for confirmation message')
def step_impl(context):
    context.favorites_and_cart_page.verify_favorites()

# steps for T10 scenario
@given('I am logged in my account!')
def step_impl(context):
    context.my_account_page.open_account_page()

@when('I search for a new product')
def step_impl(context):
    context.favorites_and_cart_page.product_search()

@when('I click on the product')
def step_impl(context):
    context.favorites_and_cart_page.access_product_page()

@when('I add the product to the cart')
def step_impl(context):
    context.favorites_and_cart_page.add_to_cart()

@then('I check the cart')
def step_impl(context):
    context.favorites_and_cart_page.verify_cart()