from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from ui_page_objects.common.webdriver import Driver
from ui_page_objects.ndtv.ndtv_homepage import ndtvHomepage

class weatherPage(ndtvHomepage):
    weather_page_url = 'https://social.ndtv.com/static/Weather/report'
    search_box_id = 'searchBox'
    bengaluru_checkbox = 'Bengaluru'
    bengaluru_map_pin = '//div[contains(@title, "Bengaluru")]'
    weather_container = '//div[@class="leaflet-popup-content"]' 
    weather_content = '//div[@class="leaflet-popup-content"]//span[@class="heading"]'

    def enter_text_in_searchbox(self, text):
        self.enter_text(text, self.search_box_id)

    def is_city_selected(self, city_name):
        if city_name.lower() == 'bengaluru':
            locator = self.bengaluru_checkbox
        return self.is_selected(locator)

    def select_city(self, city_name):
        if city_name.lower() == 'bengaluru':
            locator = self.bengaluru_checkbox
        self.click_element(locator)
    
    def click_city_on_map(self, city_name):
        if city_name.lower() == 'bengaluru':
            self.click_element(self.bengaluru_map_pin, 'xpath')
    
    def get_weather_conditions(self, city_name):
        conditions = self.driver.find_elements_by_xpath(self.weather_content)
        weather_condition = {}
        for condition in conditions:
            parameter, separator, value = condition.text.partition(':')
            weather_condition[parameter.strip()] = value
        return weather_condition
            