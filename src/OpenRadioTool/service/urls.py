from django.conf.urls import url
from service import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^json/traffic$', views.traffic_json, name='traffic_json')
]