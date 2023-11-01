from codrone_edu.drone import *
from DroneHandler import DroneHandler

droneManager = DroneHandler(Drone())

try:
    drone = Drone()
    drone.pair()
    drone.takeoff()
    droneManager.move((0,0,0))
    droneManager.update()
    drone.land()
    drone.close()


except Exception as e:
    print("An error occurred: ", e)
