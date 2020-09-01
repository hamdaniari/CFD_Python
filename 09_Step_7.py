# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:54:36 2020

@author: Hamdani
"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, pyplot as plt
import numpy as np

#variable declarations
nx  =31
ny = 31
dx = 2/(nx-1)
dy = 2/(ny-1)
nu = 0.05
nt = 17
sigma = 0.25
dt = sigma * dx * dy / nu

x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)

u = np.ones([nx,ny])
un = u.copy()

#I.C
u[int(0.5/dx):int(1/dx+1),int(0.5/dy):int(1/dy+1)] = 2

#plot I.C
fig = plt.figure(figsize=(11,7),dpi=100)
ax = fig.gca(projection = '3d')
X,Y = np.meshgrid(x, y)
surf = ax.plot_surface(X,Y,u,cmap=cm.viridis)
ax.set_zlim(1, 2.5)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

"""
for n in range(nt+1):
    un = u.copy()
    u[1:-1,1:-1] = un[1:-1,1:-1] + dt/dx**2*nu*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[0:-2,1:-1]) + dt/dy**2*nu*(un[1:-1,2:]-2*un[1:-1,1:-1]+un[1:-1,0:-2])
    
    u[0,:] = 1
    u[-1,:] = 1
    u[:,0] = 1
    u[:,-1] = 1

fig = plt.figure(figsize=(11,7),dpi=100)
ax = fig.gca(projection = '3d')
X,Y = np.meshgrid(x, y)
surf2 = ax.plot_surface(X,Y,u,cmap=cm.viridis)
"""

#Run through nt timesteps
def diffuse(nt):
    u[int(0.5/dx):int(1/dx+1),int(0.5/dy):int(1/dy+1)] = 2
    
    for n in range(nt+1):
        un = u.copy()
        u[1:-1,1:-1] = un[1:-1,1:-1] + dt/dx**2*nu*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[0:-2,1:-1]) + dt/dy**2*nu*(un[1:-1,2:]-2*un[1:-1,1:-1]+un[1:-1,0:-2])
    
        u[0,:] = 1
        u[-1,:] = 1
        u[:,0] = 1
        u[:,-1] = 1
        
diffuse(50)

fig = plt.figure(figsize=(11,7),dpi=100)
ax = fig.gca(projection = '3d')
X,Y = np.meshgrid(x, y)
surf3 = ax.plot_surface(X,Y,u,cmap=cm.viridis)
ax.set_zlim(1, 2.5)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')


    
    