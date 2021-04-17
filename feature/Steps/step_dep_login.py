from behave import *
from pages.login.login import Login
from pages.account_creation.account_creation import Account



class LoginTest():


    #@given('I visit the guru99 Ecommerce website in Chrome')
    # def classObject(context):
    #     context.login = Login(context.driver)

    @when("I click on Login link")
    def click_login_link(context):
        context.login.click_login_link()


    @when("I enter {username} and {password}")
    def enter_username_password(context,username,password):
        context.login.enter_credentials(username,password)

    @when("I click on Login Button")
    def step_click_login(context):
        context.login.click_login_button()

    @then('My Homepage should be displayed.')
    def login_success(context):
        assert context.login.my_account_dislayed() == True

