import logging

from browser import Browser
from time import sleep
from selenium.webdriver.common.by import By

class My_Account_Page(Browser):

    ADRESE_BTN = (By.XPATH, '//div[@class="row"]/ul[3]/li[2]/a')
    ADRESA_NOUA_BTN = (By.XPATH, '//a[contains(text(),"Adauga")]')
    ADD_JUDET = (By.ID, '_shippingRegion')
    ADD_CITY = (By.ID, '_shippingCity')
    ADD_ADDRESS = (By.CSS_SELECTOR, '#addAddress > div:nth-child(9) > input')
    ADD_POSTAL_CODE = (By.CSS_SELECTOR, '#addAddress > div:nth-child(10) > input')
    ADD_PHONE = (By.CSS_SELECTOR, '#addAddress > div:nth-child(11) > input')
    SAVE_BTN = (By.ID, 'doSave')
    MESSAGE = (By.CLASS_NAME, 'succes-message')
    DELETE_ADDRESS = (By.XPATH, '(//div[@class="row"]/div/div/a[2])[1]')

# methods for T7 scenario
    def open_account_page(self):
        self.chrome.get('https://www.bikermag.ro/contul-meu')

    def click_adrese(self):
        self.chrome.find_element(*self.ADRESE_BTN).click()


    def click_adauga_adresa_noua(self):
        self.chrome.find_element(*self.ADRESA_NOUA_BTN).click()
        sleep(1)

    def fill_in_fields(self):
        self.chrome.find_element(*self.ADD_JUDET).click()
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, '#_shippingRegion > option[value="267"]').click()
        sleep(1)
        self.chrome.find_element(*self.ADD_CITY).click()
        sleep(1)
        self.chrome.find_element(By.CSS_SELECTOR, '#_shippingCity > option[value="4758"]').click()
        sleep(1)
        self.chrome.find_element(*self.ADD_ADDRESS).send_keys('str. B.ST.Delavrancea, nr.1')
        self.chrome.find_element(*self.ADD_POSTAL_CODE).send_keys('106400')
        self.chrome.find_element(*self.ADD_PHONE).send_keys('0761585630')

    def click_salveaza(self):
        self.chrome.find_element(*self.SAVE_BTN).click()

    def verify_address_added(self):
        try:
            expected_text = 'Adresa de livrare a fost salvata cu succes.'
            actual_text = self.chrome.find_element(*self.MESSAGE).text
            assert expected_text == actual_text
            logging.info('The address was successfully saved!')
        except Exception as i:
            logging.error(f'An error occurred while trying to save the address: {str(i)}')

# methods for T8 scenario
    def delete_address(self):
        self.chrome.find_element(*self.DELETE_ADDRESS).click()

    def verify_delete(self):
        try:
            expected_text = 'Adresa a fost stearsa cu succes'
            actual_text = self.chrome.find_element(*self.MESSAGE).text
            assert expected_text == actual_text
            logging.info('The address was successfully deleted!')

        except Exception as i:
            logging.error(f'An error occurred while trying to save the address: {str(i)}')