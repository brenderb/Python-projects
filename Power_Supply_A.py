import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

V_6_5 = np.loadtxt("Power_Supply_A.txt", delimiter = ",", usecols = 0) #V
I_6_5 = np.loadtxt("Power_Supply_A.txt", delimiter = ",", usecols = 1) #mA

V_10 = np.loadtxt("Power_Supply_A.txt", delimiter = ",", usecols = 2) #V
I_10 = np.loadtxt("Power_Supply_A.txt", delimiter = ",", usecols = 3) #mA

V_15 = np.loadtxt("Power_Supply_A.txt", delimiter = ",", usecols = 4) #V
I_15 = np.loadtxt("Power_Supply_A.txt", delimiter = ",", usecols = 5) #mA

V_20 = np.loadtxt("Power_Supply_A.txt", delimiter = ",", usecols = 6) #V
I_20 = np.loadtxt("Power_Supply_A.txt", delimiter = ",", usecols = 7) #mA

V_6_5_uncert = np.array([])
I_6_5_uncert = np.array([])
V_10_uncert = np.array([])
I_10_uncert = np.array([])
V_15_uncert = np.array([])
I_15_uncert = np.array([])
V_20_uncert = np.array([])
I_20_uncert = np.array([])

for i in range(0, len(V_6_5)):
    V_6_5_uncert = np.append(V_6_5_uncert, 0.005 + 0.0005 * V_6_5[i])
    V_10_uncert = np.append(V_10_uncert, 0.005 + 0.0005 * V_10[i])
    V_15_uncert = np.append(V_15_uncert, 0.002 + 0.0005 * V_15[i])
    V_20_uncert = np.append(V_20_uncert, 0.002 + 0.0005 * V_20[i])
    I_6_5_uncert = np.append(I_6_5_uncert, 0.005 + 0.002 * I_6_5[i])
    I_10_uncert = np.append(I_10_uncert, 0.005 + 0.002 * I_10[i])
    I_15_uncert = np.append(I_15_uncert, 0.005 + 0.002 * I_15[i])
    I_20_uncert = np.append(I_20_uncert, 0.005 + 0.002 * I_20[i])
    
    
    
def model(x, a, b):
    return a - b * x

def chi_square(num_datapoints, num_parameters, measure_data, prediction, sigma):
    result = (1 / (num_datapoints - num_parameters)) * (np.sum(
        ((measure_data - prediction) ** 2) / (sigma ** 2)
        ))
    return result


popt_6_5, pcov_6_5 = curve_fit(model, I_6_5, V_6_5, sigma = V_6_5_uncert, absolute_sigma = True)
pstd_6_5 = np.sqrt(np.diag(pcov_6_5))
curvefit_6_5 = model(I_6_5, popt_6_5[0], popt_6_5[1])
chi_6_5 = chi_square(6, 2, V_6_5, curvefit_6_5, V_6_5_uncert)
print(f'- Using curve_fit function for 6.5V, V = V_inf - R_int * I with: \n'
      f'  V_inf = {popt_6_5[0]} +- {pstd_6_5[0]} V \n'
      f'  R_int = {popt_6_5[1]*1000 } +- {pstd_6_5[1]*1000} Ohms')
print(f'  Reduced chi squared is {chi_6_5}.')

popt_10, pcov_10 = curve_fit(model, I_10, V_10, sigma = V_10_uncert, absolute_sigma = True)
pstd_10 = np.sqrt(np.diag(pcov_10))
curvefit_10 = model(I_10, popt_10[0], popt_10[1])
chi_10 = chi_square(6, 2, V_10, curvefit_10, V_10_uncert)
print(f'- Using curve_fit function for 10V, V = V_inf - R_int * I with: \n'
      f'  V_inf = {popt_10[0]} +- {pstd_10[0]} V \n'
      f'  R_int = {popt_10[1]*1000 } +- {pstd_10[1]*1000 } Ohms')
print(f'  Reduced chi squared is {chi_10}.')

popt_15, pcov_15 = curve_fit(model, I_15[:-1], V_15[:-1], sigma = V_15_uncert[:-1], absolute_sigma = True)
pstd_15 = np.sqrt(np.diag(pcov_15))
curvefit_15 = model(I_15, popt_15[0], popt_15[1])
chi_15 = chi_square(5, 2, V_15[:-1], curvefit_15[:-1], V_15_uncert[:-1])
print(f'- Using curve_fit function for 15V, V = V_inf - R_int * I with: \n'
      f'  V_inf = {popt_15[0]} +- {pstd_15[0]} V \n'
      f'  R_int = {popt_15[1]*1000 } +- {pstd_15[1]*1000 } Ohms')
print(f'  Reduced chi squared is {chi_15}.')

popt_20, pcov_20 = curve_fit(model, I_20[:-1], V_20[:-1], sigma = V_20_uncert[:-1], absolute_sigma = True)
pstd_20 = np.sqrt(np.diag(pcov_20))
curvefit_20 = model(I_20, popt_20[0], popt_20[1])
chi_20 = chi_square(5, 2, V_20[:-1], curvefit_20[:-1], V_20_uncert[:-1])
print(f'- Using curve_fit function for 20V, V = V_inf - R_int * I with: \n'
      f'  V_inf = {popt_20[0]} +- {pstd_20[0]} V \n'
      f'  R_int = {popt_20[1]*1000 } +- {pstd_20[1]*1000 } Ohms')
print(f'  Reduced chi squared is {chi_20}.')


######################################################################     
res_6_5 = V_6_5 - curvefit_6_5
res_10 = V_10 - curvefit_10
res_15 = V_15 - curvefit_15
res_20 = V_20 - curvefit_20

p_6_5 = popt_6_5[1] * I_6_5
u_p_6_5 = p_6_5 * np.sqrt((pstd_6_5[1] / popt_6_5[1]) ** 2 + (I_6_5_uncert / I_6_5) ** 2)
u_curvefit_6_5 = np.sqrt(pstd_6_5[0]**2 + u_p_6_5 ** 2)
u_res_6_5 = np.sqrt(V_6_5_uncert ** 2 + u_curvefit_6_5 ** 2)

p_10 = popt_10[1] * I_10
u_p_10 = p_10 * np.sqrt((pstd_10[1] / popt_10[1]) ** 2 + (I_10_uncert / I_10) ** 2)
u_curvefit_10 = np.sqrt(pstd_10[0]**2 + u_p_10 ** 2)
u_res_10 = np.sqrt(V_10_uncert ** 2 + u_curvefit_10 ** 2)

p_15 = popt_15[1] * I_15
u_p_15 = p_15 * np.sqrt((pstd_15[1] / popt_15[1]) ** 2 + (I_15_uncert / I_15) ** 2)
u_curvefit_15 = np.sqrt(pstd_15[0]**2 + u_p_15 ** 2)
u_res_15 = np.sqrt(V_15_uncert ** 2 + u_curvefit_15 ** 2)

p_20 = popt_20[1] * I_20
u_p_20 = p_20 * np.sqrt((pstd_20[1] / popt_20[1]) ** 2 + (I_20_uncert / I_20) ** 2)
u_curvefit_20 = np.sqrt(pstd_20[0]**2 + u_p_20 ** 2)
u_res_20 = np.sqrt(V_20_uncert ** 2 + u_curvefit_20 ** 2)



r_int = np.array([popt_6_5[1]*1000, popt_10[1]*1000, popt_15[1]*1000, popt_20[1]*1000])
u_r_int = np.array([pstd_6_5[1]*1000, pstd_10[1]*1000, pstd_15[1]*1000, pstd_20[1]*1000])
volt = np.array([6.5, 10, 15, 20])

def c(x, a):
    return a

popt_r, pcov_r = curve_fit(c, volt, r_int, sigma = u_r_int, absolute_sigma = True)
pstd_r = np.sqrt(np.diag(pcov_r))
curvefit_r = c(volt, popt_r)
print(f'- Using curve_fit on a function R_int vs voltages, the result is: \n'
      f'  R_int = {popt_r[0]} +- {pstd_r[0]}.')


######################################################################


plt.figure(figsize = (8, 6))
plt.errorbar(I_6_5, V_6_5, lw=1, xerr=I_6_5_uncert, yerr = V_6_5_uncert, ls= "none", marker = ".", markersize = 10,
             label = "measured data")
plt.plot(I_6_5, curvefit_6_5, label = "curve_fit result (6.5V)", lw=2)
plt.xlabel("current (mA)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid()

plt.figure(figsize = (8, 6))
plt.errorbar(I_10, V_10, lw=1, xerr=I_10_uncert, yerr = V_10_uncert, ls= "none", marker = ".", markersize = 10,
             label = "measured data")
plt.plot(I_10, curvefit_10, label = "curve_fit result (10V)", lw=2)
plt.xlabel("current (mA)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid()

plt.figure(figsize = (8, 6))
plt.errorbar(I_15, V_15, lw=1, xerr=I_15_uncert, yerr = V_15_uncert, ls= "none", marker = ".", markersize = 10,
             label = "measured data")
plt.plot(I_15, curvefit_15, label = "curve_fit result (15V)", lw=2)
plt.xlabel("current (mA)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid()

plt.figure(figsize = (8, 6))
plt.errorbar(I_20, V_20, lw=1, xerr=I_20_uncert, yerr = V_20_uncert, ls= "none", marker = ".", markersize = 10,
             label = "measured data")
plt.plot(I_20, curvefit_20, label = "curve_fit result (20V)", lw=2)
plt.xlabel("current (mA)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid()

########################################################################################

plt.figure(figsize = (8, 6))
plt.errorbar(I_6_5, res_6_5, yerr = u_res_6_5
             , marker = ".", markersize = 10, lw = 1, c = "g", ls = "none", label = "R_res for 6.5V")
plt.plot(I_6_5, [0, 0, 0, 0, 0, 0], label = "zero line", c = "orange")
plt.xlabel("Current (mA)")
plt.ylabel("measured data - curve fit data (V)")
plt.grid()
plt.legend()

plt.figure(figsize = (8, 6))
plt.errorbar(I_10, res_10, yerr = u_res_10
             , marker = ".", markersize = 10, lw = 1, c = "g", ls = "none", label = "R_res for 10V")
plt.plot(I_10, [0, 0, 0, 0, 0, 0], label = "zero line", c = "orange")
plt.xlabel("Current (mA)")
plt.ylabel("measured data - curve fit data (V)")
plt.grid()
plt.legend()

plt.figure(figsize = (8, 6))
plt.errorbar(I_15[:-1], res_15[:-1], yerr = u_res_15[:-1]
             , marker = ".", markersize = 10, lw = 1, c = "g", ls = "none", label = "R_res for 15V")
plt.plot(I_15[:-1], [0, 0, 0, 0, 0], label = "zero line", c = "orange")
plt.xlabel("Current (mA)")
plt.ylabel("measured data - curve fit data (V)")
plt.grid()
plt.legend()

plt.figure(figsize = (8, 6))
plt.errorbar(I_20[:-1], res_20[:-1], yerr = u_res_20[:-1]
             , marker = ".", markersize = 10, lw = 1, c = "g", ls = "none", label = "R_res for 20V")
plt.plot(I_20[:-1], [0, 0, 0, 0, 0], label = "zero line", c = "orange")
plt.xlabel("Current (mA)")
plt.ylabel("measured data - curve fit data (V)")
plt.grid()
plt.legend()

########################################################################################
plt.figure(figsize = (8, 6))
plt.errorbar(volt, r_int, lw=1, yerr = u_r_int, ls= "none", marker = ".", markersize = 10,
             label = "calculated R_int")
plt.plot(volt, np.array([curvefit_r, curvefit_r, curvefit_r, curvefit_r]), label = "curve_fit R_int", lw=2)
plt.xlabel('voltage (V)')
plt.ylabel('internal resistance (Ohms)')
plt.grid()
plt.legend()



