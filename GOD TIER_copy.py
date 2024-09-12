## Complete rewrite
import numpy as np
import matplotlib.pyplot as plt

def plot_fourier():
    
    nt = 1024  # number of point in time array
    time = np.linspace(-1.2*np.pi, 1.2*np.pi, nt)
    
    def F(t): #to be used as a fxn of time
        return t*np.sign(np.sin(t)) + (np.pi)*(np.sign(np.sin(t)) + 1)
    
    a0 = (np.pi)/2    
    
    def approximation(t, N):
        
        if N == 0:
            return t*0 + a0
        
        approx_F = a0
        for mode in range(1, N+1, 1): #adding modes between 0 and N (the mode count that gets set by the user)
            an = (2/((np.pi)*mode**2))*np.cos(mode*t)*(np.cos(mode*np.pi) - 1)
            approx_F += an
            
        return approx_F
    
    
    
    fg, ax = plt.subplots(5, 1, sharex=True, sharey=True)
    fg.set_size_inches(15, 15)
    ax[0].set_title('F(t) & Partial sums of a0, 1, 2, 10, 100 of the Fourier series')
    ax[0].plot(time, approximation(time, 0), 'k--', label='$a0$')
    ax[0].plot(time, approximation(time, 1), label='$F(t), N = 1$')
    ax[1].plot(time, approximation(time, 2), label='$F(t), N = 2$')
    ax[2].plot(time, approximation(time, 10), label='$F(t), N = 10$')
    ax[3].plot(time, approximation(time, 100), label='$F(t), N = 100$')
    ax[4].plot(time, approximation(time, 100000), 'r-', label='$F(t)$')
    ax[0].set_xlim(time[0], time[-1])
    ax[0].grid('on')
    ax[1].grid('on')
    ax[2].grid('on')
    ax[3].grid('on')
    ax[4].grid('on')
    ax[0].legend(loc='lower left')
    ax[1].legend()
    ax[2].legend()
    ax[3].legend()
    ax[4].legend()
    ax[1].set_xticks([-np.pi, 0., np.pi])
    ax[1].set_yticks([0., np.pi/2, np.pi])
    ax[1].set_xticklabels(['$-\pi$', '$0$', '$\pi$'])
    ax[1].set_yticklabels(['$0$', '$\pi/2$', '$\pi$'])
    plt.show()
    
plot_fourier()
    
    
