import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

c = np.loadtxt('feather.csv', delimiter=",")

time=[]
pos=[]
sigma=[]

for i in range(0, len(c)):
    time.append(c[i][0])
    sigma.append(c[i][2])
    pos.append(c[i][1])
    
time = np.array(time)
pos = np.array(pos)
yerrors = np.array(sigma)

def positionvstime(time, s0, u, a):
    return s0 + u*time + .5*a*(time**2)

first_guess_params = [1.75, 0, -9.8/7]
popt, pcov = curve_fit(positionvstime, time, pos, sigma=yerrors, absolute_sigma=True, p0=first_guess_params)
ptsd = np.sqrt(np.diag(pcov))

print('s0 = ' + str(popt[0]) + ' (m) with standard deviation ' + str(ptsd[0]) + ' (m).')
print('u = ' + str(popt[1]) + ' (m/s) with standard deviation ' + str(ptsd[1]) + ' (m/s).')
print('a = ' + str(popt[2]) + ' (m/s^2) with standard deviation ' + str(ptsd[2]) + ' (m/s^2).')

plt.errorbar(time, pos, yerrors, label='raw data')
plt.plot(time, positionvstime(time, popt[0], popt[1], popt[2]))
plt.grid()
plt.suptitle("Position of feather dropped on the moon: raw data and model")
plt.xlabel('Time (hours)')
plt.ylabel('Position (kilometres)')
plt.show()