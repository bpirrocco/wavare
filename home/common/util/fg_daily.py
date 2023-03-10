import datetime as dt
from datetime import datetime

from unidecode import unidecode

from fg_shared import generate_json, generate_height_list

def generate_date_list(numdays):
    base = datetime.combine(dt.date.today(), datetime.min.time())
    datetime_list = [base + dt.timedelta(days=x) for x in range(numdays)]
    date_list = []
    for date in datetime_list:
        date_list.append(date.strftime("%Y-%m-%dT%H:%M:%SZ"))
    return date_list

def generate_daily_forecast(location, length):
    date_list = generate_date_list(length)
    height_list = generate_height_list(length)
    keys = ["date", "max_wave_height"]
    values = ['', '']
    data = []

    # Why don't we turn each entry into a dict first? Maybe:

    for dates in date_list:
        i = date_list.index(dates)
        values[0] = date_list[i]
        values[1] = height_list[i]
        pre_data = dict(zip(keys, values))
        data.append(pre_data)

    # That worked :)

    generate_json(location, 'daily', data)

