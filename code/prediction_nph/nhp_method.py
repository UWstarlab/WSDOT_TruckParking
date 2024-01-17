import datetime as dt
from extract_data import get_capacity
from config import total_occupancy, h_interval, week_second

'''
* onhomogeneous Poisson (NHP)
* cur_time: current time for prediction
* k: interval between prediction and current time
'''
def predict_poisson(cur_time, k, parking_id="45"):
    W = 3
    H = 3
    cap = total_occupancy[parking_id]

    a_tk = 0
    a_t = get_capacity(cur_time, parking_id)
    v_sum = 0

    for i in range(1, k + 1):
        v_sum += compute_mean_v(cur_time + dt.timedelta(seconds=i * h_interval), W, H, cap)
    a_tk = a_t + cap * v_sum

    return int(a_tk)

'''
* Compute the ratio of arrivals / reservations
* (a_t - a_{t-1}) / cap
* a_t is the parking avalibity at time t
* a_{t-1} is the parking avalibity at time t - 1
* cap: total capacity
'''
def compute_v(a_t, a_t1, cap):
    return (a_t - a_t1) / cap

def compute_mean_v(cur_time, W, H, cap):
    v_sum = 0

    for j in range(1, W + 1):
        for i in range(H):
            a_t = get_capacity(cur_time - dt.timedelta(seconds=i * h_interval + j * week_second))
            a_t1 = get_capacity(cur_time - dt.timedelta(seconds=(i + 1) * h_interval + j * week_second))
            v_sum += compute_v(a_t, a_t1, cap)
    
    return v_sum / W / H