# -*- coding: utf-8 -*-
import json
import urllib2

WEATHER_API_KEY = '7ec667bf669cce3a71b5381e2fcdbf75'


def weather_by_city_id(city_id):
    url_template = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid={}'
    url = url_template.format(city_id, WEATHER_API_KEY)
    response = urllib2.urlopen(url).read()
    return json.loads(response)
