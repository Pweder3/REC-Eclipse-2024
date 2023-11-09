from codrone_edu.drone import *
from DroneHandler import DroneHandler
import traceback
from LiveGraph import LiveGraph

#plotData = [grain,dataAmount,dataNames,overAllName,colors]

lg = LiveGraph(([10,2,["input","output"],"Pid1",["r","b"]],[10,2,["input","output"],"Pid2",["k","g"]]))
lg.interactiveMode()
droneManager = DroneHandler(Drone())


try:
    drone = Drone()
    drone.pair()
    drone.takeoff()
    while  not drone.r2_pressed():
        droneManager.move((0,0,0))
        droneManager.update(drone.get_position_data())
        
        
        lg.update([droneManager.getPrintData(0),droneManager.getPrintData(1)])
    
        
        # drone.hover(.01)
        # print(drone.r2_pressed())
    drone.land()
    drone.close()

except Exception as e:
    traceback.print_exc()
    drone.land()
    drone.close()

