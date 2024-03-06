from browser import Browser
from selenium.webdriver.common.by import By
import logging


class Product_Search(Browser):

    SEARCH = (By.XPATH, '//*[@id="_autocompleteSearchMainHeader"]')
    RESULTS = (By.CLASS_NAME, 'catTitle')
    SEARCH_BTN = (By.ID, '_doSearch')

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

    def verify_results(self, expected_text):
        results_text = self.chrome.find_element(*self.RESULTS).text
        if results_text == expected_text:
            assert True, "The search was successful, items displayed"
        else:
            assert False, "No results were found"

