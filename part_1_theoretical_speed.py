import numpy as np

L0 = 1.5 * 10**(-3)
C0 = 0.01 * 10**(-6)

uL = 0.1*L0
uC = 0.03*C0

vsqred = 1/(L0*C0)
v = np.sqrt(vsqred)

u = np.sqrt((uL**2)/(4*C0*(L0**3)) + (uC**2)/(4*L0*(C0**3)))

print('the theoretical speed is ' + str(v) + ' +- ' + str(u))

# uncertainty propagations done by hand and simplified so that python math wouldn't be a mess. see sample calculations