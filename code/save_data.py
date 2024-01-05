# Configure information
username = ""
password = ""

# Nisqually: 45
# Scatter Creek: 46
total_occupancy = {"45": 37, "46": 12}

history_url = "https://parking.sensysnetworks.net/snaps/dataservice/parkingHistory.xml"
current_url = "https://parking.sensysnetworks.net/snaps/dataservice/parkingStatus.xml"

week_second = 604800 # Week to seconds
h_interval = 3600 # Hour to seconds

json_file_name1 = "C:/Users/staradmin/Desktop/truckparking/web_display_restarea.json"
json_file_name2 = "C:/Users/staradmin/Desktop/truckparking/web_display_weightstation.json"
txt_file_folder = "C:/Users/staradmin/Desktop/truckparking/data/"

import requests
import xml.etree.ElementTree as et
import datetime as dt
import time
import os
import json

# Get current parking data for a specific lot
def get_current_data(parking_id):
    # Assemble a request
    data = {'username': username, 'password': password, 'lotId': parking_id}
    
    r = requests.post(url=current_url, data=data)
    root = et.fromstring(r.content)
    gen = ((child.attrib['id'], child.attrib['state']) for child in root.iter('space'))
    my_data = [child for child in gen]

    # Output includes sensor_id, parking_status, time
    return sorted(my_data, key=lambda x: int(x[0]))

# Write to txt file
def write_txt(data, ctime, parking_id):
    txt_file_name = txt_file_folder + str(parking_id) + "_" + str(cur_time.year) + str(cur_time.month).zfill(2) + str(cur_time.day).zfill(2) + ".txt"

    with open(txt_file_name, 'a') as f:
        f.write("*******************\n")
        f.write(str(ctime.year) + str(ctime.month).zfill(2) + str(ctime.day).zfill(2) + str(ctime.hour).zfill(2) + str(ctime.minute).zfill(2) + '\n')
        for d in data:
            f.write(d[0] + '_' + d[1] + '\n')

# Write to json file
def write_json(data, json_name):
    entry = []
    for child_id, child in enumerate(data, 101):
        if child[1] == "OCCUPIED":
            entry.append({"id": str(child_id), "state": "O"})
        else:
            entry.append({"id": str(child_id), "state": "E"})
    json_obj = json.dumps(entry)
    with open(json_name, 'w') as f:
        f.write(json_obj)

if __name__ == "__main__":
    while True:
        cur_time = dt.datetime.now()
        
        # Park 45 data
        park45 = get_current_data(parking_id=45)
        write_txt(data=park45, ctime=cur_time, parking_id=45)
        write_json(data=park45, json_name=json_file_name1)

        # Park 46 data
        park46 = get_current_data(parking_id=46)
        write_txt(data=park46, ctime=cur_time, parking_id=46)
        write_json(data=park46, json_name=json_file_name2)

        # Sleep interval (seconds)
        time.sleep(30)