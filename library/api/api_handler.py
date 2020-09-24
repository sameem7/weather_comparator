import requests

class apiHandler():
    def __init__(self):
        self.response_body = ""

    def send_request(self, method, url, endpoint, data = None, headers=None, params=None):
        response_body = None
        status_code = None

        if method.lower() == 'get':
            response_body,  status_code = self.get_request(url, endpoint, params=params)
            return response_body, status_code 
        elif method.lower() == 'post':
            response_body, status_code = self.post_request(url, endpoint, data, params=params)
            return response_body, status_code 
        
    def get_request(self, url, endpoint, headers=None, params=None):
        response = requests.get(url+endpoint, headers=headers, params=params)
        return response.json(), response.status_code

    def post_request(self, url, endpoint, data, headers=None, params=None):
        response = requests.post( url + endpoint, headers=headers, data=data, params=params)
        return response.json(), response.status_code

class weatherCondition(apiHandler):
    def __init__(self, city, country_code, api_key, unit):
        self.city_name = city
        self.country_code = country_code
        self.api_key = api_key
        self.unit = unit

    def get_temperature_from_api(self):
        url = 'https://api.openweathermap.org'
        endpoint = '/data/2.5/weather'
        city = self.city_name + ',' + self.country_code
        params = {'q':city, 'appid':self.api_key, 'units':self.unit}
        
        response_body, status_code = self.send_request('get', url, endpoint, params=params)
        return response_body['main']
        