from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Index
    :param request: HTTP Request handled
    """
    context = {'title': 'Service Display'}
    return render(request, 'service/index.html', context)