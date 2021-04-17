from behave import *

from pages.login.login import Login
from utilities.customlogger import custom_logger
import logging
from base.WebDriverFactory import WebDriverFactory
from base.selenium_driver import SeleniumDriver
import configuration_file.configuration as config
from pages.account_creation.account_creation import Account
import allure_behave.hooks


cl = custom_logger(logging.INFO)



def before_scenario(context,feature):
    cl.info("Automation Started")
    context.wdf = WebDriverFactory(browser=config.browser,url=config.url)
    context.driver = context.wdf.get_browser_instance()

    # All Page Objects initialized here
    context.selenium_driver = SeleniumDriver(context.driver)
    context.login = Login(context.driver)
    context.account = Account(context.driver)





def after_scenario(context,feature):
    context.driver.quit()
    cl.info("Automation Ended")



