from django.http import HttpResponse
from django.views import generic
from django.core import serializers


class JSONView(generic.ListView):
    """
    Generic View for all kinds of Models transferred to JSON

    All filtering methods a listView offers may be used
    """
    def get(self, request, *args, **kwargs):
        data = serializers.serialize("json", self.get_queryset())
        return HttpResponse(data)