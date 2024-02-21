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
    drone.reset_sensor()
    time.sleep(1)
    drone.takeoff()
    while not drone.r2_pressed():
        pass
        # droneManager.move([0,0,.5])
        
        testPoints = [2.7232189178466797, 1.6]
        
        droneManager.sequential_movement([
            (Y_KEYHOLE_XY[0] - inchtoM(6),-inchtoM(3),Y_KEYHOLE_BASE_HEIGHT + (KEYHOLE_DIAMATER/2)), # moves infront of yellow keyhole
            (G_KEYHOLE_XY[0] ,-inchtoM(3),(G_KEYHOLE_BASE_HEIGHT + KEYHOLE_DIAMATER/2)), #goes throught the yellow keyhole and infront of green keyhole
            (testPoints[0] , testPoints[1],G_KEYHOLE_BASE_HEIGHT + (KEYHOLE_DIAMATER/2)), # goes though the green keyhole and gets ready to land
        ])
    
    
    

    drone.land()
    drone.close()

except Exception as e:
    traceback.print_exc()
    drone.land()
    drone.close()

