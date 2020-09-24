import sys
sys.path.append('../')

from ui_page_objects.ndtv.ndtv_homepage import ndtvHomepage
from ui_page_objects.ndtv.weather_page import weatherPage
import time

page = weatherPage('Chrome')
page.go_to_ndtv_homepage()
page.click_three_dots_icon()
page.navigate_to_weather_page()
time.sleep(3)
page.enter_text_in_searchbox('Bengaluru')
time.sleep(3)
if not page.is_city_selected('Bengaluru'):
    page.select_city('Bengaluru')
else:
    print('Bengaluru is already selected')
time.sleep(3)
page.click_city_on_map('Bengaluru')
time.sleep(3)
conditions = page.get_weather_conditions('Bengaluru')
for key in conditions:
    print(key+':'+conditions[key])
time.sleep(3)
