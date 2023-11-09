import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import math
class Plot():
    
    def __init__(self,fig,ax,grain,dataAmount,dataNames,names,colors ) -> None:
        
        

        self.fig = fig
        self.ax = ax
        self.grain = grain
        
        
        self.names = names
        self.color = colors
        
        self.xData = range(grain)
        
        self.yData = []
        self.Lines = []
        
        
        for i in range(dataAmount):
            self.yData.append([0] * grain ) 
            
            ln, = self.ax.plot(self.xData,self.yData[i] , animated=False,label=dataNames[i], color=colors[i])
            
            self.Lines.append(ln)            
        
    
        
        
        
        
        self.fig.canvas.draw()
        self.fig.show()
        
        self.bg = fig.canvas.copy_from_bbox(self.ax.bbox)
        self.fig.canvas.blit(self.ax.bbox)
        self.ax.legend()
        
            
    def restore(self):
        self.fig.canvas.restore_region(self.bg)
    
    def setYData(self,y): # for loop could be made more readable 
        for i,yVal in enumerate(y):
            self.yData[i].append(yVal) 
            self.yData[i].pop(0) 
            
            self.Lines[i].set_ydata(self.yData[i]) # every line has its own yData
        
        
    def draw_artist(self):
        
        
        # maxVal = max([max(y) for y in self.yData ])
        # minVal = min([min(y) for y in self.yData ])
        maxVal = 5
        minVal = -5
            
        for line in self.Lines:
            self.ax.draw_artist(line)
            self.ax.axis([0,self.grain,minVal,maxVal])
            
        self.ax.set_title(self.names)
        self.ax.legend()
        
        
    def blit(self):
        self.fig.canvas.blit(self.fig.bbox)
        
    