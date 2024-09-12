import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

grav_acce = 9.804253


def chi_square(num_datapoints, num_parameters, measure_data, prediction, sigma):
    result = (1 / (num_datapoints - num_parameters)) * (np.sum(
        ((measure_data - prediction) ** 2) / (sigma ** 2)
        ))
    return result



floor_num = np.loadtxt("radius_of_the_earth.csv", delimiter = ",", usecols=0)
g = np.loadtxt("radius_of_the_earth.csv", delimiter = ",", usecols=1)
ug = np.loadtxt("radius_of_the_earth.csv", delimiter = ",", usecols=2)

g = g * 0.10055 #milligals
g = g * 10**(-5) #m/s^2
g = np.delete(g, 0) #pop basement
g = np.delete(g, 0) #pop first floor
g = np.delete(g, 0) #pop second floor
g = np.delete(g, 11)  #pop 14 floor

ug = ug * 0.10055 #milligals
ug = ug * 10**(-5) #m/s^2
ug = np.delete(ug, 0) #pop basement
ug = np.delete(ug, 0) #pop first floor
ug = np.delete(ug, 0) #pop second floor
ug = np.delete(ug, 11)  #pop 14 floor


dg = []
for i in range(0, len(g)):
    dg.append(g[i] - g[0])
dg = np.array(dg)

udg = []
for i in range(0, len(ug)):
    udg.append(np.sqrt(ug[i]**2 + ug[0]**2))
udg = np.array(udg)

dr = floor_num * 3.95
dr = np.delete(dr, 0) #pop basement
dr = np.delete(dr, 0) #pop first floor
dr = np.delete(dr, 0) #pop second floor
dr = np.delete(dr, 11) #pop 14 floor

def f(x, a, b):
    return a * x + b

popt, pcov = curve_fit(f, dr, dg, sigma=udg)
pstd = np.sqrt(np.diag(pcov))
curvefit = f(dr, popt[0], popt[1])
print(f'- Curvefit slope is {popt[0]} +- {pstd[0]}.')


R = -2*grav_acce / popt[0]
uR = R * np.sqrt((pstd[0] / popt[0])**2)
print(f'- slope is -2g/R, so R = {R} +- {uR} m .')

chi = chi_square(len(dg), 2, dg, curvefit, udg)
print(f'- chi squared is {chi}.')


#############################################################################
#grav force of floor
G = 6.67430*10**(-11)
M = 10**6

def grav_force(r, m):
    return G * m / r**2

addition_g = []
for i in range(4, 13):
    above_center = ((13 - i) / 2) * 3.95
    below_center = ((i - 3) / 2) * 3.95
    addition_g.append(-grav_force(above_center, M*(13-i)) + grav_force(below_center, M*(i-3)))

addition_g.insert(0, -grav_force(5 * 3.95, 10*M))
addition_g.append(grav_force(5 * 3.95, 10*M))
addtion_g = np.array(addition_g)

new_g = g + addition_g
new_dg = []
for i in range(0, len(new_g)):
    new_dg.append(new_g[i] - new_g[0])
new_dg = np.array(new_dg)


popt2, pcov2 = curve_fit(f, dr, new_dg, sigma=udg)
pstd2 = np.sqrt(np.diag(pcov2))
curvefit2 = f(dr, popt2[0], popt2[1])
print(f'- When considering grav force of floors, curvefit slope is {popt2[0]} +- {pstd2[0]}.')

new_R = -2*grav_acce / popt2[0]
new_uR = new_R * np.sqrt((pstd2[0] / popt2[0])**2)
print(f'- new slope is -2g/R, so new R = {new_R} +- {new_uR} m .')

chi2 = chi_square(len(new_dg), 2, new_dg, curvefit2, udg)
print(f'- chi squared is {chi2}.')


#############################################################################
#Residual
res = dg - curvefit

#1.uncertainty of curvefit
uax = popt[0]*dr * np.sqrt((pstd[0]/popt[0])**2)
ucurvefit = np.sqrt(uax**2 + pstd[1]**2)

#2.uncertainty of residual
ures = np.sqrt(udg**2 + ucurvefit**2)



res2 = new_dg - curvefit2

#1.uncertainty of curvefit
uax2 = popt2[0]*dr * np.sqrt((pstd2[0]/popt2[0])**2)
ucurvefit2 = np.sqrt(uax2**2 + pstd2[1]**2)

#2.uncertainty of residual
ures2 = np.sqrt(udg**2 + ucurvefit2**2)

#############################################################################
plt.figure(figsize=(8, 6))
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)
plt.errorbar(dr, dg, yerr=udg, ls="none", marker = "o", markersize=5, label="measured data", capsize=3)
plt.plot(dr, curvefit, label="best fit line")
plt.xlabel("delta R (m)", fontsize=17)
plt.ylabel("delta g (m/s^2)", fontsize=17)
plt.grid()
plt.legend(fontsize=17)


plt.figure(figsize=(8, 6))
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)
plt.errorbar(dr, new_dg, yerr=udg, ls="none", marker = "o", markersize=5, label="measured data (with grav force of floors)", capsize=3)
plt.plot(dr, curvefit2, label="best fit line with grav force of floors")
plt.xlabel("delta R (m)", fontsize=17)
plt.ylabel("delta g (m/s^2)", fontsize=17)
plt.grid()
plt.legend(fontsize=15)



plt.figure(figsize=(8, 6))
plt.errorbar(dr, res, yerr=ures, ls="none", marker = "o", markersize=5, label="Measured data - curvefit result", capsize=7)
plt.plot(dr, dr*0, label="Zero line")
plt.xlabel("delta R (m)", fontsize=17)
plt.ylabel("Residual", fontsize=17)
plt.legend(fontsize=12)
plt.grid()


plt.figure(figsize=(8, 6))
plt.errorbar(dr, res2, yerr=ures2, ls="none", marker = "o", markersize=5, label="Measured data - curvefit result (with grav force of floors)", capsize=7)
plt.plot(dr, dr*0, label="Zero line")
plt.xlabel("delta R (m)", fontsize=17)
plt.ylabel("Residual", fontsize=17)
plt.legend(fontsize=12)
plt.grid()


#############################################################################
plt.show()

    