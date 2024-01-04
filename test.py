from codrone_edu.drone import *
from DroneManager import DroneHandler
import traceback
from LiveGraph import LiveGraph


try:
    drone = Drone()
    drone.pair()
    drone.takeoff()
    while  not drone.r2_pressed():

        drone.set_throttle(100)
        drone.move()
         
        
        # drone.hover(.01)
        # print(drone.r2_pressed())
    drone.land()
    drone.close()

except Exception as e:
    traceback.print_exc()
    drone.land()
    drone.close()
