import numpy as np
import matplotlib as plt

# Using measured data
x = np.loadtxt("two_terminal_devices.csv", usecols=4, delimiter=",")  # V
y1 = np.loadtxt("two_terminal_devices.csv", usecols=0, delimiter=",")  # mV
y2 = np.loadtxt("two_terminal_devices.csv", usecols=1, delimiter=",")  # mV
y = (y1 + y2) / 2
y = y / 1000  # V
R2 = 4.7
V_dev = x - y
I = y / R2
R = V_dev / I
print(R)

# Using figure
x = -2.925
y = -287.5  # mV
y = y / 1000
V_dev = x - y
I = y / R2
R = V_dev / I
print(R)
