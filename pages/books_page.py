from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.keys import Keys


class BooksPage(BasePage):
    #selectors
    LOGIN_BUTTON = '//button[@id="login"]'
    NUMBER_OF_BOOKS = '//div[@class="action-buttons"]'
    SEARCH_INPUT = '//input[@id="searchBox"]'
    BOOK_TITLE = '//div[@class="action-buttons"]//a'
    ADD_TO_YOUR_COLLECTION_BUTTON = '(//button[@id="addNewRecordButton"])[2]'
    BACK_TO_BOOKSTORE_BUTTON = '(//button[@id="addNewRecordButton"])[2]'

    #actions
    def navigate_to_books_page(self):
        self.driver.get('https://demoqa.com/books/')

    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    def click_add_to_your_collection_button(self):
        self.wait_for_elem(self.ADD_TO_YOUR_COLLECTION_BUTTON)
        self.driver.find_element(By.XPATH, self.ADD_TO_YOUR_COLLECTION_BUTTON).click()


    def click_back_to_bookstore_button(self):
        self.wait_for_elem(self.BACK_TO_BOOKSTORE_BUTTON)
        self.driver.find_element(By.XPATH, self.BACK_TO_BOOKSTORE_BUTTON).click()


    def fill_search_input(self, query):
        self.wait_for_elem(self.SEARCH_INPUT)
        search = self.driver.find_element(By.XPATH, self.SEARCH_INPUT)
        search.clear()
        search.send_keys(query)

    def clear_search_input(self):
        self.wait_for_elem(self.SEARCH_INPUT)
        search = self.driver.find_element(By.XPATH, self.SEARCH_INPUT)
        search.send_keys(Keys.COMMAND, 'a')
        search.send_keys(Keys.BACK_SPACE)

    def click_book_by_title(self, title):
        self.driver.find_element(By.XPATH, '//a[text()="' + title + '"]').click()

    #validations
    def validate_correct_url(self):
        sleep(1)
        expected = 'https://demoqa.com/books'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'Url is incorrect')

    def validate_books_count(self, expected_number):
        sleep(1)
        actual = len(self.driver.find_elements(By.XPATH, self.NUMBER_OF_BOOKS))
        self.assertEqual(expected_number, actual, 'Number of books incorrect')

    def validate_book_name(self, expected_title):
        self.wait_for_elem(self.BOOK_TITLE)
        actual = self.driver.find_element(By.XPATH, self.BOOK_TITLE).text
        self.assertEqual(expected_title, actual, 'Book title is incorrect')


