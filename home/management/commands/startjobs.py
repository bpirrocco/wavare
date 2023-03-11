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
from home.models import Location, Forecast, ForecastTest
from ...common.util import fg_shared, fg_daily, fg_hourly


logger = logging.getLogger(__name__)
BASE_DIR = settings.BASE_DIR
MEDIA_ROOT = settings.MEDIA_ROOT


def save_new_forecasts():
    """Saves new forecasts to the database


    Takes the paths to the newly generated json files and uses them to 

    save new forecasts to the database


    Args:

        location: takes a list of all Locations

    """
    locations = Location.objects.values_list("location", flat=True)
    date = dt.date.today().strftime("%Y-%m-%d")

    for location in locations:
        if not Forecast.objects.filter(date = date).exists:
            daily_data = create_daily_forecast(location)
            hourly_data = create_hourly_forecast(location)
            daily_forecast = Forecast(
                location = location,
                date = date,
                interval = daily_data[0],
                filename = daily_data[1]
                # interval = 'daily',
                # filename = 'wavare/home/media/test/nazare_daily_3.11.23'
            )
            daily_forecast.save()
            hourly_forecast = Forecast(
                location = location,
                date = date,
                interval = hourly_data[0],
                filename = hourly_data[1]
                # interval = 'hourly',
                # filename = 'wavare/home/media/test/nazare_hourly_3.11.23'
            )
            hourly_forecast.save()

def create_daily_forecast(location):
    """Create daily forecasts for each location.
    
    Args: 
    
        Location: a string of a location contained in the db
        
    Returns:
    
        A list containing the info needed to create a Forecast model
    
    """

    interval = "daily"
    filepath = fg_daily.generate_daily_forecast(location, 10)

    return [interval, filepath]

def create_hourly_forecast(location):
    """Create hourly forecasts for each location.
    
    Args:
    
        Location: a string of a location contained in the db
        
    Returns:
    
        A list containing the info needed to create a Forecast model
        
    """

    interval = "hourly"
    filepath = fg_hourly.generate_hourly_forecast(location, 24)

    return [interval, filepath]

def test_json_generator():
    fg_hourly.generate_hourly_forecast("Nazaré", 24)

def delete_old_job_executions(max_age=604_800):
    """Deletes all apscheduler job execution logs older than `max_age`."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)

class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # scheduler.add_job(
        #     save_new_forecasts,
        #     trigger="interval",
        #     seconds=30,
        #     id="Forecasts",
        #     max_instances=1,
        #     replace_existing=True,
        # )
        # logger.info("Added job: Save New Forecasts")

        scheduler.add_job(
            test_json_generator,
            trigger="interval",
            seconds=30,
            id="TEST",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: TEST")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="Delete Old Job Executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: Delete Old Job Executions.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")