from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    #selectors
    USER_INPUT = '//input[@id="userName"]'
    PASS_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//button[@id="login"]'
    INVALID_CREDENTIALS_ERROR = '//p[@id="name"]'
    #INVALID_CREDENTIALS_ERROR = '//*[@id="name"]'
    #actions
    def fill_user_input(self, user):
        self.wait_for_elem(self.USER_INPUT)
        self.driver.find_element(By.XPATH, self.USER_INPUT).send_keys(user)

    def fill_pass_input(self, pswd):
        self.wait_for_elem(self.PASS_INPUT)
        self.driver.find_element(By.XPATH, self.PASS_INPUT).send_keys(pswd)

    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    # validations
    def validate_invalid_credentials_error(self):
        self.wait_for_elem(self.INVALID_CREDENTIALS_ERROR)
        expected = 'Invalid username or password!'
        actual = self.driver.find_element(By.XPATH, self.INVALID_CREDENTIALS_ERROR).text
        self.assertEqual(expected, actual, 'Error message is incorrect')

