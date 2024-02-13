# Drone using dependancy injection to test code.
import time


class FakeDrone:
    
    
    def __init__(self) -> None:
        self.pos = [0,0,0]
        self.throttle=0
        self.pitch =0 
        self.roll = 0
        self.startTime = time.time()

    def pair(self):
        # doesnt do anything because we are faking it
        pass
    
    def takeoff(self):
        # doesnt do anything because we are faking it
        pass
    
    def land(self):
        # doesnt do anything because we are faking it
        pass
    
    
    def r2_pressed(self):
        return False
    
    def close(self):
        # doesnt do anything because we are faking it
        pass
    
    def get_position_data(self):
        return [self.startTime - time.time()] + self.pos
    
    def set_throttle(self,throttle):
        self.throttle = (max(min(throttle,100),0)-25)*.2
    
    def set_pitch(self,pitch):
        self.pitch = (max(min(pitch,100),-100)-25)*.2
        
    def set_roll(self,roll):
        self.roll = (max(min(roll,100),-100)-25) *.2 
        
    
    
    def move(self):
        self.pos[0] += self.roll
        self.pos[1] += self.pitch
        self.pos[2] += self.throttle
        print(self.pos)
        
    
    
    
    
