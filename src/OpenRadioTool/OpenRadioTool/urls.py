from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OpenRadioTool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'service/', include('service.urls', namespace="service")),
    url(r'^admin/', include(admin.site.urls)),
)
