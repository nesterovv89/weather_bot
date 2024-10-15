import requests
import geocoder

import constants as c

url = c.URL


async def get_weather(city):
    """Запрос погоды от АПИ по кастомному городу"""
    response = requests.get(f'{url}{city}?format=4')
    if response.status_code == 200:
        return response.text
    elif response.status_code == 404:
        return c.ERR_404
    else:
        return c.ERR


async def get_weather_current_location():
    """Запрос погоды от АПИ по текущему месту"""
    geo = geocoder.ip('me')
    city = geo.city
    print (city)
    response = requests.get(f'{url}{city}?format=4')
    if response.status_code == 200:
        return response.text
    elif response.status_code == 404:
        return c.ERR_404
    else:
        return c.ERR
