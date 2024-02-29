from codrone_edu.drone import *
from src.DroneManager import DroneHandler
import traceback
from src.LiveGraph import LiveGraph
from FakeDrone import FakeDrone
import numpy as np
from src.Course import *



drone = Drone()
droneManager = DroneHandler(drone)
print("--Innit Complete--")

try:
    drone.pair()
    while not drone.r2_pressed():
        pass
        # droneManager.move([0,0,.5])
        print(drone.get_position_data()[1:])
    
    
    

    drone.land()
    drone.close()

except Exception as e:
    traceback.print_exc()
    drone.land()
    drone.close()

