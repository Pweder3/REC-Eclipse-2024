from codrone_edu.drone import *
from DroneManager import DroneHandler
import traceback
from LiveGraph import LiveGraph
from FakeDrone import FakeDrone
import numpy as np
from Course import *


drone = Drone()

drone.open()
drone.set_drone_LED(255,255,255,100) # makes white
drone.close()