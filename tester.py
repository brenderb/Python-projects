import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

pump_speeds = [350,300,180,150]
delays = [5.3,6.3,9.4,11.2]
delays_sigma = [0.3,0.4,0.3,.4]
taus = [3.1,3.9,7.4,8.6]
taus_sigma=[.1,.4,.1,.7]
FAKET = np.linspace(150,350,1000)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

lns1 = ax1.errorbar(pump_speeds, delays, delays_sigma, color='red',linestyle='None',capsize=3, fmt = 'o', markersize=3, label='Delay')
lns2 = ax2.errorbar(pump_speeds, taus, taus_sigma, color='blue',linestyle='None',capsize=3, fmt = 'o', markersize=3, label='Dispersion')
plt.xticks([150,180,300,350],['150','180','300','350'])
ax1.grid()

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, fontsize=15)

plt.xlabel('Pump speed (mL/h)',fontsize=15)
ax1.set_xlabel('Pump speed (mL/h)',fontsize=15)
ax1.set_ylabel('Delay constants (s)',fontsize=15)
ax2.set_ylabel('Dispersion constants (s)',fontsize=15)
ax2.set_ylim([2,9])

def quad(x, a, b, xshift, yshift):
    return a*(x+xshift)**2 + b*(x+xshift) + yshift

def exp(x, a, b, xshift, yshift):
    return a*np.exp(b*(x+xshift)) + yshift

params1, diags1 = curve_fit(exp,pump_speeds,delays,p0=[24.631,-0.004,0,0])
params2, diags2 = curve_fit(exp,pump_speeds,taus,p0=[12.661,-0.004,0,0])

plt.suptitle('Measured delay and dispersion constants - PET/CT ABSS - F18 Blood Analog',fontsize=15)
ax1.plot(FAKET, exp(FAKET, params1[0], params1[1], params1[2], params1[3]), color='red', linestyle='--', linewidth=.7)
ax2.plot(FAKET, exp(FAKET, params2[0], params2[1], params2[2], params2[3]), color='blue', linestyle='--', linewidth=.7)
plt.show()