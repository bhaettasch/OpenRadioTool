from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from service.models import Traffic


def index(request):
    """
    Index
    :param request: HTTP Request handled
    """
    context = {'title': 'Service Display'}
    return render(request, 'service/index.html', context)


def traffic_json(request):
    """
    Return the current traffic information as json data block

    :param request: HTTP Request to handle
    :return: A json formatted plain string containing the current traffic information
    """
    return HttpResponse(serializers.serialize("json", Traffic.objects.all()))
