from codrone_edu.drone import *
from DroneManager import DroneHandler
import traceback
from LiveGraph import LiveGraph

#plotData = [grain,dataAmount,dataNames,overAllName,colors]

lg = LiveGraph(([10,3,["input","output","pidOut"],"xPid",["r","b","g"]],
                [10,3,["input","output","pidOut"],"yPid",["k","g","y"]],
                [10,3,["input","output","pidOut"],"zPid",["y","m","violet"]]))
lg.interactiveMode()
droneManager = DroneHandler(Drone())


try:
    drone = Drone()
    drone.pair()
    drone.takeoff()
    while  not drone.r2_pressed():
        droneManager.move((0,0,1))
        droneManager.update(drone.get_position_data())
        
        
        lg.update([droneManager.getPrintData(0),droneManager.getPrintData(1),droneManager.getPrintData(2)])
        
        # drone.hover(.01)
        # print(drone.r2_pressed())
    drone.land()
    drone.close()

except Exception as e:
    traceback.print_exc()
    drone.land()
    drone.close()

