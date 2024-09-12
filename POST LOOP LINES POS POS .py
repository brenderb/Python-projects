import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

tmax = 10000

pos_x_coord = 0
pos_y_coord = -0.5
pos_z_coord = 0.5

pos_2_x_coord = 0
pos_2_y_coord = 0.5
pos_2_z_coord = 1

neg_2_x_coord = 0
neg_2_y_coord = 0
neg_2_z_coord = 1


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
        rsep_neg = ((x - pos_2_x_coord)**2 + (y - pos_2_y_coord)**2 + (z - pos_2_z_coord)**2)**0.5 # separation distance
        rsep_pos_2 = ((x - neg_2_x_coord)**2 + (y - neg_2_y_coord)**2 + (z - neg_2_z_coord)**2)**0.5 # separation distance
    
        EFx = (x - pos_x_coord)/rsep_pos**3 - (x - pos_2_x_coord)/rsep_neg**3 + (x - neg_2_x_coord)/rsep_pos_2**3
        EFy = (y - pos_y_coord)/rsep_pos**3 - (y - pos_2_y_coord)/rsep_neg**3 + (y - neg_2_y_coord)/rsep_pos_2**3
        EFz = (z - pos_z_coord)/rsep_pos**3 - (z - pos_2_z_coord)/rsep_neg**3 + (z - neg_2_z_coord)/rsep_pos_2**3
        return EFx, EFy, EFz

    solution = solve_ivp(EF, [0, tmax], [x0, y0, z0], rtol=1e-3)
    EFline_x = solution.y[0, :]
    EFline_y = solution.y[1, :]
    EFline_z = solution.y[2, :]

    ax.plot(EFline_x, EFline_y, EFline_z, color='k')
    print(x0)
    
ax.plot(pos_x_coord, pos_y_coord, pos_z_coord, 'ro') # charge 1 +
ax.plot(pos_2_x_coord, pos_2_y_coord, pos_2_z_coord, 'bo') # charge 2 -
ax.plot(neg_2_x_coord, neg_2_y_coord, neg_2_z_coord, 'go') # charge 2 +

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')

plt.title("6.2 | 3D Dipole 'Random' Config | Benjamin Brender")
plt.savefig('3D Dipole_3D_Config.png', dpi=300)
plt.show()

