from django.conf.urls import url

from weather.views import HomeView, CityWeatherView, CitySearchListView

app_name = 'weather'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^search$', CitySearchListView.as_view(), name='search_results'),
    url(r'^(?P<city_id>\d+)$', CityWeatherView.as_view(), name='city_weather')
]
