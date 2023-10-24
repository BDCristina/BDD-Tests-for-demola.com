from pages.login_page import LoginPage
from behave import *

#gherkin Syntax - scriem exact pasii pe care ii facem cu POM si BDD
# given - seteaza situatia initiala
# when - actiunile intermediare
# then - verificarea finala

"""
Given I am a user on home page
When I click to bookstore application
When I click login button
When I login with valid credentials
Then I should land on books page
"""

login_page = LoginPage()


@when('login: I login with user {user} and pass {pswd}')
def step_impl(context, user, pswd):
    login_page.fill_user_input(user)
    login_page.fill_pass_input(pswd)
    login_page.click_login_button()


@then('login: I validate that error message is displayed')
def step_impl(context):
    login_page.validate_invalid_credentials_error()