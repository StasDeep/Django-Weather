# -*- coding: utf-8 -*-
import json
import urllib2

WEATHER_API_KEY = '7ec667bf669cce3a71b5381e2fcdbf75'


def weather_by_city_id(city_id):
    """Take weather from Weather API and return it.
    
    Args:
        city_id (str): unique number, representing city.
        
    Returns:
        dict: object with information about weather.
              Has keys:
              - city_name (str),
              - country_code (str),
              - weather (str),
              - weather_description (str),
              - temperature (float),
              - humidity (float),
              - pressure (float),
              - wind_speed (float),
              - icon_url (str)
            
    """
    url_template = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid={}'
    url = url_template.format(city_id, WEATHER_API_KEY)
    response = urllib2.urlopen(url).read()
    data = json.loads(response)

    city_weather = dict()
    city_weather['city_name'] = data['name']
    city_weather['country_code'] = data['sys']['country']
    city_weather['weather'] = data['weather'][0]['main']
    city_weather['weather_description'] = data['weather'][0]['description']
    city_weather['temperature'] = data['main']['temp'] - 273.15
    city_weather['humidity'] = float(data['main']['humidity'])
    city_weather['pressure'] = float(data['main']['pressure'])
    city_weather['wind_speed'] = float(data['wind']['speed'])
    city_weather['icon_url'] = 'http://openweathermap.org/img/w/{}.png'.format(data['weather'][0]['icon'])

    return city_weather
