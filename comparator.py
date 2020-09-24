import sys
sys.path.append('../')

from library.api.api_handler import weatherCondition
from ui_page_objects.ndtv.ndtv_homepage import ndtvHomepage
from ui_page_objects.ndtv.weather_page import weatherPage
import time


def _get_temperature_from_ui():
    page = weatherPage('Chrome')
    page.go_to_ndtv_homepage()
    page.click_three_dots_icon()
    page.navigate_to_weather_page()
    time.sleep(3)
    
    page.enter_text_in_searchbox('Bengaluru')
    time.sleep(3)
    if not page.is_city_selected('Bengaluru'):
        page.select_city('Bengaluru')
    time.sleep(3)
    page.click_city_on_map('Bengaluru')
    time.sleep(3)
    conditions = page.get_weather_conditions('Bengaluru')
    
    return conditions['Temp in Degrees']
    
def _get_temperature_from_api():
    temperature_dict = weatherCondition().get_temperature_from_api()
    return temperature_dict['temp']

def comparator():
    temperature_ui = int(_get_temperature_from_ui())
    temperature_api = _get_temperature_from_api()
    print('Temperature from UI: ' +str(temperature_ui))
    print('Temperature from API: '+str(temperature_api))

    if abs(temperature_api - temperature_ui) > 2:
        print('Comparison failed!!! Variance is not within specified limits.')
    else:
        print('Variance is within specified limits.')

comparator()