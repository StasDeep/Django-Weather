# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView

from weather.service import weather_by_city_id


class HomeView(TemplateView):
    template_name = 'weather/home.html'


class CityWeatherView(TemplateView):
    template_name = 'weather/city_weather.html'

    def get_context_data(self, **kwargs):
        context = super(CityWeatherView, self).get_context_data(**kwargs)
        context['city_weather'] = weather_by_city_id(self.kwargs['city_id'])
        return context
