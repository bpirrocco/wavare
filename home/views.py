import json
import datetime as dt

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import RedirectView
from django.http import Http404

from .models import Location, Forecast
from .common.util import functions
from .forms import ForecastForm

# import meteomatics.api as api


def welcome(request):
    urldate = dt.datetime(2023, 2, 10)
    return render(request, "home/home.html", {"urldate": urldate})

def nazare(request):
    # USERNAME = 'personaluse_pirrocco'
    # PASSWORD = '07hY0reaKI'
    # coords = [(39.6033193, -9.0912258)]
    # startdate = dt.datetime.utcnow().replace(hour=1, minute=0, second=0, microsecond=0)
    # enddate = startdate + dt.timedelta(days=1)
    # interval = dt.timedelta(hours=1)
    # parameters = ['max_individual_wave_height:m']

    # wave_height = api.query_time_series(coords, startdate, enddate, interval, parameters, USERNAME, PASSWORD)

    # return render(request, "home/nazare.html", {"wave_height": wave_height})
    return render(request, "home/nazare.html")

def forecast(request, location, date, interval):
    forecast = get_object_or_404(Forecast, location = location, date = date, interval = interval)
    forecast_file = forecast.filename
    # with open('media/test/' + forecast_file, "r") as read_file:
    #     data = json.load(read_file)
    pre_data = forecast_file.file.open('r')
    data = json.load(pre_data)
    time_list = []
    date_list = []
    functions.get_forecast_datetime(data, time_list, date_list)
    data_list = list(enumerate(data))
    # data = json.dumps(json_data)
    return render(request, "home/forecast.html", {"forecast": forecast, "data": data, "time_list": time_list, "date_list": date_list, "data_list": data_list})


def locations(request):

    return render(request, "home/location.html", {"location": Location.objects.all()})
    
class QuerystringRedirect(RedirectView):
    
    permanent = False
    query_string = False
    pattern_name = 'forecast'

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Forecast, location=kwargs['location'], date=kwargs['date'], interval=['interval'])
        return super().get_redirect_url(*args, **kwargs)

def contact(request):
    return render(request, "home/contact.html")

def about(request):
    return render(request, "home/about.html")