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

plt.grid()
plt.errorbar(time, pos, yerr=sigma)
plt.suptitle('Position versus time of the rocket.')
plt.xlabel('Time (hours)')
plt.ylabel('Position (kilometres)')
plt.savefig('rocket_positiontime')    
plt.show()