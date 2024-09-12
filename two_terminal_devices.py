import numpy as np
import matplotlib.pyplot as plt
#ohmeter measured 47.5 ohms on 47 one
#ohmeter measured 5.3 ohms on 4.7 one


R2 = 5.3

x = np.loadtxt("two_terminal_devices.txt", usecols=0, delimiter=",")
y = np.loadtxt("two_terminal_devices.txt", usecols=1, delimiter=",")
uy = np.loadtxt("two_terminal_devices.txt", usecols=2, delimiter=",")

y = y * 10 ** (-3)
uy = uy * 10 ** (-3)

V_dev = x - y
uV_dev = uy
I = y / R2
uI = I * np.sqrt((uy/y)**2)
R = V_dev / I
uR = R * np.sqrt((uI/I)**2)
print(f'{R} +- {uR}')


Vplot = np.linspace(-6.4, 6.4, 40)
TheorySlope = 1/47
RealSlope = 1/R
Yerr = np.sqrt(Vplot**2)*uR*(1/(R**2))

plt.figure(figsize=(8, 6))
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)
plt.plot(Vplot, TheorySlope*Vplot, label='Theoretical IV Characteristics of 47ohm resistor', marker="o", markersize=1.2, lw=1)
plt.errorbar(Vplot, RealSlope*Vplot, yerr=Yerr, label='Real IV Characteristics of 47ohm resistor', marker="o", markersize=1.5, lw=1, c='red', ls="none")
plt.xlabel("Voltage (V)", fontsize=14)
plt.ylabel("Current (I)", fontsize=14)
plt.grid()
plt.legend(fontsize=13)


zeroline = np.linspace(0, 0, 40)
res = RealSlope*Vplot - TheorySlope*Vplot
ures = Yerr
plt.figure(figsize=(8, 6))
plt.plot(Vplot, zeroline, label="zero line")
plt.errorbar(Vplot, res, yerr=ures, label='Residual', marker="o", markersize=1.5, lw=1, c='red', ls="none")
plt.xlabel("Voltage (V)", fontsize=14)
plt.ylabel("Residual", fontsize=14)
plt.grid()
plt.legend(fontsize=13)
plt.show()







