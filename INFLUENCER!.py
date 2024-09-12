import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

tmax = 10
x0 = -0.9
y0 = -0.9
z0 = -0.9

def EF(t, position):
    """ Electric field as a function of position=[x, y, z] for a single
    charge located at the origin.
    Note: we need to keep the t argument, even if we don't use it. """
    x, y, z = position # unpack the position vector
    # Electric field, setting 1/(4*pi*epsilon0) to 1 for simplicity
    rsep = (x**2 + y**2 + z**2)**0.5 # separation distance
    EFx = x/rsep**3
    EFy = y/rsep**3
    EFz = z/rsep**3
    return EFx, EFy, EFz

solution = solve_ivp(EF, [0, tmax], [x0, y0, z0], rtol=1e-3)
EFline_x = solution.y[0, :]
EFline_y = solution.y[1, :]
EFline_z = solution.y[2, :]

ax = plt.figure().add_subplot(projection='3d') # initialize 3D figure
ax.plot(EFline_x, EFline_y, EFline_z)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
plt.show()

