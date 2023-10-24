from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.keys import Keys


class LeftMenu(BasePage):
    #selectors
    LOGIN_BUTTON = '//span[text()="Profile"]'

    #actions
    def click_profile_section(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        element = self.driver.find_element(By.XPATH, self.LOGIN_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

