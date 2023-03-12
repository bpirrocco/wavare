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
        date = datetime_list[0]
        today = date.strftime("%A, %B %-d")
        for date in datetime_list:
            time_list.append(date.strftime("%-I%p"))
        pre_data_list = list(df['max_wave_height'])
        key = ["max_wave_height"]
        value = [""]
        data_list = []
        for item in pre_data_list:
            i = pre_data_list.index(item)
            value[0] = pre_data_list[i]
            pre_data = dict(zip(key, value))
            data_list.append(pre_data)
        return today, time_list, data_list
