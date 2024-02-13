from codrone_edu.drone import *
from DroneManager import DroneHandler
import traceback
from LiveGraph import LiveGraph
from FakeDrone import FakeDrone

# plotData = [grain,dataAmount,dataNames,overAllName,colors]

lg = LiveGraph(([10,3,["input","Pos","pidOut"],"xPid",["r","b","g"]],
                [10,3,["input","Pos","pidOut"],"yPid",["k","g","y"]],
                [10,3,["input","Pos","pidOut"],"zPid",["y","m","violet"]]))
lg.interactiveMode()

drone = Drone()
droneManager = DroneHandler(drone)

try:
    drone.pair()
    drone.takeoff()
    while  not drone.r2_pressed():
        droneManager.move((0,0,1.8))
        droneManager.update()
        
        lg.update([droneManager.getPrintData(0),droneManager.getPrintData(1),droneManager.getPrintData(2)])
        

    drone.land()
    drone.close()

except Exception as e:
    traceback.print_exc()
    drone.land()
    drone.close()

