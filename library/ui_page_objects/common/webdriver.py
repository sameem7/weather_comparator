from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class Driver(webdriver.Chrome):
    
    def __init__(self, browser_name):
        if browser_name.lower() == 'chrome':
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser_name.lower() == 'firefox':
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    
    def __del__(self):
        try:
            if self.driver.session_id:
                self.driver.close()
        except Exception as error:
            print('Browser is already closed.')
    
    def enter_text(self, text, locator):
        self.driver.find_element_by_id(locator).send_keys(text)

    def is_selected(self, locator):
        return self.driver.find_element_by_id(locator).is_selected()

    def click_element(self, locator, by='id'):
        if by.lower() == 'id':
            self.driver.find_element_by_id(locator).click()
        elif by.lower() == 'xpath':
            self.driver.find_element_by_xpath(locator).click()

    def get_content(self, locator, by='id'):
        if by.lower() == 'id':
            self.driver.find_element_by_id(locator).text
        elif by.lower() == 'xpath':
            self.driver.find_element_by_xpath(locator).text
        
class Wait(webdriver.support.ui.WebDriverWait):

    def wait_until_element_is_visible(self):
        pass
