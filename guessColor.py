from codrone_edu.drone import *
from DroneManager import DroneHandler
import traceback
from LiveGraph import LiveGraph
from FakeDrone import FakeDrone
import numpy as np
from Course import *

drone = Drone()
droneManager = DroneHandler(drone)
print("--Innit Complete--")

try:
    drone.pair()
    drone.reset_sensor()
    while not drone.r2_pressed():
        
        RED = [255,0,0]
        GREEN = [0,255,0]
        BLUE = [0,0,255]
        
        color_data = drone.get_color_data()
        hue = color_data[1]
        if 0 <= hue < 60:
            color = "Red"
            drone.set_drone_LED(*RED,100)
        elif 60 <= hue < 180:
            color = "Green"
            drone.set_drone_LED(*GREEN,100)
        elif 180 <= hue < 300:
            color = "Blue"
            drone.set_drone_LED(*BLUE,100)
        print("Detected color:", color)
        

    drone.close()

except Exception as e:
    traceback.print_exc()
    drone.land()
    drone.close()

