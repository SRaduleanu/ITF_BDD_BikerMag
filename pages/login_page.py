from browser import Browser
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class Login_Page(Browser):

    LOGIN_BTN = (By.XPATH, "//li[@class='-g-user-icon']")
    EMAIL = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SIGN_IN = (By.ID, "doLogin")
    ERROR = (By.CLASS_NAME, "errorMsg")
    ACCOUNT = (By.XPATH, "(//span[contains(text(), 'Serban')])[2]")
    LOGOUT = (By.XPATH, '//*[@id="wrapper"]/div[3]/div/div[1]/div[2]/ul[5]/li/a')
    ACCEPT_COOKIES_BTN = (By.ID, '__gomagCookiePolicy')

# methods for T1 scenario
    def open_home_page(self):
        self.chrome.get("https://www.bikermag.ro/")

    def click_login_button(self):
        WebDriverWait(self.chrome, 5).until(EC.visibility_of_element_located(self.LOGIN_BTN))
        max_try = 3
        attempts = 0
        while attempts < max_try:
            try:
                login_button = self.chrome.find_element(*self.LOGIN_BTN)
                if login_button:
                    login_button.click()
                    sleep(1)
                    break
                else:
                    raise AssertionError("Login button element not found")
            except Exception as i:
                logging.error(f'An error occurred while clicking the "Intra in cont" button: {str(i)}')
                attempts += 1

    def insert_email(self):
        try:
            user_email = self.chrome.find_element(*self.EMAIL)
            user_email.send_keys('tester.sraduleanu@yahoo.com')
            sleep(1)
        except Exception as i:
            logging.error(f'An error occurred while inserting the email: {str(i)}')

    def insert_invalid_password(self, password):
        try:
            user_password = self.chrome.find_element(*self.PASSWORD)
            user_password.send_keys(password)
            sleep(1)
        except Exception as i:
            logging.error(f'An error occurred while inserting the password: {str(i)}')

    def click_sign_in_button(self):
        try:
            sign_in_button = self.chrome.find_element(*self.SIGN_IN)
            sign_in_button.click()
            sleep(2)
        except Exception as i:
            logging.error(f'An error occurred while clicking the "Intra in cont" authentication button: {str(i)}')

    def login_failed(self, error_message):
        try:
            login_error = self.chrome.find_element(*self.ERROR)
            login_error_text = login_error.text
            assert error_message in login_error_text
            logging.info("Login failed {}".format(error_message))
        except Exception as i:
            logging.error(f'The error message does not match: {str(i)}')

# methods for T2 scenario
    def insert_password(self):
        try:
            userpassword = self.chrome.find_element(*self.PASSWORD)
            userpassword.send_keys('Tester123')
            sleep(1)
        except Exception as i:
            logging.error(f"An error occurred while inserting the password: {str(i)}")

    def my_account_page(self):
        account_url = "https://www.bikermag.ro/contul-meu"
        assert self.chrome.current_url == account_url
        logging.info('Test passed: Current URL match the expected account URL')
        sleep(1)

    def verify_login(self):
        account = self.chrome.find_element(*self.ACCOUNT)
        account_text = 'Buna, Serban'
        assert account.text == account_text
        logging.info('I am logged in.')
        sleep(1)

# methods for T3 scenario
    def click_my_account(self):
        self.chrome.find_element(*self.ACCOUNT).click()
        sleep(1)

    def click_logout(self):
        try:
            logout_account = self.chrome.find_element(*self.LOGOUT)
            logout_account.click()
            sleep(1)
        except Exception as i:
            logging.error(f'An error occurred while trying to logout: {str(i)}')

    def verify_logout(self):
        logout_text = 'Intra in cont'
        logout_text_btn = self.chrome.find_element(By.XPATH, '//*[@id="wrapper"]/header/div[2]/div/div/div[3]/ul/li[2]/a/span').text
        print(logout_text_btn)
        assert logout_text_btn in logout_text
        logging.info("I am no longer logged in.")
        sleep(1)

# methods for T4 scenario

    def accept_cookies(self):
        cookies_btn = self.chrome.find_element(*self.ACCEPT_COOKIES_BTN)
        cookies_btn.click()