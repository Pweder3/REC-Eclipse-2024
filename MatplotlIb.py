import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from codrone_edu.drone import *
from DroneHandler import DroneHandler
import traceback
    
droneManager = DroneHandler(Drone())


plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

x,y = [],[]

def animate(i):

    x.append(i)
    y1.append()
    y2

    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()


try:

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()