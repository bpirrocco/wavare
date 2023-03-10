import logging
import datetime as dt
from datetime import datetime

# Django
from django.conf import settings
from django.core.management.base import BaseCommand

# Third Party
from dateutil import parser
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

# Models & Functions
from home.models import Location, Forecast
from ...common.util import fg_shared, fg_daily, fg_hourly


logger = logging.getLogger(__name__)

def save_new_forecast(locations):
    """Saves new forecasts to the database


    Takes the paths to the newly generated json files and uses them to 

    save new forecasts to the database


    Args:

        location: takes a list of all Locations

    """

    for location in locations:
        if not Forecast.objects.filter(location_id = location):
            forecast = Forecast(
                date = dt.date.today().strftime("%Y.%m.%d")
            )

