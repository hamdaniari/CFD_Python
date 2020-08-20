# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:50:04 2020

@author: Hamdani
"""
#Array Operations with NumPy
""" 
import numpy as np

u = np.array([0,1,2,3,4,5])

for i in range(1,len(u)):
    uni = u[i]-u[i-1]
    print(uni)
    
########
#another way
uni = u[1:]-u[0:-1]
print(uni)
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

nx = 81
ny = 81
nt = 100
c = 1
dx = 2/(nx-1)
dy = 2/(ny-1)
sigma = 0.2
dt = sigma*dx/c

x = np.linspace(0,2,nx)
y = np.linspace(0,2,ny)

u = np.ones((ny,nx))
un = np.ones((ny,nx))

###Assign initial conditions
u[int(0.5/dx):int(1/dx+1), int(0.5/dy):int(1/dy+1)]=2

#plot the innitial condition
"""
fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d') 
X,Y = np.meshgrid(x, y)
surf = ax.plot_surface(X,Y,u[:],cmap=cm.viridis)
"""

%%timeit
for n in range(nt+1):
    un=u.copy()
    row,col=u.shape
    for i in range(1,row):
        for j in range(1,col):
            u[i,j]=

