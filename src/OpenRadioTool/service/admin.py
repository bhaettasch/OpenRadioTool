from django.contrib import admin
from service.models import Traffic


class TrafficAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Wo", {'fields': ['where', 'direction']}),
        ("Was", {'fields': ['what', 'text']}),
        (None, {'fields':['prio']})
    ]

    list_display = ('what', 'where', 'direction', 'prio', 'updated')

    list_filter = ['what']


admin.site.register(Traffic, TrafficAdmin)