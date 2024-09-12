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
    pos.append(c[i][1])
    sigma.append(c[i][2])

time = np.array(time)
pos = np.array(pos)
yerrors = np.array(sigma)

def model_function(time, m, b):
    return m*time + b

first_guess_params = [4357, 5640]

popt, pcov = curve_fit(model_function, time, pos, sigma=yerrors, absolute_sigma=True, p0=first_guess_params)
ptsd = np.sqrt(np.diag(pcov))

net_std = np.sqrt(ptsd[0]**2 + ptsd[1]**2)

print('the best estimate for the speed is '+ str(popt[0]) + ' with standard deviation ' + str(ptsd[0]))
print('the best estimate for the starting position is '+ str(popt[1]) + ' with standard deviation ' + str(ptsd[1]))

def model(t):
    return popt[1] + popt[0]*t

def chisquared(t, y_data, fxn, sigma_data, N, m):
    summation = []
    for i in range(len(y_data)):
        summation.append((((y_data[i] - fxn(time[i]))**2))/(sigma_data[i])**2)
    return (1/(N-m))*sum(summation)

new_chi = chisquared(time, pos, model, yerrors, len(time), 2)

print('the new value for chi is ' + str(new_chi))

q5_speed = 4357.412595548586
q5_dist = 5640.244920890051

plt.errorbar(time, pos, yerrors, label='raw data')
plt.plot(time, time*q5_speed + q5_dist, label = 'linear regression model') #no std
plt.errorbar(time, time*popt[0] + popt[1], net_std, ls='--', label='curve_fit model with standard deviation')
plt.suptitle("Rocket position vs time: raw data, linear regression and curve_fit model.")
plt.xlabel('Time (hours)')
plt.ylabel('Position (kilometres)')
plt.grid()
plt.legend()
plt.show()
