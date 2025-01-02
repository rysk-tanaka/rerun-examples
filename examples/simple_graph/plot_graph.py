import rerun as rr

rr.init("rerun_example_my_data1", spawn=True)

for x in range(100):
    # 時刻 x におけるセンサデータを記録
    rr.set_time_sequence("sensor_data", x)
    rr.log("sensor_data", rr.Scalar(x))
