from pages.left_menu import LeftMenu
from behave import *
from time import sleep

left_menu = LeftMenu()


@when('menu: I click profile_section')
def step_imp(context):
    left_menu.click_profile_section()

