import time
from picarx import Picarx

px = Picarx()
px.set_dir_servo_angle(20)
time.sleep(0.5)
px.set_dir_servo_angle(-20)
time.sleep(0.5)
px.set_dir_servo_angle(0)
time.sleep(0.5)
px.forward(10)
time.sleep(1)
px.backward(10)
time.sleep(1)
px.forward(0)
px.stop()