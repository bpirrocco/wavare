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

# Models
from home.models import Location, Forecast


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

    # podcast_title = feed.channel.title
    # podcast_image = feed.channel.image["href"]

    # for item in feed.entries:
    #     if not Episode.objects.filter(guid=item.guid).exists():
    #         episode = Episode(
    #             title=item.title,
    #             description=item.description,
    #             pub_date=parser.parse(item.published),
    #             link=item.link,
    #             image=podcast_image,
    #             podcast_name=podcast_title,
    #             guid=item.guid,
    #         )
    #         episode.save()