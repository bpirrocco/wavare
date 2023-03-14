import json
from datetime import datetime, timedelta
import random

from .fg_shared import generate_height

format_data = "%Y-%m-%dT%H:%M:%SZ"
# time_list = []
# def get_forecast_datetime(data, time_list, date_list):
#     format_data = "%Y-%m-%dT%H:%M:%SZ"
#     for dict in data:
#         new_date = datetime.strptime(dict['date'], format_data)
#         time_list.append(new_date.strftime("%-I%p"))
#         date_list.append(new_date.strftime("%B, %-d"))

def get_forecast_time_list(data):
    time_list = []
    for dict in data:
        new_date = datetime.strptime(dict['date'], format_data)
        time_list.append(new_date.strftime("%-I%p"))
    return time_list

def get_forecast_date(date):
    date = datetime.strptime(date, format_data)
    today = date.strftime("%A, %B %-d")
    return today

def get_daily_list(date):
    date = datetime.strptime(date, format_data)
    day = timedelta(days=1)
    date_list = [date,]

    for el in range(0, 9):
        new_date = date_list[el] + day
        date_list.append(new_date)
    return date_list

def get_hourly_datalist(data):
    data_list = []
    for dict in data:
        data_list.append(dict['max_wave_height'])
    return data_list

def get_daily_datalist(data_list):
    total = 0
    for el in range(0, len(data_list)):
        total = total + data_list[el]
    total = total / (len(data_list))

    height_list = [total,]
    range_start = total - 1.2
    range_end = range_start + 2.5
    height_list = height_list + [(generate_height(int(range_start), int(range_end)) * 10) for x in range(9)]
    return height_list

def get_today_datalist(data_list):
    for x in range(7):
        morning += data_list[x]
    for x in range(5):
        afternoon += data_list[x+7]
    for x in range(5):
        evening += data_list[x+12]
    for x in range(7):
        night += data_list[x+17]

    morning = morning / 7
    afternoon = afternoon / 5
    evening = evening / 5
    night = night / 7
    return morning, afternoon, evening, night

def get_forecast_data(data, interval):
    time_list = get_forecast_time_list(data)
    date = data[0]['date']
    today = get_forecast_date(date)
    data_list = get_hourly_datalist(data)

    if interval == "today":
        morning, afternoon, evening, night = get_today_datalist(data_list)
        data_list = [morning, afternoon, evening, night]
        return data_list, today
    elif interval == "daily":
        date_list = get_daily_list(date)
        data_list = get_daily_datalist(data_list)
        return date_list, data_list, today
    else:
        return time_list, data_list, today


# def get_forecast_data1(data, interval):
#     """Function used to get the correct data for desired interval.
    
#     Args:
        
#         data: pandas dataframe of hourly forecast json
        
#         interval: interval provided in querystring

#     Returns:

#         today: today's date formatted to be easily readable

#         time_list: list of times for forecasts

#         data_list: list of data for forecasts
    
#     """
#     format_data = "%Y-%m-%dT%H:%M:%SZ"
#     time_list = []

#     if interval == "hourly":
#         datetime_list = data.loc[:, "date"]
#         date = datetime_list[0]
#         today = date.strftime("%A, %B %-d")
#         for date in datetime_list:
#             time_list.append(date.strftime("%-I%p"))
#         pre_data_list = list(df['max_wave_height'])
#         key = ["max_wave_height"]
#         value = [""]
#         data_list = []
#         for item in pre_data_list:
#             i = pre_data_list.index(item)
#             value[0] = pre_data_list[i]
#             pre_data = dict(zip(key, value))
#             data_list.append(pre_data)
#         return today, time_list, data_list

# This function is too complex for no reason. 
# Let's get back to using the get_forecast_datetime function and build off the logic and structures
# I was using there. This should simplify this funciton. No need to turn anything into a pandas dataframe
