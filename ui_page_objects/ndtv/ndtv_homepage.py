from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui_page_objects.common.webdriver import Driver


class ndtvHomepage(Driver):
    ndtv_homepage_url = 'https://www.ndtv.com/'
    three_dots_icon = '//*[@id="h_sub_menu"]'
    weather_link = '//*[contains(text(), "WEATHER")]'

    def go_to_ndtv_homepage(self):     
        self.driver.get(self.ndtv_homepage_url)
        self.driver.maximize_window()
        
        return self.driver.title
        
    def click_three_dots_icon(self):
        icon = self.driver.find_element_by_xpath(self.three_dots_icon)
        icon.click()

    def navigate_to_weather_page(self):
        link = self.driver.find_element_by_xpath(self.weather_link)
        link.click()

