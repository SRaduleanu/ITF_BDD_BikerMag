from browser import Browser
from pages.login_page import Login_Page
from pages.product_search_page import Product_Search
from pages.my_account_page import My_Account_Page
from pages.favorites_and_cart_page import Favorites_And_Cart_Page


def before_all(context):
    context.browser = Browser()
    context.browser.maximize_window()
    context.login_page = Login_Page()
    context.product_search_page = Product_Search()
    context.my_account_page = My_Account_Page()
    context.favorites_and_cart_page = Favorites_And_Cart_Page()

def after_all(context):
    context.browser.close_browser()