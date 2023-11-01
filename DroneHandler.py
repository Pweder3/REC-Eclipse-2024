from codrone_edu.drone import *
from simple_pid import PID


class DroneHandler():
    
    def __init__(self,drone) -> None:
        self.drone = drone
        self.curPos = (0,0,0) # x,y,z
        self.curRot = (0,0,0) # yaw, pitch, roll
        self.curTarget = (0,0,0) # x,y,z
        
        pitchPidData = (0,0,0) # Kp, Ki, Kd
        zPidData = (0,0,0)
        rollPidData = (0,0,0)

        self.xPid = PID(rollPidData[0],rollPidData[1],rollPidData[2], setpoint=0)
        self.yPid = PID(pitchPidData[0], pitchPidData[1], pitchPidData[2], setpoint=0)
        self.zPid = PID(zPidData[0],zPidData[1],zPidData[2], setpoint=0)  
        
        self.pidList = [self.zPid,self.yPid,self.xPid]
        

    def move(self,relPos):
        
        self.curTarget = relPos
        
        self.drone.set_pitch(self.yPid(relPos[1]))
        self.drone.set_roll (self.xPid(relPos[0]))
        self.drone.set_throttle(self.zPid(relPos[2]))
        self.drone.move(.01)
        
        
    def update(self):
        posData = self.drone.get_position_data()
        self.curPos = (posData[1],posData[2],posData[3])
        self.curRot = self.drone.get_gyro_data()
    
    