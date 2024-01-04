from codrone_edu.drone import *
from simple_pid import PID


class DroneHandler():
    
    def __init__(self,drone: Drone) -> None:
        self.drone = drone
        self.curPos = (0,0,0) # x,y,z
        self.curRot = (0,0,0) # yaw, pitch, roll
        self.curTarget = (0,0,0) # x,y,z
        
        pitchPidData = (10,0,0) # Kp, Ki, Kd
        zPidData = (20,0,0)
        rollPidData = (10,0,0)

        self.xPid = PID(rollPidData[0],rollPidData[1],rollPidData[2], setpoint=0)
        self.yPid = PID(pitchPidData[0], pitchPidData[1], pitchPidData[2], setpoint=0)
        self.zPid = PID(Kp= zPidData[0], Ki=zPidData[1], Kd=zPidData[2], setpoint=0) 

        
        
        
        self.pidList = [self.xPid,self.yPid,self.zPid]
        
        

    def move(self,relPos):
        
        self.curTarget = relPos
        
        for i,pid in enumerate(self.pidList):
            pid.setpoint = relPos[i]
        
        
        self.drone.set_pitch(self.yPid(self.curPos[1]))
        self.drone.set_roll (self.xPid(self.curPos[0]))
        
        zValue = self.zPid(self.curPos[2]) 
        print(f"zval: {zValue}  curPos:{self.curPos[2]} error: {self.curTarget[2] -self.curPos[2] } target: {self.curTarget} zpid: {self.zPid(.5)}"  )
        self.drone.set_throttle(zValue)
        
        self.drone.move()
        
        
    def update(self, data  = None):
        posData = data if data != None else self.drone.get_position_data()
        self.curPos = (posData[1],posData[2],posData[3])
        self.curRot = self.drone.get_position_data()
    
    def getPrintData(self,pV):
        
        # print(  f"pidTing: {self.pidList[pV](self.curPos[pV])} currPos: {self.curPos[pV]}  ")
        return (self.pidList[pV].setpoint,self.curPos[pV],self.pidList[pV](self.curPos[pV]))
    
    def get_z_pos(self):
        return self.curPos[2]
    
    def getCurPos(self):
        return self.curPos  