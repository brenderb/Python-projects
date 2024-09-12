import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

background2020 = np.loadtxt('background20min20sec2024.txt', skiprows=2)
cesium2020 = np.loadtxt('cesium20min20sec2024.txt', skiprows=2)

##################### Computing background mean + std

background2020_count = []

for i in range(0, len(background2020)):
    background2020_count.append(background2020[i][1])
            
background2020mean = sum(background2020_count) / len(background2020)
background2020std = np.sqrt(background2020mean)

##################### Computing counts and standard deviations

cesium2020_samplenum = []
cesium2020_count = [] # the count to use
cesium2020_countstd = []
cesium2020std = [] # The STD to use

for i in range(0, len(cesium2020)):
    cesium2020_samplenum.append(cesium2020[i][0])
    cesium2020_count.append(cesium2020[i][1] - background2020mean)
    cesium2020_countstd.append(np.sqrt(cesium2020[i][1]))
    cesium2020std.append(np.sqrt(background2020std**2 + cesium2020_countstd[i]**2))
        
##################### Computing Rates + Creating time arrays

deltaT2020 = (1220/60) / 60

cesium2020_rate = np.array(cesium2020_count) / deltaT2020 # Final Use for curve_fit
cesium2020_std_rate = np.array(cesium2020std) / deltaT2020 # Final Use for curve_fit

time2020 = np.empty(len(cesium2020_rate))

for i in range(0, len(time2020)):
    time2020[i] = (i+1)*deltaT2020
    
##################### Defining model functions

def f(x, a, b):
    return a*x + b

def g(x, a, b):
    return a * (1/2)**(x/b)

##################### Using curve_fit for exponential fit

cesiumHLparams, pcov = curve_fit(g, time2020, cesium2020_rate, sigma=cesium2020_std_rate, absolute_sigma=True)
cesiumHLstd = np.sqrt(np.diag(pcov))

I0 = cesiumHLparams[0]
half_life = cesiumHLparams[1]
half_life_std = cesiumHLstd[1]
print('The non-linear regression method yielded a half life of ' + str(half_life) + ' +- ' + str(half_life_std) + ' minutes.')

IOSTD = cesiumHLstd[0]
EXP_RES_UNC = []
for i in time2020:
    EXP_RES_UNC.append(np.sqrt((((1/2)**(2*i/half_life)) * IOSTD**2) + (((I0*i*np.log(2)) / (half_life**2 * 2**(i/half_life)))**2) * half_life_std**2))

print(EXP_RES_UNC)

##################### Using curve_fit for linear regression

cesiumHLparamslinear, pcovlinear = curve_fit(f, time2020, np.log(cesium2020_rate), sigma=(cesium2020_std_rate/cesium2020_rate), absolute_sigma=True)
cesiumHLstdlinear = np.sqrt(np.diag(pcovlinear))

I0linear = np.exp(cesiumHLparamslinear[1])
half_life_linear = np.log(1/2) / cesiumHLparamslinear[0]
half_life_linear_std = cesiumHLstdlinear[0]
REALSTD = half_life_linear * half_life_linear_std * (half_life_linear / np.log((1/2))) # Use
print('The linear regression method yielded a half life of ' + str(half_life_linear) + ' +- ' + str(REALSTD) + ' minutes.')

I0LINSTD = I0*cesiumHLstdlinear[1]
LIN_RES_UNC = []
for i in time2020:
    LIN_RES_UNC.append(np.sqrt((((1/2)**(2*i/half_life_linear)) * I0LINSTD**2) + (((I0linear*i*np.log(2)) / (half_life_linear**2 * 2**(i/half_life_linear)))**2) * REALSTD**2))
print(LIN_RES_UNC)

##################### Chi^2

def chi_square(num_datapoints, num_parameters, measure_data, prediction, sigma):
    result = (1 / (num_datapoints - num_parameters)) * (np.sum(
        ((measure_data - prediction) ** 2) / (sigma ** 2)
        ))
    return result

chinonlinear = chi_square(len(time2020), 2, cesium2020_rate, (I0 * (1/2)**(time2020/half_life)), cesium2020_std_rate)
chilinear = chi_square(len(time2020), 2, cesium2020_rate, (I0linear * (1/2)**(time2020/half_life_linear)), cesium2020_std_rate)
print('Reduced chi squared for the non linear best fit is ' + str(chinonlinear))
print('Reduced chi squared for the linear best fit is ' + str(chilinear))
##################### Plotting

plt.figure(figsize = (8, 6))
plt.errorbar(time2020, cesium2020_rate, yerr=cesium2020_std_rate, label='measured data', ls='', marker='o', markersize='2')
plt.plot(time2020, I0linear * (1/2)**(time2020/half_life_linear), label='fitted with linear regression')
plt.plot(time2020, I0 * (1/2)**(time2020/half_life), label='fitted non linear regression')
plt.plot(time2020, I0 * (1/2)**(time2020/(156/60)), label='theoretical half life')
plt.legend()
plt.grid()
plt.xlabel('Time (mins)')
plt.ylabel('Rate (I/mins)')

plt.figure(figsize = (8, 6))
plt.errorbar(time2020, cesium2020_rate, yerr=cesium2020_std_rate, label='measured data', ls='', marker='o', markersize='2')
plt.semilogy(time2020, I0linear * (1/2)**(time2020/half_life_linear), label='fitted with linear regression')
plt.semilogy(time2020, I0 * (1/2)**(time2020/half_life), label='fitted non linear regression')
plt.semilogy(time2020, I0 * (1/2)**(time2020/(156/60)), label='theoretical half life')
plt.legend()
plt.grid()
plt.xlabel('Time (mins)')
plt.ylabel('ln(Rate) (I/mins)')

RES_UNC_E_FINAL = []
for i in range(0, len(time2020)):
    RES_UNC_E_FINAL.append(np.sqrt(cesium2020_std_rate[i]**2 + EXP_RES_UNC[i]**2))
    
RES_UNC_L_FINAL = []
for i in range(0, len(time2020)):
    RES_UNC_L_FINAL.append(np.sqrt(cesium2020_std_rate[i]**2 + LIN_RES_UNC[i]**2))

plt.figure(figsize = (8, 6))
plt.plot(time2020, time2020*0, label='Zero line')
plt.errorbar(time2020, cesium2020_rate - (I0 * (1/2)**(time2020/half_life)), yerr=RES_UNC_E_FINAL, label='Residual of non-linear regression',color='tab:green', ls='', marker='o', markersize='2')
plt.legend()
plt.grid()
plt.xlabel('Time (mins)')
plt.ylabel('(Rate) (I/mins)')
plt.savefig('RESIDUAL_NONLIN.png', dpi=300)

plt.figure(figsize = (8, 6))
plt.plot(time2020, time2020*0, label='Zero line')
plt.errorbar(time2020, cesium2020_rate - (I0linear * (1/2)**(time2020/half_life_linear)), yerr=RES_UNC_L_FINAL, label='Residual of linear regression', ls='', marker='o', markersize='2')
plt.legend()
plt.grid()
plt.xlabel('Time (mins)')
plt.ylabel('(Rate) (I/mins)')
plt.savefig('RESIDUAL_LIN.png', dpi=300)

print(I0, cesiumHLstd[0])
print(I0linear, I0*cesiumHLstdlinear[1])
print(half_life, half_life_std)
print(half_life_linear, REALSTD)
plt.show()
