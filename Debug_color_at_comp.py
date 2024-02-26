from codrone_edu.drone import *
from DroneManager import DroneHandler
import traceback
from LiveGraph import LiveGraph
from FakeDrone import FakeDrone
import numpy as np
from Course import *


# plotData = [grain,dataAmount,dataNames,overAllName,colors]

# lg = LiveGraph(([10,3,["input","Pos","pidOut"],"xPid",["r","b","g"]],
#                 [10,3,["input","Pos","pidOut"],"yPid",["k","g","y"]],
#                 [10,3,["input","Pos","pidOut"],"zPid",["y","m","violet"]]))
# lg.interactiveMode()

drone = Drone()
droneManager = DroneHandler(drone)
print("--Innit Complete--")

try:
    drone.open()
    # drone.reset_sensor()7
    drone.set_drone_LED(255,255,255,100) # makes white
    time.sleep(1)
    innit_color = droneManager.get_pad_color()
    
    # drone.takeoff()
    
    # while True and not drone.r2_pressed():
    #     # droneManager.move([0,0,.5])
    #     testPoints = [2.7232189178466797, inchtoM(68)]
        
    #     if droneManager.sequential_movement([
    #         (Y_KEYHOLE_XY[0] - inchtoM(4),0,Y_KEYHOLE_BASE_HEIGHT + (KEYHOLE_DIAMATER/2)), # moves infront of yellow keyhole
    #         (G_KEYHOLE_XY[0] ,-inchtoM(1),Y_KEYHOLE_BASE_HEIGHT + (KEYHOLE_DIAMATER/2)),
    #         (G_KEYHOLE_XY[0] ,-inchtoM(1),(G_KEYHOLE_BASE_HEIGHT + KEYHOLE_DIAMATER/2)), #goes throught the yellow keyhole and infront of green keyhole
    #         (G_KEYHOLE_XY[0] ,inchtoM(-1),(G_KEYHOLE_BASE_HEIGHT + KEYHOLE_DIAMATER/2)),
    #         (G_KEYHOLE_XY[0] ,inchtoM(12*3),(G_KEYHOLE_BASE_HEIGHT + KEYHOLE_DIAMATER/2)),
    #         (LANDING_PAD[0], testPoints[1],inchtoM(3*12)), # goes though the green keyhole and gets ready to land
    #     ]) == True:
    #         break 
    #     else:
    #         continue
    
    print("sleep")
    time.sleep(5)
        
    for x in range(10):
        time.sleep(.1)
        color = droneManager.get_pad_color()
        
        red_num = 0
        green_num = 0
        blue_num = 0
        
        
        if color == "Red":
            red_num += 1
        elif color == "Green":
            green_num += 1
        elif color == "Blue":
            blue_num += 1
            
        if red_num > green_num and red_num > blue_num:
            drone.set_drone_LED(255,0,0,100)
        elif green_num > red_num and green_num > blue_num: 
            drone.set_drone_LED(0,255,0,100)
        elif blue_num > red_num and blue_num > green_num:
            drone.set_drone_LED(0,0,255,100)
        
    

    
    if color == innit_color: 
        RED = [255,0,0]
        GREEN = [0,255,0]
        BLUE = [0,0,255]
        
        colors = [
        "Red",
        "Green",
        "Blue"
        ]
        
        colors.remove[colors.index(color)]
        rand_color = colors[np.random.randint(0,1)]
        
        
        if rand_color == "Red":
            drone.set_drone_LED(*RED,100)
        elif rand_color == "Green":
            drone.set_drone_LED(*GREEN,100)
        elif rand_color == "Blue":
            drone.set_drone_LED(*BLUE,100)
    
    
    time.sleep(7)
    drone.set_controller_LED(225,225,225,100)
    print("close")

    # drone.land()
    drone.close()

except Exception as e:
    traceback.print_exc()
    # drone.land()
    drone.close()

