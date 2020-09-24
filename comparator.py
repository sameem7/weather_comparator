import sys
sys.path.append('../')

import json
import pytest
import time

from library.api.api_handler import weatherCondition
from library.ui_page_objects.ndtv.ndtv_homepage import ndtvHomepage
from library.ui_page_objects.ndtv.weather_page import weatherPage


class comparator():
    def __init__(self):
        with open('config/config.json') as config_file:
            config = json.loads(config_file.read())
        
        self.BROWSER = config['BROWSER']
        self.VARIANCE_TOLERANCE_LIMIT = config['VARIANCE_TOLERANCE_LIMIT']
        self.TEMPERATURE_UNIT = config['TEMPERATURE_UNIT']
        self.API_KEY = config['API_KEY']
        self.BROWSER_TIMEOUT = config['BROWSER_TIMEOUT']

    def _get_temperature_from_ui(self, city_name):
        page = weatherPage(self.BROWSER)
        page.go_to_ndtv_homepage()
        page.click_three_dots_icon()
        page.navigate_to_weather_page()
        time.sleep(self.BROWSER_TIMEOUT)

        page.enter_text_in_searchbox(city_name)
        time.sleep(self.BROWSER_TIMEOUT)
        if not page.is_city_selected(city_name):
            page.select_city(city_name)
        time.sleep(self.BROWSER_TIMEOUT)
        page.click_city_on_map(city_name)
        time.sleep(self.BROWSER_TIMEOUT)
        conditions = page.get_weather_conditions(city_name)

        return conditions['Temp in Degrees']

    def _get_temperature_from_api(self, city_name, country_code):
        temperature_api = weatherCondition(city_name, country_code, self.API_KEY, self.TEMPERATURE_UNIT).get_temperature_from_api()
        return temperature_api['temp']

    def compare_temperature(self, city_name, country_code):
        temperature_ui = float(self._get_temperature_from_ui(city_name)) 
        temperature_api = float(self._get_temperature_from_api(city_name, country_code))

        print('Temperature from UI: ' +str(temperature_ui))
        print('Temperature from API: '+str(temperature_api))

        if abs(temperature_api - temperature_ui) <= self.VARIANCE_TOLERANCE_LIMIT:
            return True
        else:
            return False


def test_compare_temperature():
    status = comparator().compare_temperature('Bengaluru', 'IN')
    assert status, "Temperature variance is above specified limit!!" 
