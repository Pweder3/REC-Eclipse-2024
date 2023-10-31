from codrone_edu.drone import *
from simple_pid import PID


class DroneHandler():
    
    def __init__(self,drone) -> None:
        self.drone = drone
        self.curPos = (0,0,0) # x,y,z
        self.curRot = (0,0,0) # yaw, pitch, roll

        xPidData = (0,0,0) # Kp, Ki, Kd
        yPidData = (0,0,0)
        zPidData = (0,0,0)

        self.pidList = [PID(xPidData),PID(yPidData),PID(zPidData)]
        

    def move(relPos):
        pass
        
    def update(self):
        posData = self.drone.get_position_data()
        self.curPos = (posData[1],posData[2],posData[3])
        self.curRot = self.drone.get_gyro_data()
    
    