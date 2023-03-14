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
import pandas as pd


def welcome(request):
    # urldate = dt.datetime(2023, 2, 10)
    urldate = dt.date.today()
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
    forecast = get_object_or_404(Forecast, location = location, date = date, interval = "hourly")
    forecast_file = forecast.filename
    pre_data = forecast_file.file.open('r')
    data = json.load(pre_data)
    date_list = []
    time_list = []
    time_of_day = ['Morning', 'Afternoon', 'Evening', 'Night']

    if interval == "hourly":
        time_list, data_list, today = functions.get_forecast_data(data, interval)
    elif interval == "daily":
        date_list, data_list, today = functions.get_forecast_data(data, interval)
    else:
        data_list, today = functions.get_forecast_data(data, interval)
    
    data_list = list(enumerate(data_list))

    hourly = (interval == "hourly")
    daily = (interval == "daily")
    today_bool = (interval == "today")

    return render(request, "home/forecast.html", {"forecast": forecast, "time_list": time_list, "date_list": date_list, "data_list": data_list, "hourly": hourly, "daily": daily, "today": today_bool, "date": today, "time_of_day": time_of_day})

def daily_forecast(request, location, date):
    forecast = get_object_or_404(Forecast, location = location, date = date, interval = "daily")
    forecast_file = forecast.filename
    pre_data = forecast_file.file.open('r')
    df = pd.read_json(pre_data)
    return render(request, "home/forecast.html", {"interval": "daily"})


def forecasts(request):
    return render(request, "home/location.html", {"location": Location.objects.all()})

def contact(request):
    return render(request, "home/contact.html")

def about(request):
    return render(request, "home/about.html")