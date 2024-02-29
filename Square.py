from codrone_edu.drone import *
from src.DroneManager import DroneHandler
import traceback
from src.LiveGraph import LiveGraph
from FakeDrone import FakeDrone
import numpy as np


# plotData = [grain,dataAmount,dataNames,overAllName,colors]

# lg = LiveGraph(([10,3,["input","Pos","pidOut"],"xPid",["r","b","g"]],
#                 [10,3,["input","Pos","pidOut"],"yPid",["k","g","y"]],
#                 [10,3,["input","Pos","pidOut"],"zPid",["y","m","violet"]]))
# lg.interactiveMode()

drone = Drone()
droneManager = DroneHandler(drone)
print("--Innit Complete--")

try:
    drone.pair()
    drone.takeoff()
    while not drone.r2_pressed():
        pass
        # droneManager.move([0,0,.5])
        
        
        h =2
        droneManager.move([0,0,h])
        print(droneManager.curPos[2])
        # droneManager.sequential_movement([(0,0,h),
        #                                 (1,0,h),
        #                                 (1,1,h),
        #                                 (0,1,h),
        #                                 (0,0,h)
        #                                 ])
    
    

    drone.land()
    drone.close()

except Exception as e:
    traceback.print_exc()
    drone.land()
    drone.close()

