from selenium import webdriver
from utilities.customlogger import custom_logger
import logging
from selenium.webdriver.chrome.options import Options

class WebDriverFactory():
    cl = custom_logger(logging.INFO)

    def __init__(self,browser,url):
        self.browser = browser
        self.url = url

    def get_browser_instance(self):
        if self.browser == "FF":
            driver = webdriver.Firefox(executable_path="drivers//geckodriver.exe")

        elif self.browser == "Chrome":
            chrome_options = Options()
            #download_dir = "C://Users//A610037//Downloads//download_chrome"
            chrome_options.add_argument('--start-maximized')
            chrome_options.add_experimental_option('prefs', {'geolocation': True})
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

            driver = webdriver.Chrome(options=chrome_options,executable_path='drivers//chromedriver.exe')


        elif self.browser == "IE":
            driver = webdriver.Ie(executable_path='drivers//IEDriverServer.exe')

        else:
            driver = webdriver.Chrome(executable_path='drivers//chromedriver.exe')


        baseUrl = self.url
        driver.delete_all_cookies()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)
        self.cl.info('Launching the URL :: ' + str(baseUrl) + ' on browser :: ' + str(self.browser))

        return driver



