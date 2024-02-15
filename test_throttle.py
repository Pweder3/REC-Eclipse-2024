#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()
drone.takeoff()
# Drone goes up for 1 second with 50 power
drone.set_roll(-50)

for i in range(100):
    drone.move(0.01)
    print(f"{drone.get_position_data()[1]:.2f}")


drone.land()
drone.close()