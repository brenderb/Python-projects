import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

tmax = 20

pos_x_coord = 0
pos_y_coord = -0.5
pos_z_coord = 0.5

neg_x_coord = 0
neg_y_coord = 0.5
neg_z_coord = 0

middle_x_coord = 0.5
middle_y_coord = 0
middle_z_coord = 1.3

ax = plt.figure().add_subplot(projection='3d') # initialize 3D figure

for i in range(0,2):
    
    x0 = 0.05 - 0.1*i
    y0 = -0.5
    z0 = 0.5

    def EF(t, position):
        """ Electric field as a function of position=[x, y, z] for a single
        charge located at the origin.
        Note: we need to keep the t argument, even if we don't use it. """
        x, y, z = position # unpack the position vector
        # Electric field, setting 1/(4*pi*epsilon0) to 1 for simplicity
        rsep_pos = ((x - pos_x_coord)**2 + (y - pos_y_coord)**2 + (z - pos_z_coord)**2)**0.5 # separation distance
        rsep_neg = ((x - neg_x_coord)**2 + (y - neg_y_coord)**2 + (z - neg_z_coord)**2)**0.5 # separation distance
        rsep_middle = ((x - middle_x_coord)**2 + (y - middle_y_coord)**2 + (z - middle_z_coord)**2)**0.5 # separation distance
    
        EFx = (x - pos_x_coord)/rsep_pos**3 - (x - neg_x_coord)/rsep_neg**3 + (x - middle_x_coord)/rsep_middle**3
        EFy = (y - pos_y_coord)/rsep_pos**3 - (y - neg_y_coord)/rsep_neg**3 + (y - middle_y_coord)/rsep_middle**3
        EFz = (z - pos_z_coord)/rsep_pos**3 - (z - neg_z_coord)/rsep_neg**3 + (z - middle_z_coord)/rsep_middle**3
        return EFx, EFy, EFz

    solution = solve_ivp(EF, [0, tmax], [x0, y0, z0], rtol=1e-3)
    EFline_x = solution.y[0, :]
    EFline_y = solution.y[1, :]
    EFline_z = solution.y[2, :]

    ax.plot(EFline_x, EFline_y, EFline_z, color='k')
    print(x0)
    
    
for i in range(0,2):
    
    x0 = 0.05
    y0 = -0.5
    z0 = 0.55 - 0.1*i

    def EF(t, position):
        """ Electric field as a function of position=[x, y, z] for a single
        charge located at the origin.
        Note: we need to keep the t argument, even if we don't use it. """
        x, y, z = position # unpack the position vector
        # Electric field, setting 1/(4*pi*epsilon0) to 1 for simplicity
        rsep_pos = ((x - pos_x_coord)**2 + (y - pos_y_coord)**2 + (z - pos_z_coord)**2)**0.5 # separation distance
        rsep_neg = ((x - neg_x_coord)**2 + (y - neg_y_coord)**2 + (z - neg_z_coord)**2)**0.5 # separation distance
        rsep_middle = ((x - middle_x_coord)**2 + (y - middle_y_coord)**2 + (z - middle_z_coord)**2)**0.5 # separation distance
    
        EFx = (x - pos_x_coord)/rsep_pos**3 - (x - neg_x_coord)/rsep_neg**3 + (x - middle_x_coord)/rsep_middle**3
        EFy = (y - pos_y_coord)/rsep_pos**3 - (y - neg_y_coord)/rsep_neg**3 + (y - middle_y_coord)/rsep_middle**3
        EFz = (z - pos_z_coord)/rsep_pos**3 - (z - neg_z_coord)/rsep_neg**3 + (z - middle_z_coord)/rsep_middle**3
        return EFx, EFy, EFz

    solution = solve_ivp(EF, [0, tmax], [x0, y0, z0], rtol=1e-3)
    EFline_x = solution.y[0, :]
    EFline_y = solution.y[1, :]
    EFline_z = solution.y[2, :]

    ax.plot(EFline_x, EFline_y, EFline_z, color='k')
    print(x0)
    
for i in range(0,2):
    
    x0 = -0.05
    y0 = -0.5
    z0 = 0.55 - 0.1*i

    def EF(t, position):
        """ Electric field as a function of position=[x, y, z] for a single
        charge located at the origin.
        Note: we need to keep the t argument, even if we don't use it. """
        x, y, z = position # unpack the position vector
        # Electric field, setting 1/(4*pi*epsilon0) to 1 for simplicity
        rsep_pos = ((x - pos_x_coord)**2 + (y - pos_y_coord)**2 + (z - pos_z_coord)**2)**0.5 # separation distance
        rsep_neg = ((x - neg_x_coord)**2 + (y - neg_y_coord)**2 + (z - neg_z_coord)**2)**0.5 # separation distance
        rsep_middle = ((x - middle_x_coord)**2 + (y - middle_y_coord)**2 + (z - middle_z_coord)**2)**0.5 # separation distance
    
        EFx = (x - pos_x_coord)/rsep_pos**3 - (x - neg_x_coord)/rsep_neg**3 + (x - middle_x_coord)/rsep_middle**3
        EFy = (y - pos_y_coord)/rsep_pos**3 - (y - neg_y_coord)/rsep_neg**3 + (y - middle_y_coord)/rsep_middle**3
        EFz = (z - pos_z_coord)/rsep_pos**3 - (z - neg_z_coord)/rsep_neg**3 + (z - middle_z_coord)/rsep_middle**3
        return EFx, EFy, EFz

    solution = solve_ivp(EF, [0, tmax], [x0, y0, z0], rtol=1e-3)
    EFline_x = solution.y[0, :]
    EFline_y = solution.y[1, :]
    EFline_z = solution.y[2, :]

    ax.plot(EFline_x, EFline_y, EFline_z, color='k')
    print(x0)
    
    
ax.plot(0, -0.5, 0.5, 'ro') # charge 1 +
ax.plot(0, 0.5, 0, 'bo') # charge 2 -
ax.plot(0.5, 0, 1.3, 'ro') # charge middle +

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')

plt.title("6.2 | 3D Dipole 'Random' Configuration | Benjamin Brender")
plt.savefig('3D Dipole Random Config', dpi=300)
plt.show()

