from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from library.ui_page_objects.common.webdriver import Driver
from library.ui_page_objects.ndtv.ndtv_homepage import ndtvHomepage

class weatherPage(ndtvHomepage):
    weather_page_url = 'https://social.ndtv.com/static/Weather/report'
    search_box_id = 'searchBox'
    bengaluru_checkbox = 'Bengaluru'
    bellary_checkbox = 'Bellary'
    chennai_checkbox = 'Chennai'
    bengaluru_map_pin = '//div[contains(@title, "Bengaluru")]'
    bellary_map_pin = '//div[contains(@title, "Bellary")]'
    chennai_map_pin = '//div[contains(@title, "Chennai")]'
    weather_container = '//div[@class="leaflet-popup-content"]' 
    weather_content = '//div[@class="leaflet-popup-content"]//span[@class="heading"]'

    def enter_text_in_searchbox(self, text):
        self.enter_text(text, self.search_box_id)

    def is_city_selected(self, city_name):
        if city_name.lower() == 'bengaluru':
            locator = self.bengaluru_checkbox
        elif city_name.lower() == 'bellary':
            locator = self.bellary_checkbox
        elif city_name.lower() == 'chennai':
            locator = self.chennai_checkbox
        else:
            raise InvalidCitySelected(city_name)
        return self.is_selected(locator)

    def select_city(self, city_name):
        if city_name.lower() == 'bengaluru':
            locator = self.bengaluru_checkbox
        elif city_name.lower() == 'bellary':
            locator = self.bellary_checkbox
        elif city_name.lower() == 'chennai':
            locator = self.chennai_checkbox
        else:
            raise InvalidCitySelected(city_name)
        self.click_element(locator)
    
    def click_city_on_map(self, city_name):
        if city_name.lower() == 'bengaluru':
            self.click_element(self.bengaluru_map_pin, 'xpath')
        elif city_name.lower() == 'bellary':
            self.click_element(self.bellary_map_pin, 'xpath')
        elif city_name.lower() == 'chennai':
            self.click_element(self.chennai_map_pin, 'xpath')
        else:
            raise InvalidCitySelected(city_name)
    
    def get_weather_conditions(self, city_name):
        conditions = self.driver.find_elements_by_xpath(self.weather_content)
        weather_condition = {}
        for condition in conditions:
            parameter, separator, value = condition.text.partition(':')
            weather_condition[parameter.strip()] = value
        return weather_condition


class InvalidCitySelected(Exception):
    
    def __init__(self, city_name):
        self.city_name = city_name
        super().__init__('Invalid city selected: ' +str(self.city_name)+'. Please select one from Bengaluru, Bellary, or Chennai')