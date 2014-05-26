from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from service.JSONView import JSONView

from service.models import Traffic


class IndexView(generic.TemplateView):
    template_name = 'service/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Service Display'
        return context


class JSONTrafficView(JSONView):
    model = Traffic

