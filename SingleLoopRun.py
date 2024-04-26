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
        (Y_KEYHOLE_XYZ[0]+ inchtoM(12) ,0,Y_KEYHOLE_XYZ[2]), # moves infront of yellow keyhole
        (Y_KEYHOLE_XYZ[0] ,inchtoM(15),Y_KEYHOLE_XYZ[2] - inchtoM(5)),
    ],timeOut= 100)
    
    
    drone.set_drone_LED(
    *droneManager.get_pad_color(20),100
    )
    
    
    print("close")

    drone.land()
    drone.close()

except Exception as e:
    traceback.print_exc()
    drone.land()
    drone.close()

