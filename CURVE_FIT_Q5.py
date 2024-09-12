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
    sigma.append(c[i][2])
    pos.append(c[i][1])

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

print('The best guess for the speed is ' + str(u))
print('The best guess for the initial distance is ' + str(d0))

def model(t):
    return d0 + u*t

def chisquared(t, y_data, fxn, sigma_data, N, m):
    summation = []
    for i in range(len(y_data)):
        summation.append((((y_data[i] - fxn(time[i]))**2))/(sigma_data[i])**2)
    return (1/(N-m))*sum(summation)

chisq = chisquared(time, pos, model, sigma, len(pos), 2)
print('The value of chi squared is '+ str(chisq))