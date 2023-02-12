from django.contrib import admin

from .models import Location, Forecast


admin.site.register(Location)
admin.site.register(Forecast)