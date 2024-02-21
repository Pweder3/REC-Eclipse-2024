from codrone_edu.drone import *
from DroneManager import DroneHandler
import traceback
from LiveGraph import LiveGraph
from FakeDrone import FakeDrone
import numpy as np
from Course import *


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
        
        
        
        droneManager.move(
            [inchtoM(110),0,.3]
        )
        print(f"error: {np.average(np.subtract(droneManager.curPos, droneManager.curTarget))}:.2f target {droneManager.curTarget} curent {droneManager.curPos[0]*39.37  }")
    

    drone.land()
    drone.close()

except Exception as e:
    traceback.print_exc()
    drone.land()
    drone.close()

