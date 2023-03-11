import datetime as dt
from datetime import datetime
import random
import os

import pandas

from unidecode import unidecode

from django.conf import settings

# from daily import generate_daily_forecast

BASE_DIR = settings.BASE_DIR
MEDIA_ROOT = settings.MEDIA_ROOT
PATH = os.path.join(MEDIA_ROOT, 'bullpen/')

def generate_height(range_start, range_end):
    return float(random.randrange(range_start, range_end))/10

def generate_height_list(length):
    range_start = int(random.randrange(0, 300))
    range_end = range_start + 25
    return [generate_height(range_start, range_end) for x in range(length)]

def generate_filename(location, interval):
    date = dt.date.today().strftime("%Y.%m.%d")
    location = unidecode(location).lower()
    filename = f"{location}_{date}_{interval}.json"
    return filename

# def generate_data(location, interval):
#     if interval == 'hourly':
#         # generate_hourly_forecast(24)
#         pass
#     elif interval == 'today':
#         # generate_today_forecast(4)
#         pass
#     elif interval == 'daily':
#         generate_daily_forecast(location, interval)
#     else:
#         raise ValueError

def generate_json(location, interval, data):
    df = pandas.DataFrame(data=data)
    filename = generate_filename(location, interval)
    filepath = os.path.join(PATH, filename)
    df.to_json(filepath, orient='records')
    return filepath