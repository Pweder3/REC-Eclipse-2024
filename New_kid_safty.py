from codrone_edu.drone import *
from src.DroneManager import DroneHandler
import traceback
from src.LiveGraph import LiveGraph
from FakeDrone import FakeDrone
import numpy as np
from src.Course import *
import pynput
from simple_pid import PID



drone = Drone()
drone.pair()

throttle_pid_data = (100, 0, 0)
#TODO: adjust PID values to precise movement.
level_PID = PID(Kp= throttle_pid_data[0], Ki=throttle_pid_data[1], Kd=throttle_pid_data[2], setpoint=.8, output_limits=(-100,100) )

def range_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def onRelease(key):
    
    if key == pynput.keyboard.Key.enter:
        for x in range(5): ## Dont need loop but redundancy is good
            pass
            # drone.emergency_stop()
        print("Emergency stop")
        
    if key == pynput.keyboard.Key.shift_r:
        # drone.land()
        print("Land")
        
    if key == pynput.keyboard.Key.space:
        # drone.takeoff()
        print("Takeoff")
        while drone.get_height("m") > .8:
            drone.set_throttle(level_PID(drone.get_height("m"))        


with pynput.keyboard.Listener(on_release= onRelease) as keyboard:
    while True:
        if drone.get_height("m") < .8:
            drone.set_throttle(range_map(drone.get_height("m"),0,.8,0,100))
            # TODO: Use PID algo to make sure even joystick will result in a hover.
        else:
            drone.set_throttle(level_PID(drone.get_height("m")))
            
