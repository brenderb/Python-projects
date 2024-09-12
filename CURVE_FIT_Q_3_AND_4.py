import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

c = np.loadtxt('rocket.csv', delimiter=",")
#print(c[0]) # [row], [column]

time = []
pos = []
sigma = []

for i in range(0, 24):
    time.append(c[i][0])
    
for i in range(0, 24):
    pos.append(c[i][1])
    
for i in range(0, 24):
    sigma.append(c[i][2])
    
time = np.array(time)
pos = np.array(pos)
sigma = np.array(sigma)

top_summation = []
bot_summation = []
avg_time = sum(time)/len(time)
avg_pos = sum(pos)/len(pos)

for i in range(0, len(time)):
    top_summation.append((time[i] - avg_time)*(pos[i]-avg_pos))
    bot_summation.append((time[i] - avg_time)**2)
    
u = sum(top_summation)/sum(bot_summation)
d0 = avg_pos - u*avg_time
print('The best estimate for u is ' + str(u) + ' (m/s).')
print('The best estimate for d0 is ' + str(d0) + ' (m).')
def model(t):
    return d0 + u*t

plt.grid()
plt.errorbar(time, pos, yerr=sigma, label='raw data')
plt.plot(time, model(time), label='prediction')
plt.suptitle("Linear Regression plotted along rocket's position versus time")
plt.xlabel('Time (hours)')
plt.ylabel('Position (kilometres)')
plt.legend()
plt.show()