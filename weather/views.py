# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from weather.models import City
from weather.service import weather_by_city_id


class HomeView(TemplateView):
    template_name = 'weather/home.html'


class CitySearchListView(ListView):
    model = City
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        try:
            return super(CitySearchListView, self).get(request, *args, **kwargs)
        except Http404:
            response = redirect('weather:search_results')
            params = '?q={q};page={page}'.format(q=request.GET.get('q'), page=1)
            response['Location'] += params
            return response

    def get_queryset(self):
        city_name = self.request.GET.get('q')
        return self.model.objects.filter(name__istartswith=city_name)

    def get_context_data(self, **kwargs):
        context = super(CitySearchListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')

        self.trim_pagination(context)

        return context

    def trim_pagination(self, context):
        page = self.request.GET.get('page')

        if page is None:
            page = '1'

        if page.isdigit():
            page_num = int(page)
            page_start = page_num - 3
            page_finish = page_num + 3
            last_page = context['paginator'].num_pages

            if page_start <= 1:
                page_finish += 1 - page_start
                page_start = 1
            else:
                context['first'] = 1

            if page_finish >= last_page:
                page_finish = last_page
            else:
                context['last'] = last_page

            context['page_range'] = xrange(page_start, page_finish + 1)


class CityWeatherView(TemplateView):
    template_name = 'weather/city_weather.html'
    partial_template_name = 'weather/city_weather_partial.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            # # Get random city.
            # self.kwargs['city_id'] = City.objects.order_by('?').first().id
            return render(request, self.partial_template_name, self.get_context_data(**kwargs))
        return super(CityWeatherView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CityWeatherView, self).get_context_data(**kwargs)
        context['city_weather'] = weather_by_city_id(self.kwargs['city_id'])
        context['city_id'] = self.kwargs['city_id']
        return context
