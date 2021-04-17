from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver
from utilities.customlogger import custom_logger
import logging
from pages.mobile_page.mobile_page import MobilePage
import time


class Account(SeleniumDriver):
    cl = custom_logger(loglevel=logging.INFO)

    def __init__(self,driver):
        super(Account, self).__init__(driver)
        self.driver = driver
        self.mb = MobilePage(self.driver)


    #locators
    _account = {"locatorType":By.XPATH, "locatorValue":"//a/span[text()='Account']"}
    _register = {"locatorType":By.LINK_TEXT, "locatorValue":"Register"}
    _firstname = {"locatorType":By.ID, "locatorValue":"firstname"}
    _lastname = {"locatorType":By.ID, "locatorValue":"lastname"}
    _email_address = {"locatorType":By.ID, "locatorValue":"email_address"}
    _password = {"locatorType":By.ID, "locatorValue":"password"}
    _confirmation = {"locatorType":By.ID, "locatorValue":"confirmation"}
    _checkbox = {"locatorType":By.ID, "locatorValue":"is_subscribed"}
    _register2= {"locatorType":By.XPATH, "locatorValue":"//button[@title='Register']"}
    _success_message = {"locatorType":By.XPATH, "locatorValue":"//span[text()='Thank you for registering with Main Website Store.']"}
    _tv = {"locatorType":By.LINK_TEXT,"locatorValue":"TV"}
    _add_to_wishlist = {"locatorType":By.XPATH, "locatorValue":"//a[@title='LG LCD']//following-sibling::div/child::div/ul/li/a"}
    _share_wishlist = {"locatorType":By.XPATH, "locatorValue":"//span[text()='Share Wishlist']"}
    _emailaddress_wishlist = {"locatorType":By.ID, "locatorValue":"email_address"}
    _message_wishlist = {"locatorType":By.ID, "locatorValue":"message"}
    _message_success_sharelist = {"locatorType":By.XPATH, "locatorValue":"//span[text()='Your Wishlist has been shared.']"}
    _my_Account = {"locatorType":By.XPATH, "locatorValue":"//div[@id='header-account']//a[text()='My Account']"}

    def click_account(self):
        self.elementClick(self._account)

    def click_registration(self):
        self.elementClick(self._register)


    # def click_tv_tab(self):
    #     self.elementClick(self._tv,'link')
    #
    # def add_to_wishlist(self,emailAddress,message):
    #     self.click_tv_tab()
    #     self.elementClick(self._add_to_wishlist,'xpath')
    #     self.elementClick(self._share_wishlist,'xpath')
    #     self.elementSend(self._emailaddress_wishlist,'id',emailAddress)
    #     self.elementSend(self._message_wishlist, 'id', message)
    #     self.elementClick(self._share_wishlist,'xpath')
    #     return self.isElementDisplayed(self._message_success_sharelist,'xpath')



    def register(self,firstName,lastName,emailAddress,password,confirmPassword):
        self.elementSend(self._firstname,firstName)
        self.elementSend(self._lastname,lastName)
        self.elementSend(self._email_address, emailAddress)
        self.elementSend(self._password, password)
        self.elementSend(self._confirmation, confirmPassword)
        self.elementClick(self._checkbox)

    def click_register_button(self):
        self.elementClick(self._register2)


    def success_message(self):
        return self.isElementDisplayed(self._success_message)












