from codrone_edu.drone import *
from src.DroneManager import DroneHandler
import traceback
from src.LiveGraph import LiveGraph
from FakeDrone import FakeDrone
import numpy as np
from src.Course import *


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
    drone.set_drone_LED(255,255,255,100) # makes white
    time.sleep(1)
    innit_color = droneManager.get_pad_color()
    drone.takeoff()
    

    testPoints = [2.7232189178466797, inchtoM(68)]
        
    droneManager.sequential_movement([
        (Y_KEYHOLE_XY[0] - inchtoM(4),0,Y_KEYHOLE_BASE_HEIGHT + (KEYHOLE_DIAMATER/2)), # moves infront of yellow keyhole
        (G_KEYHOLE_XY[0] ,-inchtoM(1),Y_KEYHOLE_BASE_HEIGHT + (KEYHOLE_DIAMATER/2)),
        (G_KEYHOLE_XY[0] ,-inchtoM(1),(G_KEYHOLE_BASE_HEIGHT + KEYHOLE_DIAMATER/2)), #goes throught the yellow keyhole and infront of green keyhole
        (G_KEYHOLE_XY[0] ,inchtoM(-1),(G_KEYHOLE_BASE_HEIGHT + KEYHOLE_DIAMATER/2)),
        (G_KEYHOLE_XY[0] ,inchtoM(12*3),(G_KEYHOLE_BASE_HEIGHT + KEYHOLE_DIAMATER/2)),
        (LANDING_PAD[0], testPoints[1],inchtoM(3*12)), # goes though the green keyhole and gets ready to land
    ])
    
    droneManager.get_pad_color()
    
    
    
    print("close")

    drone.land()
    drone.close()

except Exception as e:
    traceback.print_exc()
    drone.land()
    drone.close()

