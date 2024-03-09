from browser import Browser
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver import Keys, ActionChains


class Product_Search(Browser):

    SEARCH = (By.ID, "_autocompleteSearchMainHeader")
    RESULTS = (By.CLASS_NAME, 'catTitle')
    SEARCH_BTN = (By.ID, '_doSearch')
    CATEGORY_CLICK_INCALTAMINTE = (By.XPATH, '(//a[@title="INCALTAMINTE"])[3]')
    VIEW_MORE = (By.XPATH, '(//div[@class="filter-holder"]/div[13]/span)[2]')
    SIZE = (By.XPATH, '(//input[@id="__label11166"])[2]')
    FILTER_RESULTS = (By.XPATH, '//span[contains(text(),"Afiseaza")]')

# methods for T5 scenario
    def product_search(self):
        try:
            product = self.chrome.find_element(*self.SEARCH)
            product.send_keys('casca hjc')
            logging.info('Successfully typed the product name')
        except Exception as i:
            logging.error(f'An error occurred while trying to type the product name: {str(i)}')

    def click_search_button(self):
        try:
            search_button = self.chrome.find_element(*self.SEARCH_BTN)
            search_button.click()
            logging.info('Successfully clicked the search button')
        except Exception as i:
            logging.error(f'An error occurred while trying to click the search button: {str(i)}')

    def verify_results(self):
        expected_text = 'Toate Produsele'
        results_text = self.chrome.find_element(*self.RESULTS).text
        if results_text == expected_text:
            assert True, "The search was successful, items displayed"
        else:
            assert False, "No results were found"

# methods for T6 scenario
    def product_search2(self):
        self.chrome.get("https://www.bikermag.ro/")
        product2 = self.chrome.find_element(*self.SEARCH)
        product2.send_keys(Keys.CONTROL, 'a')
        product2.send_keys(Keys.BACKSPACE)
        product2.send_keys('ghete alpinestars')

    def category_click(self):
        mouse = ActionChains(self.chrome)
        mouse.move_to_element(self.chrome.find_element(By.XPATH, '(//a[@title="Strada"]/span)[2]')).perform()
        self.chrome.find_element(*self.CATEGORY_CLICK_INCALTAMINTE).click()

    def filter_by_size(self):
        self.chrome.find_element(*self.VIEW_MORE).click()
        self.chrome.find_element(*self.SIZE).click()

    def verify_filter_results(self):
        expected_text = 'Afiseaza:'
        filter_results = self.chrome.find_element(*self.FILTER_RESULTS).text
        if filter_results == expected_text:
            assert True, "The filter was successful, items displayed"
        else:
            assert False, "No results were found"


