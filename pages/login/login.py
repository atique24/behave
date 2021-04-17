from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class Login(SeleniumDriver):
    def __init__(self,driver):
        super(Login, self).__init__(driver)
        self.driver = driver


    #locators
    _account = {"locatorType":By.XPATH, "locatorValue":"//a/span[text()='Account']"}
    _my_Account = {"locatorType":By.XPATH, "locatorValue":"//div[@id='header-account']//a[text()='My Account']"}
    _login_link = {"locatorType":By.LINK_TEXT,"locatorValue":"Log In"}
    _username = {"locatorType":By.XPATH,"locatorValue":"//input[@title='Email Address']"}
    _password = {"locatorType":By.ID,"locatorValue":"pass"}
    _login = {"locatorType":By.ID,"locatorValue":"send2"}
    _dashboard = {"locatorType":By.XPATH,"locatorValue":"//h1[text()='My Dashboard']"}


    def click_account(self):
        self.elementClick(self._account)

    def click_login_link(self):
        self.elementClick(self._login_link)

    def enter_credentials(self,username,password):
        self.elementSend(self._username,username)
        self.elementSend(self._password, password)

    def click_login_button(self):
        self.elementClick(self._login)

    def my_account_dislayed(self):
        return self.isElementDisplayed(self._dashboard)

