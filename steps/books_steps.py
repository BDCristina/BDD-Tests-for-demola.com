from pages.books_page import BooksPage
from behave import *
from time import sleep

#gherkin Syntax - scriem exact pasii pe care ii facem cu POM si BDD
# given - seteaza situatia initiala
# when  - actiunile intermediare
# then - verificarea finala

"""
Given I am a user on home page
When I click to bookstore application
When I click login button
When I login with valid credentials
Then I should land on books page
"""

books_page = BooksPage()


@when('books: I click login button')
def step_impl(context):
    books_page.click_login_button()


@when('books: I search after {query}')
def step_impl(context, query):
    books_page.fill_search_input(query)

@when('books: I add to collection the book title {title}')
def step_impl(context, title):
    books_page.click_book_by_title(title)
    books_page.click_add_to_your_collection_button()
    books_page.browser_back()
    sleep(1)


@when('books: I clear search input')
def step_impl(context):
    books_page.clear_search_input()
    sleep(3)


@then('books: I should land on books page')
def step_impl(context):
    books_page.validate_correct_url()


@then('books: I validate that 8 books are displayed')
def step_imp(context):
    books_page.validate_books_count(8)


@then('books: I validate that only {title} book is displayed')
def step_imp(context, title):
    books_page.validate_books_count(1)
    books_page.validate_book_name(title)

