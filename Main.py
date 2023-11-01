from codrone_edu.drone import *
from DroneHandler import DroneHandler
import traceback
    
droneManager = DroneHandler(Drone())


try:
    drone = Drone()
    drone.pair()
    drone.takeoff()
    while  not drone.r2_pressed():
        droneManager.move((0,0,0))
        droneManager.update()
        
        # drone.hover(.01)
        # print(drone.r2_pressed())
    drone.land()
    drone.close()

except Exception as e:
    traceback.print_exc()
    drone.land()
    drone.close()

