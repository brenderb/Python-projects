import matplotlib.pyplot as plt
import numpy as np

def fibo(n):
    n_list = [1,1]
    for i in range(2,n+1):
        n_list.append(n_list[-1] + n_list[-2])
    return n_list[n - 1]

def fibolist(n):
    n_list = [1,1]
    for i in range(2,n+1):
        n_list.append(n_list[-1] + n_list[-2])
    return n_list

points_per_seg = 100
total_spins = 10
total_segs = total_spins*4

t = np.linspace(0,total_spins*2*np.pi,points_per_seg*total_segs)

R_list = fibolist(int(len(t)/points_per_seg))
R_list = R_list[1:]

RofT = []
keyindices = []
for i in range(0,len(t)):
    RofT.append(R_list[int(np.floor(i/points_per_seg))])
for i in range(1,len(RofT)):
    if RofT[i]!= RofT[i-1]:
        keyindices.append(i)
     
xlist=[]
ylist=[]
counter = 0
xvar = 0
yvar = 0
for i in range(0,len(t)):
    temp = counter
    if i in keyindices:
        if counter == 1:
            counter = 2
        elif counter == 2:
            counter = 3
        elif counter == 3:
            counter = 4
        elif counter == 4:
            counter = 1
        elif counter ==0:
            counter = 1 
    if temp != counter:
        if counter == 1:
            yvar = yvar - (RofT[i+1 ] - RofT[i - 3])
        if counter == 2:
            xvar = xvar + (RofT[i+1 ] - RofT[i - 3])
        if counter == 3:
            yvar = yvar + (RofT[i+1 ] - RofT[i - 3])
        if counter == 4:
            xvar = xvar - (RofT[i+1 ] - RofT[i - 3])
           
    xlist.append(xvar)
    ylist.append(yvar) 

plt.plot(RofT*np.cos(t) + xlist,RofT*np.sin(t) + ylist)
plt.grid()
plt.show()