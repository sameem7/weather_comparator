from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

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
        try:
            self.driver.find_element_by_id(locator).send_keys(text)
        except ElementNotSelectableException as not_selectable:
            print('Element {0} is not selectable'.format(not_selectable))
        except ElementNotVisibleException as not_visible:
            print('Element {0} is not visible'.format(not_visible))
        except ElementNotInteractableException as not_interactable:
            print('Element {0} is not interactable'.format(not_interactable))    

    def is_selected(self, locator):
        try:
            return self.driver.find_element_by_id(locator).is_selected()
        except ElementNotSelectableException as not_selectable:
            print('Element {0} is not selectable'.format(not_selectable))    

    def click_element(self, locator, by='id'):
        try:
            if by.lower() == 'id':
                self.driver.find_element_by_id(locator).click()
            elif by.lower() == 'xpath':
                self.driver.find_element_by_xpath(locator).click()
        except ElementNotSelectableException as not_selectable:
            print('Element {0} is not selectable'.format(not_selectable))    

    def get_content(self, locator, by='id'):
        if by.lower() == 'id':
            self.driver.find_element_by_id(locator).text
        elif by.lower() == 'xpath':
            self.driver.find_element_by_xpath(locator).text
