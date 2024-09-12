import numpy as np
import matplotlib.pyplot as plt

time_set = [0.001,1,1.5,3]
delay_set = [1,1,2,2]

plt.plot(time_set, delay_set,'black')
plt.plot([1,1.0001],[0,5],'--',c='red')
plt.plot([1.5,1.5001],[0,5],'--',c='red')
plt.grid()
plt.xlim([-0.2,3.2])
plt.ylim([0,3])
plt.xticks(np.array([0,1,1.5,3]), ['t_start','t1','t2','t_end'],fontsize=20)
plt.yticks(np.array([0,1,2]), ['0','δ_1','δ_2'],fontsize=20)
plt.xlabel('Time', fontsize=20)
plt.ylabel('Delay',fontsize=20)
plt.show()