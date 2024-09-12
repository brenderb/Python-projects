import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

c = np.loadtxt('rocket.csv', delimiter=",")

time = []
pos = []
sigma = []

for i in range(0, 24):
    time.append(c[i][0])
    sigma.append(c[i][2])
    pos.append(c[i][1])
    
time = np.array(time)
pos = np.array(pos)
sigma = np.array(sigma)

mean_list = []
for i in range(0, 23):
    mean_list.append(pos[i+1] - pos[i])

avg_speed = sum(mean_list)/len(mean_list)

std = np.std(mean_list)
print('The speed of the ship is ' + str(avg_speed) + ' (m/s) with standard deviation ' + str(std) + ' (m/s).')