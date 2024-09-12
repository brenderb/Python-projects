import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0,60,1000)
delay=0

def aif(time, alpha, a, b):
    return alpha*(np.heaviside(time-a,0) - np.heaviside(time-b,0))

def realf(time,alpha,a,b,beta):
    return alpha*(np.heaviside(time-a,0)*(1 - (np.exp(-beta*(time-a)))) - np.heaviside(time-b,0)*(1 - (np.exp(-beta*(time-b)))))

A1 = 20
B1 = 40

plt.plot(time, realf(time, 50, A1+delay, B1+delay,1/5), 'blue', label='y(t)')
plt.grid()
plt.xlabel('Time', fontsize=20)
plt.ylabel('Activity concentration', fontsize=20)
plt.legend(fontsize=40)
plt.xticks([0,A1+delay,B1+delay],['0','a_o','b_o'], fontsize=20)
plt.yticks([0,50],['0','α'], fontsize=20)
plt.show()