import datetime as dt
from datetime import datetime

from unidecode import unidecode

from fg_shared import generate_json, generate_height_list


def generate_time_list(length):
    base = datetime.now()
    datetime_list = [base + dt.timedelta(hours=x) for x in range(length)]
    time_list = []
    for date in datetime_list:
        # pandas.Timestamp.round('60min').to_pydatetime()
        time = date.replace(second=0, microsecond=0, minute=0)
        time_list.append(time.strftime("%Y-%m-%dT%H:%M:%SZ"))
    return time_list

def generate_hourly_forecast(location, length):
    time_list = generate_time_list(length)
    height_list = generate_height_list(length)
    keys = ["date", "max_wave_height"]
    values = ['', '']
    data = []

    # Why don't we turn each entry into a dict first? Maybe:

    for dates in time_list:
        i = time_list.index(dates)
        values[0] = time_list[i]
        values[1] = height_list[i]
        pre_data = dict(zip(keys, values))
        data.append(pre_data)

    # That worked :)

    generate_json(location, 'hourly', data)