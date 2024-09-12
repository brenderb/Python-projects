import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


L0 = 1.5 * 10**(-3)
C0 = 0.01 * 10**(-6)

uL = 0.1*L0
uC = 0.03*C0

vsqred = 1/(L0*C0)
v = np.sqrt(vsqred)

u = np.sqrt((uL**2)/(4*C0*(L0**3)) + (uC**2)/(4*L0*(C0**3)))

print('- the theoretical speed is ' + str(v) + ' +- ' + str(u))



#number of LC unit
num = np.loadtxt("cable_part_1.csv", delimiter = ",", usecols=0)
a = []
for i in range(0, len(num)):
    a.insert(0, num[i])
num = np.array(a)

#starting point of pulse from channel 1
c1 = np.loadtxt("cable_part_1.csv", delimiter = ",", usecols=1)

#starting point of pulse from channel 2. Taking average 
c21 = np.loadtxt("cable_part_1.csv", delimiter = ",", usecols=3)
c22 = np.loadtxt("cable_part_1.csv", delimiter = ",", usecols=4)

#reverse order
c211 = []
for i in range(0, len(c21)):
    c211.insert(0, c21[i])
c21 = np.array(c211)

c222 = []
for i in range(0, len(c22)):
    c222.insert(0, c22[i])
c22 = np.array(c222)

#c2
c2 = c21 * 0
for i in range(0, len(c21)):
    c2[i] = (c21[i]+c22[i])/2
    
    
#uncertainty of c2
uncert_c2 = []
for i in range (0, len(c2)):
    uncert_c2.append(
        max(c22[i]-c2[i], c2[i]-c21[i])
        )
uncert_c2 = np.array(uncert_c2)
    


def f(x, a, b):
    return a * x + b

popt, pcov = curve_fit(f, num, c2)
pstd = np.sqrt(np.diag(pcov))
curvefit = f(num, popt[0], popt[1])
print(f'- Curvefit slope is {popt[0]} +- {pstd[0]} microsecond / LC unit.')
slope_inverse = 1 / popt[0]
u_slope_inverse = np.sqrt(
    (-1/popt[0]**2)**2 * (pstd[0]**2)
    )
print(f'- so the speed should be 1 / slope = {slope_inverse} +- {u_slope_inverse} LC unit / microsecond .')
print(f'- which is {slope_inverse * 10**6} +- {u_slope_inverse * 10**6} LC unit / second.')


def chi_square(num_datapoints, num_parameters, measure_data, prediction, sigma):
    result = (1 / (num_datapoints - num_parameters)) * (np.sum(
        ((measure_data - prediction) ** 2) / (sigma ** 2)
        ))
    return result

chi = chi_square(len(c2), 2, c2, curvefit, uncert_c2)
print(f'- chi squared is {chi}.')

################### residuals
cf_unc = []
for i in range(0, len(num)):
    cf_unc.append( np.sqrt(  num[i]*num[i]*pstd[0]*pstd[0] + pstd[1]*pstd[1]   )   )

res_unc = []
for i in range(0,len (num)):
    res_unc.append(np.sqrt(uncert_c2[i]*uncert_c2[i] + cf_unc[i]*cf_unc[i]))



plt.figure(figsize = (8, 6))
plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)
plt.errorbar(num, c2, yerr = uncert_c2, ls = "none", marker = "o", markersize = 3,
             label="measured data")
plt.xlabel("unit distance", fontsize=30)
plt.ylabel("time delay (microseconds)", fontsize=25)
plt.plot(num, curvefit, label="curvefit result")
plt.grid()
plt.legend(fontsize=20)


plt.figure(figsize = (8, 6))
plt.errorbar(num, c2 - curvefit, yerr = res_unc, ls = "none", marker = "o", markersize = 3,
             label="residual of measured data - expected curve fit", color='black')
plt.plot(num, num*0, label='zero line',color='red')
plt.xlabel("unit distance", fontsize=30)
plt.ylabel("residual of time delay (microseconds)", fontsize=18)
plt.grid()
plt.legend(fontsize=15)

plt.show()






