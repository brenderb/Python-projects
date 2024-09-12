import numpy as np
import matplotlib.pyplot as plt

T = np.array([100,110,112,125,150,175,200])
H = np.array([-5254,-4496,3604,4039,4896,5743,6587])
S = np.array([73,78.5,152.5,156.5,162.7,168,172.5])
U = np.array([-5258, -4501, 2674, 3026, 3667, 4301, 4935])

'''
plt.figure(figsize = (8, 6))
plt.plot(T, H)
plt.xlabel('Temperature (K)')
plt.ylabel('Enthalpy (J/mol)')
plt.suptitle('Refrigerant Enthalpy v Temperature @ 1atm - Benjamin Brender')
plt.savefig('EnthalpyGraphTHERMAL.png',dpi=300)

plt.figure(figsize = (8, 6))
plt.plot(T, S)
plt.xlabel('Temperature (K)')
plt.ylabel('Entropy (J/mol*K)')
plt.suptitle('Refrigerant Entropy v Temperature @ 1atm - Benjamin Brender')
plt.savefig('EntropyGraphTHERMAL.png',dpi=300)
'''
plt.figure(figsize = (8,6))
plt.plot(T, U)
plt.show()