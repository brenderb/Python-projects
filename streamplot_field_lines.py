""" Pythonic solution to Griffith's Problem 2.65(b) of the 5th edition
Draw field lines for two positive charges and a dipole
"""

import numpy as np
import matplotlib.pyplot as plt

xx = np.arange(-1., 1., 0.02)
zz = 1*xx
x2d, z2d = np.meshgrid(xx, zz)

msize = 12  # size of charge location markers

# %%
# Part (b) asks for field lines emanating from two charges of the same
# and of opposite charges.

# Charge located at z=-0.5
z2d1 = z2d + 0.5  # z-separation
r2d1 = (x2d**2 + z2d1**2)**0.5  # separation distance
EFx1, EFz1 = x2d/r2d1**3, z2d1/r2d1**3  # electric field (absolute value)

# Charge located at x=+0.5
z2d2 = z2d - 0.5  # x-separation
r2d2 = (x2d**2 + z2d2**2)**0.5  # separation distance
EFx2, EFz2 = x2d/r2d2**3, z2d2/r2d2**3  # electric field (absolute value)

# Charges of the same sign first
EFx_same = EFx1 + EFx2
EFz_same = EFz1 + EFz2

plt.figure()
plt.streamplot(x2d, z2d, EFx_same, EFz_same,  # the basic options
               broken_streamlines=False,  # Field lines must be continuous
               color='k', linewidth=0.5,  # why not
               density=0.5)  # figure gets too busy otherwise
plt.plot(0., -0.5, 'r+', markersize=msize)  # positive charge with a red +
plt.plot(0., 0.5, 'r+', markersize=msize)  # positive charge with a red +
plt.xlabel('$x$')
plt.ylabel('$z$')
plt.gca().set_aspect('equal')
# Save the figure as a .png file you can then insert into a report
plt.savefig('two_positives.png')


# %% Charges of opposite signs next
EFx_opp = EFx1 - EFx2
EFz_opp = EFz1 - EFz2
plt.figure()
# Below, I reduce the density of lines; figure gets too busy otherwise
plt.streamplot(x2d, z2d, EFx_opp, EFz_opp,
               color='k', linewidth=0.5,  # why not
               broken_streamlines=False,  # Field lines must be continuous
               density=0.5)  # figure gets too busy otherwise
plt.plot(0., -0.5, 'r+', markersize=msize)  # positive charge with a red +
plt.plot(0., 0.5, 'b_', markersize=msize)  # negative charge with a blue -
plt.plot(0., 0.5, 'bo', markersize=msize, fillstyle='none')
plt.xlabel('$x$')
plt.ylabel('$z$')
plt.gca().set_aspect('equal')
# Save the figure as a .png file you can then insert into a report
plt.savefig('dipole.png')

# Show the figures on your screen. This line should be last in general
# because it then flushes all existing figures out of the computer's memory
plt.show()
