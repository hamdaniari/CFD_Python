# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:01:31 2020

@author: Hamdani
"""
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from matplotlib import cm, pyplot as plt

#variable declaration
nx = 81
ny = 81
dx = 2/(nx-1)
dy = 2/(ny-1)
nt = 100
c = 1
sigma = 0.2
dt = sigma * dx / c

x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)

#initial condition
u = np.ones((nx,ny))
un = u.copy()
#set hat function I.C. : u(0.5<=x<=1 && 0.5<=y<=1) is 2
u[int(0.5/dx):int(1/dx+1),int(0.5/dy):int(1/dy+1)] = 2

#plot initial condition
fig = plt.figure(figsize=(11,7),dpi=100)
ax = plt.gca(projection='3d')
X, Y = np.meshgrid(x, y)
Z = u
surf = ax.plot_surface(X,Y,Z,cmap=cm.viridis)

"""
#for operation
for n in range(nt+1):
    un = u.copy()
    row, col = u.shape
    for i in range(1,col):
        for j in range(1,row):
            u[i,j] = (un[i,j])-c*dt/dx*(un[i,j]-(un[i-1,j]))-c*dt/dy*(un[i,j]-un[i,j-1])
            
            u[0,:] = 1
            u[-1,:] = 1
            u[:,0] = 1
            u[:,-1] = 1
            
fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
surf2 = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)    
"""

#array operation
for n in range(nt+1):
    un = u.copy()
    u[1:,1:] = (un[1:,1:]) - c*dt/dx*(un[1:,1:]-un[0:-1,1:]) - c*dt/dy*(un[1:,1:]-un[1:,0:-1])
    
    u[0,:] = 1
    u[-1,:] = 1
    u[:,0] = 1
    u[:,-1] = 1
    
fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
surf2 = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)    