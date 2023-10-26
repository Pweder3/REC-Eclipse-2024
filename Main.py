from codrone_edu.drone import *


try:
    drone = Drone()
    drone.pair()
    drone.takeoff()
    data = drone.get_position_data()
    
    drone.square(60,.5)
    drone.land()
    drone.close()


except Exception as e:
    print("An error occurred: ", e)
