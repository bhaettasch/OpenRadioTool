from django.conf.urls import url
from service import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^json/traffic$', views.JSONTrafficView.as_view(), name='traffic_json')
]