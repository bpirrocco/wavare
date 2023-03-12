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

def get_forecast_data(data, interval):
    """Function used to get the correct data for desired interval.
    
    Args:
        
        data: pandas dataframe of hourly forecast json
        
        interval: interval provided in querystring

    Returns:

        today: today's date formatted to be easily readable

        time_list: list of times for forecasts

        data_list: list of data for forecasts
    
    """
    format_data = "%Y-%m-%dT%H:%M:%SZ"
    time_list = []

    if interval == "hourly":
        datetime_list = data.loc[:, "date"]
        date = datetime.strptime(datetime_list[0], format_data)
        today = date.strftime("%A, %B %-d")
        for datetime in datetime_list:
            new_date = datetime.strptime(datetime, format_data)
            time_list.append(new_date.strftime("%-I%p"))
        data_list = data.loc[:, "max_wave_height"]
        return today, time_list, data_list
