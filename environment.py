from browser import Browser
from pages.login_page import Login_Page
from pages.product_search_page import Product_Search


def before_all(context):
    context.browser = Browser()
    context.browser.maximize_window()
    context.login_page = Login_Page()
    context.product_search_page = Product_Search()

def after_all(context):
    context.browser.close_browser()