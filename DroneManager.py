from codrone_edu.drone import *
from simple_pid import PID
import numpy as np
import time


class DroneHandler():
    
    def __init__(self,drone) -> None:
        self.drone = drone
        self.curPos = [0,0,0] # x,y,z
        # self.curRot = (0,0,0) # yaw, pitch, roll
        self.curTarget = [0,0,0] # x,y,z
        
        pitch_pid_data = (70, 2, 0) # Kp, Ki, Kd
        throttle_pid_data = (140, 10, 0)
        roll_pid_data = (70, 2, 0)

        self.roll_pid = PID(roll_pid_data[0],roll_pid_data[1],roll_pid_data[2], setpoint=0, output_limits=(-100,100))
        self.pitch_pid = PID(pitch_pid_data[0], pitch_pid_data[1], pitch_pid_data[2], setpoint=0, output_limits=(-100,100))
        self.throttle_pid = PID(Kp= throttle_pid_data[0], Ki=throttle_pid_data[1], Kd=throttle_pid_data[2], setpoint=0, output_limits=(-100,100) )

        self.start_time = time.time()
        
        
        
        self.pidList = [self.pitch_pid,self.roll_pid,self.throttle_pid]
        
        

    def move(self,relPos):
        
        self.curTarget = relPos
        
        for i,pid in enumerate(self.pidList):
            pid.setpoint = relPos[i]
            
        
        
        # self.drone.set_pitch(self.pitch_pid(self.curPos[0]))
        # self.drone.set_roll(-self.roll_pid(self.curPos[1]))
        self.drone.set_throttle(self.throttle_pid(self.curPos[2]))
        
        self.drone.move()
        
        self.update()
        
        
    def update(self, data  = None):
        posData = data if data != None else self.drone.get_position_data()
    
        
        self.curPos = (posData[1],posData[2],posData[3])
        self.curRot = self.drone.get_position_data() 
        return self.curPos
        # print(f"x: {self.curPos[0]:.2f} y: {self.curPos[1]:.2f} z: {self.curPos[2]:.2f}")
        
    def sequential_movement(self,seq:list[tuple]):
        print("--ENTERED SEQUENTIAL MOVEMENT--")
        for i,movement in enumerate(seq):
            while np.average(np.subtract(self.curPos, movement)) > 0.1 and not self.drone.r2_pressed(): # while the drone is within the target with 10% error.
                print(f"movement: {i} looking for: {movement} ")
                self.move(movement)
                
                
    def flashColor(self,color = None):
        if color == None:
            color = map(lambda x: x*255, np.random.rand(3))
        self.drone.set_drone_LED(color)

    
    
    def get_display_Data(self,pV,minIndex =0,maxIndex = 2):
        return (self.pidList[pV].setpoint*10,self.curPos[pV] *10,self.pidList[pV](self.curPos[pV]))[minIndex:maxIndex]
        # converted to cm for better readability
    
    def get_z_pos(self):
        return self.curPos[2]
    
    def getCurPos(self):
        return self.curPos  
    
    def get_latest_time(self):
        return time.time() - self.start_time