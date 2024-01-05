# Extract data
import requests
import xml.etree.ElementTree as et
import datetime as dt
from config import *

def get_historical_data(start_time, period, parking_id):
    # Transform start_time and period to string
    # "start_time" format is datetime
    # "period" format is int (unit is seconds) 
    if type(start_time) != str:
        start_time_str = str(int((start_time - dt.datetime(1970, 1, 1)).total_seconds()))
    if type(period) != str:
        period_str = str(period)

    # Assemble a request
    data = {'username': username,
            'password': password,
            'startTime': start_time_str,
            'period': period_str,
            'lotId': parking_id
            }
    
    r = requests.post(url=history_url, data=data)
    root = et.fromstring(r.content)
    gen = ((child.attrib['id'], child.attrib['state'], child.attrib['time']) for child in root.iter('space'))
    my_data = [child for child in gen]

    # Output includes sensor_id, parking_status, time
    return my_data

def get_current_data(parking_id):
    # Assemble a request
    data = {'username': username,
            'password': password,
            'lotId': parking_id
            }
    
    r = requests.post(url=current_url, data=data)
    root = et.fromstring(r.content)
    gen = ((child.attrib['id'], child.attrib['state'], child.attrib['time']) for child in root.iter('space'))
    my_data = [child for child in gen]

    # Output includes sensor_id, parking_status, time
    return my_data

# parking_id = "45" # Nisqually Weigh Station
# parking_id = "46" # Scatter Creek Rest Area
def get_capacity(time, parking_id="45"):
    time = time + dt.timedelta(hours=8)
    res = get_historical_data(time, 30, parking_id)
    output = {}

    for r in res:
        key = r[0]
        if key not in output:
            output[key] = r[1]
    
    #occupancy = total_occupancy[parking_id]
    available = 0

    for key in output.keys():
        if output[key] != "OCCUPIED":
            available += 1
    
    #return available / occupancy
    return available