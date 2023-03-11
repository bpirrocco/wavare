from django.contrib import admin

from .models import Location, Forecast, ForecastTest


admin.site.register(Location)
admin.site.register(Forecast)
admin.site.register(ForecastTest)