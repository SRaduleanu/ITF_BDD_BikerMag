import logging
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from browser import Browser
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Favorites_And_Cart_Page(Browser):

    CATEGORY_CLICK_COPII = (By.XPATH, '(//a[@title="COPII"])[2]')
    ASCENDING = (By.CSS_SELECTOR, '#category-page > div > div:nth-child(3) > div.result-section.clearfix > label > select > option:nth-child(5)')
    CHEAPEST_PRODUCT = (By.XPATH, '//a[@class="title _productUrl_56174"]')
    ADD_FAVORITE = (By.CSS_SELECTOR, 'a[title="Favorite"]')
    SEARCH = (By.ID, "_autocompleteSearchMainHeader")
    PRODUCT_TO_ADD_TO_CART = (By.XPATH, '//a[@class="title _productUrl_41125"]')
    ADD_TO_CART_BTN = (By.XPATH, '//a[normalize-space()="Adauga in cos"]')
    CART_ITEM = (By.XPATH, '//a[contains(text(),"Armura moto pentru copii Thor")]')

# methods for T9 scenario
    def category_click(self):
        mouse = ActionChains(self.chrome)
        mouse.move_to_element(self.chrome.find_element(By.XPATH, '(//a[@title="Casti"]/span)[2]')).perform()
        self.chrome.find_element(*self.CATEGORY_CLICK_COPII).click()

    def ascending_sort(self):
        self.chrome.find_element(By.CLASS_NAME, 'input-s').click()
        self.chrome.find_element(*self.ASCENDING).click()

    def click_cheapest_product(self):
        WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(*self.CHEAPEST_PRODUCT))
        self.chrome.find_element(*self.CHEAPEST_PRODUCT).click()

    def add_to_favorites(self):
        WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(*self.ADD_FAVORITE))
        self.chrome.find_element(*self.ADD_FAVORITE).click()

    def verify_favorites(self):
        WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="wishlist-pp visible"]')))
        favorite_added = (self.chrome.find_element(By.CSS_SELECTOR, 'i[class*=icon-selected]'))
        if favorite_added.is_displayed():
            logging.info('The product was successfully added to favorites')
        else:
            logging.info('The product was not successfully added to favorites')

# methods for T10 scenario
    def product_search(self):
        try:
            product = self.chrome.find_element(*self.SEARCH)
            product.send_keys('Armura moto pentru copii')
            product.send_keys(Keys.ENTER)
            logging.info('Successfully typed the product name')
        except Exception as i:
            logging.error(f'An error occurred while trying to type the product name: {str(i)}')

    def access_product_page(self):
        WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(*self.PRODUCT_TO_ADD_TO_CART))
        click_product = self.chrome.find_element(*self.PRODUCT_TO_ADD_TO_CART)
        click_product.click()

    def add_to_cart(self):
        WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(*self.ADD_TO_CART_BTN))
        add_cart = self.chrome.find_element(*self.ADD_TO_CART_BTN)
        add_cart.click()
        sleep(2)

    def verify_cart(self):
        self.chrome.get('https://www.bikermag.ro/cos-de-cumparaturi')
        WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(*self.CART_ITEM))
        cart_item = self.chrome.find_element(*self.CART_ITEM)
        if cart_item:
            logging.info('Item was successsfully added to the cart!')
        else:
            logging.info('Item was not added to the cart!')





