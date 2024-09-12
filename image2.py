import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0,100,1000)
delay=40

def aif(time, alpha, a, b):
    return alpha*(np.heaviside(time-a,0) - np.heaviside(time-b,0))

def realf(time,alpha,a,b,beta):
    return alpha*(np.heaviside(time-a,0)*(1 - (np.exp(-beta*(time-a)))) - np.heaviside(time-b,0)*(1 - (np.exp(-beta*(time-b)))))

plt.plot(time, aif(time, 50, 10, 30), 'red',label='x(t)')
plt.plot(time, realf(time, 50, 10+delay, 30+delay,1/5), 'blue', label='y(t)')
plt.grid()
plt.xlabel('Time', fontsize=20)
plt.ylabel('Activity concentration', fontsize=20)
plt.legend(fontsize=40)
plt.xticks([0,10,30,50,70],['0','a_i','b_i','a_o','b_o'], fontsize=20)
plt.yticks([0,50],['0','α'], fontsize=20)
plt.show()