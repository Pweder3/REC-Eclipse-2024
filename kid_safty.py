from codrone_edu.drone import *
from src.DroneManager import DroneHandler
import traceback
from src.LiveGraph import LiveGraph
from FakeDrone import FakeDrone
import numpy as np
from src.Course import *




drone = Drone()
drone.pair()


while True:
    i = input("enter to stop")
    for x in range(20):
        drone.emergency_stop()
    
