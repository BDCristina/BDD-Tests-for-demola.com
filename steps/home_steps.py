from pages.home_page import Homepage
from behave import *

#gherkin Syntax - scriem exact pasii pe care ii facem cu POM si BDD
# given - seteaza situatia initiala
# when  - actiunile intermediare
# then - verificarea finala

"""
Given I am a user on home page
When I click to bookstore application card
When I click login button
When I login with valid credentials
Then I should land on books page
"""

home_page = Homepage()


@given('home: I am a user on home page')
def step_impl(context):
    home_page.driver.delete_all_cookies()
    home_page.navigate_to_home_page()


@when('home: I click to bookstore application card')
def step_impl(context):
    home_page.click_book_store_application_card()
