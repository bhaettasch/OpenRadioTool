from django.conf.urls import *
from service.api import TrafficResource, WeatherCurrentResource, WeatherForecastResource
from tastypie.api import Api
from service import views

v1_api = Api(api_name='v1')
v1_api.register(TrafficResource())
v1_api.register(WeatherCurrentResource())
v1_api.register(WeatherForecastResource())

trafficResource = TrafficResource()

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^api/', include(v1_api.urls), name='api'),
    url(r'^loadWeather$', views.CurrentWeatherView.as_view(), name='load_weather'),
    url(r'^json/traffic$', views.JSONTrafficView.as_view(), name='traffic_json')
]