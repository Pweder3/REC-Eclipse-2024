import time
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import math
import numpy as np
from plot import Plot

class LiveGraph():
    
    
    def __init__(self,plotdata) -> None:
        
        
        # plotData = [grain,dataAmount,dataNames,overAllName,colors]
        
        self.fig = plt.figure(figsize=(10,10))
        
        self.plots = []
        for i in range(len(plotdata)):
            self.plots.append(Plot(
                                   self.fig,
                                   self.fig.add_subplot(len(plotdata),1,i+1),
                                   plotdata[i][0],
                                   plotdata[i][1],
                                   plotdata[i][2],
                                   plotdata[i][3],
                                   plotdata[i][4]
                                   ))
        
        
        
        self.tick = 0
        plt.show(block = False)
        plt.pause(0.1)  
        
    def interactiveMode(self):
        plt.ion() 
        
    def update(self,y,plotInSequence = True):
        
        self.tick += 1
        if plotInSequence:
            [plot.restore() for plot in self.plots]
            [plot.setYData(y[i]) for i, plot in enumerate(self.plots)]
            [plot.draw_artist() for plot in self.plots]
            [plot.blit() for plot in self.plots]
        else:
            for i,plot in enumerate(self.plots):
                plot.restore()
                plot.setYData(y[i])
                plot.draw_artist()
                plot.blit()
        self.fig.canvas.flush_events() 
        

    
            
        
            
        
if __name__ == "__main__":
    LG = LiveGraph(([50,2,['a','b'],'fig1',["r","b"]],[50,2,['c','d'],'fig2',["r","b"]]))
    LG.interactiveMode()

    for j in range(1000):
        LG.update([[1,math.sin(j/100)],
                   [math.cos(j/100),math.sin(j/100)]])
        

            
        
    
    