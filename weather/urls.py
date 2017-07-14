from django.conf.urls import url

from weather.views import HomeView, CityWeatherView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<city_id>\d+)$', CityWeatherView.as_view(), name='city_weather')
]
