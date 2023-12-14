from codrone_edu.drone import *
from simple_pid import PID


class DroneHandler():
    
    def __init__(self,drone: Drone) -> None:
        self.drone = drone
        self.curPos = (0,0,0) # x,y,z
        self.curRot = (0,0,0) # yaw, pitch, roll
        self.curTarget = (0,0,0) # x,y,z
        
        pitchPidData = (10,0,0) # Kp, Ki, Kd
        zPidData = (100,30,0)
        rollPidData = (10,0,0)

        self.xPid = PID(rollPidData[0],rollPidData[1],rollPidData[2], setpoint=0)
        self.yPid = PID(pitchPidData[0], pitchPidData[1], pitchPidData[2], setpoint=0)
        self.zPid = PID(zPidData[0],zPidData[1],zPidData[2], setpoint=0) 

        
        
        
        self.pidList = [self.zPid,self.yPid,self.xPid]
        
        

    def move(self,relPos):
        
        self.curTarget = relPos
        
        for i,pid in enumerate(self.pidList):
            pid.setpoint = relPos[i]
        
        
        self.drone.set_pitch(self.yPid(self.curPos[1]))
        self.drone.set_roll (self.xPid(self.curPos[0]))
        self.drone.set_throttle(20)
        
        self.drone.move()
        
        
    def update(self, data  = None):
        posData = data if data != None else self.drone.get_position_data()
        self.curPos = (posData[1],posData[2],posData[3])
        self.curRot = self.drone.get_position_data()
    
    def getPrintData(self,pV):
        
        # print(  f"pidTing: {self.pidList[pV](self.curPos[pV])} currPos: {self.curPos[pV]}  ")
        return (self.pidList[pV].setpoint,self.curPos[pV],self.pidList[pV](self.curPos[pV]))
    

    def getCurPos(self):
        return self.curPos  