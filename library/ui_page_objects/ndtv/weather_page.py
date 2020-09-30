from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from robot.libraries.BuiltIn import BuiltIn

from library.ui_page_objects.common.webdriver import Driver
from library.ui_page_objects.ndtv.ndtv_homepage import ndtvHomepage


class weatherPage(ndtvHomepage):

    weather_page_url = 'https://social.ndtv.com/static/Weather/report'
    search_box_id = 'searchBox'
    city_map_pin = '//div[contains(@title, "'
    weather_container = '//div[@class="leaflet-popup-content"]' 
    weather_content = '//div[@class="leaflet-popup-content"]//span[@class="heading"]'        

    def get_valid_city_names(self):
        city_elements = self.driver.find_elements_by_xpath("//input[@type='checkbox']")
        valid_city_names = []
        for item in city_elements:
            name = item.get_attribute('id')
            valid_city_names.append(name)
        return valid_city_names

    def enter_text_in_searchbox(self, text):
        self.enter_text(text, self.search_box_id)

    def is_city_selected(self, city_name):        
        valid_city_names = self.get_valid_city_names()
        if city_name.title() not in valid_city_names:
            raise InvalidCitySelected(city_name, valid_city_names)
        else:
            locator = city_name.title()
        return self.is_selected(locator)

    def select_city(self, city_name):
        valid_city_names = self.get_valid_city_names()
        if city_name.title() not in valid_city_names:
            raise InvalidCitySelected(city_name, valid_city_names)
        else:
            locator = city_name.title()
        self.click_element(locator)
    
    def click_city_on_map(self, city_name):
        valid_city_names = self.get_valid_city_names()
        if city_name.title() not in valid_city_names:
            raise InvalidCitySelected(city_name, valid_city_names)
        else:
            locator = self.city_map_pin+str(city_name.title())+'")]'
            self.click_element(locator, 'xpath')
    
    def get_weather_conditions(self, city_name):
        conditions = self.driver.find_elements_by_xpath(self.weather_content)
        weather_condition = {}
        for condition in conditions:
            parameter, separator, value = condition.text.partition(':')
            weather_condition[parameter.strip()] = value
        return weather_condition


class InvalidCitySelected(Exception):
    
    def __init__(self, city_name, valid_cities):
        self.city_name = city_name
        super().__init__('Invalid city selected: ' +str(self.city_name)+'. Please select one from {}'.format(valid_cities) )

