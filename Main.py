from codrone_edu.drone import *
from DroneManager import DroneHandler
import traceback
from LiveGraph import LiveGraph
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

z_pos = np.zeros((2,0))
try:
    drone.pair()
    drone.takeoff()
    while not drone.r2_pressed():
        # droneManager.move([0,0,.5])
        
        z_pos = np.append(z_pos, [[drone.get_z_accel()-98 ], [droneManager.get_latest_time()]], axis=1)

        
        print(f"y pid: {droneManager.throttle_pid(drone.get_pos_z('m')):.2f}m " +
              f"y pos: {drone.get_pos_z('m'):.2f}m " +
              f"error average: {np.average(np.subtract(drone.get_position_data()[1:4], [0,0,.5])) } " + 
            #   f"vel: {np.gradient(z_pos)}) " +
            #   f"accel: {drone.get_z_accel()}m/s^2" ) 
        # *accelData used to unpack the array into the function.
        
        
        
    # droneManager.sequential_movement([(0,0,.5),
    #                                 (0,.5,.5),
    #                                 (0,0,.5)])
    
    

    drone.land()
    drone.close()

except Exception as e:
    traceback.print_exc()
    drone.land()
    drone.close()

