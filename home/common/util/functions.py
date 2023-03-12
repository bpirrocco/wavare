import json
from datetime import datetime

# format_data = "%Y-%m-%dT%H:%M:%S.%fZ"
# time_list = []
def get_forecast_datetime(data, time_list, date_list):
    format_data = "%Y-%m-%dT%H:%M:%SZ"
    for dict in data:
        new_date = datetime.strptime(dict['date'], format_data)
        time_list.append(new_date.strftime("%-I%p"))
        date_list.append(new_date.strftime("%B, %-d"))

def get_forecast_date(data, date_list):
    format_data = "%Y-%m-%dT%H:%M:%S.%fZ"
