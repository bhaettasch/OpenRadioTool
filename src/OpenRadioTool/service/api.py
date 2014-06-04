from service.models import Traffic, WeatherCurrent, WeatherForecast
from tastypie.resources import ModelResource


class TrafficResource(ModelResource):
    class Meta:
        queryset = Traffic.objects.all()
        resource_name = 'traffic'


class WeatherCurrentResource(ModelResource):
    class Meta:
        queryset = WeatherCurrent.objects.all()
        resource_name = 'weatherCurrent'


class WeatherForecastResource(ModelResource):
    class Meta:
        queryset = WeatherForecast.objects.all()
        resource_name = 'weatherForecast'