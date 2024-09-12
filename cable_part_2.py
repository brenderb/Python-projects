import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

epsilon_vacuum = 8.8541878128 * 10 ** (-12)
mu_vacuum = 4 * np.pi * 10 ** (-7)

epsilon_cable = 2.25 * epsilon_vacuum
mu_cable = mu_vacuum

v = np.sqrt(1 / (epsilon_cable * mu_cable))
print(f'- theoretical speed is {v} m/s.')


c1 = np.loadtxt("cable_part_2.csv", delimiter = ",", usecols=0)
uc1 = np.loadtxt("cable_part_2.csv", delimiter = ",", usecols=1)
c2 = np.loadtxt("cable_part_2.csv", delimiter = ",", usecols=2)
uc2 = np.loadtxt("cable_part_2.csv", delimiter = ",", usecols=3)
diff = c2 - c1
udiff = np.sqrt(uc1**2 + uc2**2)

l = np.loadtxt("cable_part_2.csv", delimiter = ",", usecols=4)
ul = np.loadtxt("cable_part_2.csv", delimiter = ",", usecols=5)

def f(x, a, b):
    return a * x + b

popt, pcov = curve_fit(f, l, diff, sigma = udiff)
pstd = np.sqrt(np.diag(pcov))
curvefit = f(l, popt[0], popt[1])
print(f'- Curvefit slope is {popt[0]} +- {pstd[0]} nanosecond / m.')

slope_inverse = 1 / popt[0]
u_slope_inverse = np.sqrt(
    (-1/popt[0]**2)**2 * (pstd[0]**2)
    )

speed = slope_inverse * 10**9
uspeed = u_slope_inverse * 10**9
print(f'- so the speed should be 1 / slope = {slope_inverse} +- {u_slope_inverse} m / nanosecond .')
print(f'- which is {speed} +- {uspeed} m / second.')



def chi_square(num_datapoints, num_parameters, measure_data, prediction, sigma):
    result = (1 / (num_datapoints - num_parameters)) * (np.sum(
        ((measure_data - prediction) ** 2) / (sigma ** 2)
        ))
    return result

chi = chi_square(len(diff), 2, diff, curvefit, udiff)
print(f'- chi squared is {chi}.')


#attenuation
V_r = np.loadtxt("cable_part_2.csv", delimiter = ",", usecols=6)
uV_r = np.loadtxt("cable_part_2.csv", delimiter = ",", usecols=7)
V_i = np.loadtxt("cable_part_2.csv", delimiter = ",", usecols=8)
uV_i = np.loadtxt("cable_part_2.csv", delimiter = ",", usecols=9)

atten = []
for i in range(0, len(V_r)):
    atten.append(10 * (np.log10(V_r[i] / V_i[i])**2))

uatten = []
for i in range(0, len(atten)):
    dattendV_r = 20 * (np.log10(V_r[i] / V_i[i])) * (1 / (V_r[i] * np.log(10)))
    dattendV_i = 20 * (np.log10(V_r[i] / V_i[i])) * (-1 / (V_i[i] * np.log(10)))
    inside_sqrt = dattendV_r**2 * uV_r[i]**2 +  dattendV_i**2 * uV_i[i]**2
    uatten.append(np.sqrt(inside_sqrt))
    
atten = np.array(atten)
uatten = np.array(uatten)

popt2, pcov2 = curve_fit(f, l, atten, sigma = uatten)
pstd2 = np.sqrt(np.diag(pcov2))
curvefit2 = f(l, popt2[0], popt2[1])

print(f' \n'
      f'- Curvefit attenuation per meter is {popt2[0]} +- {pstd2[0]} dB / m.')

chi = chi_square(len(l), 2, atten, curvefit2, uatten)
print(f'- chi squared is {chi}.')

###########################################################################################

time_curvefit_unc = []
time_res_unc = []

for i in range(0, len(l)):
    time_curvefit_unc.append(np.sqrt(l[i]*l[i]*pstd[0]*pstd[0] + pstd[1]*pstd[1]))

for i in range(0, len(l)):
    time_res_unc.append(np.sqrt(time_curvefit_unc[i]**2 + udiff[i]**2))

att_curvefit_unc = []
att_res_unc = []

for i in range(0, len(l)):
    att_curvefit_unc.append(np.sqrt(l[i]*l[i]*pstd2[0]*pstd2[0] + pstd2[1]*pstd2[1]))

for i in range(0, len(l)):
    att_res_unc.append(np.sqrt(att_curvefit_unc[i]**2 + uatten[i]**2))


###########################################################################################
#impedance
R1 = 0.0004445
R2 = 0.0014732
L0 = (mu_cable / (2*np.pi)) * np.log(R2 / R1)
Z0 = speed * L0
uZ0 = Z0 * (uspeed/speed)
print(f' \n'
      f"- Impedance of the cable is {Z0} +- {uZ0} Ohms. ")




###########################################################################################

plt.figure(figsize = (8, 6))
plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)
plt.errorbar(l, diff, xerr=ul, yerr=udiff, ls = "none", marker = "o", markersize = 3,
             label="measured data")
plt.xlabel("cable length (m)", fontsize=27)
plt.ylabel("time delay (nanosecond)", fontsize=27)
plt.plot(l, curvefit, label="curvefit result")
plt.grid()
plt.legend(fontsize=20)

plt.figure(figsize = (8, 6))
plt.errorbar(l, atten, xerr=ul, yerr=uatten, ls = "none", marker = "o", markersize = 3,
             label="measured data")
plt.plot(l, curvefit2, label="curvefit result")
plt.xlabel("cable length (m)", fontsize=30)
plt.ylabel("attenuation (dB)", fontsize=30)
plt.grid()
plt.legend(fontsize=20)


plt.figure(figsize = (8, 6))
plt.errorbar(l, diff - curvefit, yerr=time_res_unc, ls = "none", marker = "o", markersize = 3,
             label="residual of measured data - curve fit result", color='black')
plt.plot(l, l*0, label='zero line', color='red')
plt.xlabel("cable length (m)", fontsize=30)
plt.ylabel("residual of time delay (nanosecond)", fontsize=18)
plt.grid()
plt.legend(fontsize=15)

plt.figure(figsize = (8, 6))
plt.errorbar(l, atten - curvefit2, yerr=att_res_unc, ls = "none", marker = "o", markersize = 3,label="residual of measured data - curve fit result", color='black')
plt.plot(l, l*0, label='zero line', color='red')
plt.xlabel("cable length (m)", fontsize=30)
plt.ylabel("residual of attenuation (dB)", fontsize=24)
plt.grid()
plt.legend(fontsize=15)


plt.show()





