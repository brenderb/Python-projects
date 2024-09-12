import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

'''
Part A_2 measured result:
volt on power supply = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
voltmeter = [9.998, 10.998, 11.998, 12.998, 13.998, 14.997, 15.998, 16.997, 17.999, 18.998, 19,998]V
I = [0.709, 0.780, 0.851, 0.922, 0.993, 1.064, 1.135, 1.207, 1.278, 1.349, 1.420]mA
potentiometer = 14.096 kiloOhms
'''

#measured voltage
on_volt_meter_A_2 = np.loadtxt("Ohms_Law_A_2.txt", delimiter = ",", usecols = 0) #V
#uncertainty for voltage
voltage_uncertainty_A_2 = np.array([])
for i in range(0, len(on_volt_meter_A_2)):
    voltage_uncertainty_A_2 = np.append(voltage_uncertainty_A_2, 0.002 + 0.0005*on_volt_meter_A_2[i]) #V
    

#measured current
I_A_2_mA = np.loadtxt("Ohms_Law_A_2.txt", delimiter = ",", usecols = 1) #mA
I_A_2 = I_A_2_mA / 1000 #A
#uncertainty for current
current_uncertainty_A_2_mA = np.array([])
for i in range(0, len(I_A_2_mA)):
    current_uncertainty_A_2_mA = np.append(current_uncertainty_A_2_mA, 0.005 + 0.002*I_A_2_mA[i]) #mA
current_uncertainty_A_2 = current_uncertainty_A_2_mA / 1000 #A
    

#curve fit
def model(x, a, b):
    return a * x + b

popt, pcov = curve_fit(model, on_volt_meter_A_2, I_A_2, sigma = current_uncertainty_A_2, absolute_sigma = True)
pstd = np.sqrt(np.diag(pcov))
curve_fit = model(on_volt_meter_A_2, popt[0], popt[1])

#return results
print(f'- Using Curve_fit function, the estimated 1 / R is: \n'
      f'  {popt[0]} +- {pstd[0]} Ohms^-1.')

#find actual resistance. Above is 1/R
actual_r = 1 / popt[0]
uncert_actual_r = (1 / popt[0]) * (pstd[0] / popt[0])
print(f' \n'
      f'- So the estimated resistance R should be: \n'
      f'  {actual_r} +- {uncert_actual_r} Ohms.')



#Caculate chi square
def chi_square(num_datapoints, num_parameters, measure_data, prediction, sigma):
    result = (1 / (num_datapoints - num_parameters)) * (np.sum(
        ((measure_data - prediction) ** 2) / (sigma ** 2)
        ))
    return result

chi_squared = chi_square(11, 2, I_A_2, curve_fit, current_uncertainty_A_2)
print(f' \n'
      f'- Chi_red squared for our curve fit function is {chi_squared}.')


#residual
res = I_A_2 - curve_fit
a_times_x = on_volt_meter_A_2 * popt[0]
u_a_times_x = a_times_x * np.sqrt(
    (voltage_uncertainty_A_2 / on_volt_meter_A_2) ** 2 + (pstd[0] / popt[0]) ** 2
    )
u_curve_fit = curve_fit * np.sqrt(
    (u_a_times_x / a_times_x) ** 2 + (pstd[1] / popt[1]) ** 2
    )
u_res = np.sqrt(
    u_curve_fit ** 2 + current_uncertainty_A_2 ** 2
    )


#plot
plt.figure(figsize = (8, 6))
plt.errorbar(on_volt_meter_A_2, I_A_2, xerr = voltage_uncertainty_A_2, yerr = current_uncertainty_A_2
             , marker = ".", markersize = 9, ls = "none", label = "measured data")
plt.plot(on_volt_meter_A_2, curve_fit, label = "voltage vs. current graph using curve fit", lw = 2)
plt.xlabel("Voltage (Volts)")
plt.ylabel("Current (Ampere)")
plt.grid()
plt.legend()

plt.figure(figsize = (8, 6))
plt.errorbar(on_volt_meter_A_2, res, yerr = u_res
             , marker = ".", markersize = 15, ls = "none", label = "how much curve fit differs from measured data")
plt.plot(on_volt_meter_A_2, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], label = "zero line")
plt.xlabel("voltage (Volts)")
plt.ylabel("measured data - curve fit data (Ampere)")
plt.grid()
plt.legend()
plt.show()