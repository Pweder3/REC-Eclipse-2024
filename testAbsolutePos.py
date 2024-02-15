from codrone_edu.drone import *
from DroneManager import DroneHandler


drone = Drone()
drone.pair()
drone.takeoff()
print("--Innit Complete--")
drone.sendControlPosition(0,2,0,.2,0,0)
time.sleep(2)
drone.sendBuzzer(1,1,.1)