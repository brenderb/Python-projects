from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

Temps = [0.1,5,10,15,20,25,30,40,50,60,80,100]
Temps = np.array(Temps)
Densities = [1.292,1.268,1.246,1.225,1.204,1.184,1.164,1.127,1.093,1.06,1,0.9467]

def model(x, a, b, c):
    return a * (x**2) + b * x + c

popt, pcov = curve_fit(model, Temps, Densities)

plt.plot(Temps,Densities,'o', markersize='3')
plt.plot(Temps, 1.08057634e-05*(Temps**2) - 4.50882903e-03*Temps +  1.29054078e+00)
#plt.show()