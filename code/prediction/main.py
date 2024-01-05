import time
import os
import json
import datetime as dt
from nhp_method import predict_poisson
from config import file_name1, file_name2, file_name3, file_name4, file_name5, file_name6, total_occupancy

# Write to json file
def write_json(data_entity, json_name, parking_id):
    # Data transformation
    data = ["AVAILABLE"] * data_entity + ["OCCUPIED"] * (total_occupancy[parking_id] - data_entity)

    entry = []

    for child_id, child in enumerate(data, 101):
        if child == "OCCUPIED":
            entry.append({"id": str(child_id), "state": "O"})
        else:
            entry.append({"id": str(child_id), "state": "E"})
    json_obj = json.dumps(entry)
    with open(json_name, 'w') as f:
        f.write(json_obj)

# Main function
def main():
    while True:
        cur_time = dt.datetime.now()
        
        # Park 45 data
        # 1 Hour
        data45 = predict_poisson(cur_time, 1, "45")
        write_json(data45, file_name1, "45")

        # 5 Hours
        data45 = predict_poisson(cur_time, 5, "45")
        write_json(data45, file_name2, "45")

        # 12 Hours
        data45 = predict_poisson(cur_time, 12, "45")
        write_json(data45, file_name3, "45")

        # Park 46 data
        # 1 Hour
        data46 = predict_poisson(cur_time, 1, "46")
        write_json(data46, file_name4, "46")

        # 5 Hours
        data46 = predict_poisson(cur_time, 5, "46")
        write_json(data46, file_name5, "46")

        # 12 Hours
        data46 = predict_poisson(cur_time, 12, "46")
        write_json(data46, file_name6, "46")
        
        # Interval is 30 minutes
        time.sleep(60 * 30)

if __name__ == "__main__":
    main()