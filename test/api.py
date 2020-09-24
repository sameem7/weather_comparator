import sys
sys.path.append('../')

from library.api.api_handler import weatherCondition

weatherCondition().get_temperature_from_api()
