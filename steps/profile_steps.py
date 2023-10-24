from pages.profile_page import ProfilePage
from behave import *
from time import sleep

profile_page = ProfilePage()


@when('profile: I remove the book with title {title} from collection')
def step_imp(context, title):
    profile_page.click_delete_by_book_title(title)
    profile_page.click_confirm_delete_button()
    profile_page.refresh_page()


@then('profile: Book with title {title} is present in collection')
def step_imp(context, title):
    profile_page.validate_book_displayed(title)


@then('profile: Book with title {title} is NOT present in collection')
def step_imp(context, title):
    profile_page.validate_book_not_displayed(title)


