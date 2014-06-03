from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
import requests
from service.JSONView import JSONView

from service.models import Traffic, WeatherCurrent


class IndexView(generic.TemplateView):
    template_name = 'service/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Service Display'
        return context


class JSONTrafficView(JSONView):
    model = Traffic


class CurrentWeatherView(generic.View):
    """
    Load current weather data into database
    To be called by cron job
    """

    def get(self, request, *args, **kwargs):

        #Get current weather data
        current = WeatherCurrent.objects.all()[0]
        params = {'id': '2950978', 'units': 'metric', 'lang': 'de', 'cnt': '1'}
        r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)
        data = r.json()

        current.temperature = data['main']['temp']
        current.humidity = data['main']['humidity']
        current.weather = data['weather'][0]['description']
        current.symbol = data['weather'][0]['icon']
        current.save()

        #Get forecast
        #TODO

        return HttpResponse(r.status_code)