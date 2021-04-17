from behave import *

from pages.account_creation.account_creation import Account
from pages.login.login import Login
from allure_behave import *

class TestRegistrationFeature():

    @given('I visit the guru99 Ecommerce website in Chrome')
    def class_object(context):
        # context.account = Account(context.driver)
        # """"
        # define all the page class objects here or define them in the environment.py file
        # e.g. context.account = Login(context.driver)
        # """
        pass


    @when('I click on ACCOUNT')
    def step_impl(context):
        context.account.click_account()


    @when('I click on Register')
    def step_impl(context):
        context.account.click_registration()

    @when('I provide the manadatory details {firstname}, {lastname}, {emailaddress}, {password}, {confirmpassword}')
    def step_impl(context,firstname,lastname,emailaddress,password,confirmpassword):
        context.account.register(firstname,lastname,emailaddress,password,confirmpassword)


    @when('I click on Register button')
    def step_impl(context):
        context.account.click_register_button()


    @then('Registration is successfull.')
    def step_impl(context):
        assert context.account.success_message() == True

