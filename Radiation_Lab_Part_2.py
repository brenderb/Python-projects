import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from scipy.stats import norm

background203 = np.loadtxt('background20min3sec2024.txt', skiprows=2)
fiesta203 = np.loadtxt('fiesta20min3sec2024.txt', skiprows=2)

##################### background mean + std

background203_count = []

for i in range(0, len(background203)):
    background203_count.append(background203[i][1])
            
background203mean = np.mean(background203_count)
background203std = np.sqrt(background203mean)
print(max(background203_count), min(background203_count))
bgarray = np.array([0,1,2,3])

###################### fiesta mean + histogram

fiesta203_count = [] # the count to use

for i in range(0, len(fiesta203)):
    fiesta203_count.append(fiesta203[i][1])

fiesta203mean = sum(fiesta203_count) / len(fiesta203_count)

narray = np.empty(61-18 + 1)
for i in range(0, len(narray)):
    narray[i] = i+18


################## Plotting

plt.figure(figsize = (8, 6))
plt.plot(narray, poisson.pmf(narray, fiesta203mean), label='Poisson distribution')
plt.plot(narray, norm.pdf(narray,loc=fiesta203mean, scale=np.sqrt(fiesta203mean)), label='Normal distribution')
plt.hist(fiesta203_count, density=True, label='Histogram (normalized)')
plt.legend()
plt.grid()
plt.xlabel('Number of samples')
plt.ylabel('Count/Total count')

plt.figure(figsize = (8, 6))
plt.plot(bgarray, poisson.pmf(bgarray, background203mean), label='Poisson distribution')
plt.plot(bgarray, norm.pdf(bgarray, loc=background203mean, scale=np.sqrt(background203mean)), label='Normal distribution')
plt.hist(background203_count, density=True, label='Histogram (normalized)')
plt.legend()
plt.grid()
plt.xlabel('Number of samples')
plt.ylabel('Count/Total count')
print(background203mean)
plt.show()