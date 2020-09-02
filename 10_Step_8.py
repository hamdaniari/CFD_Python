# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:48:48 2020

@author: Hamdani
"""

import numpy  as np
from matplotlib import cm, pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

#variable declaration
nx = 41
ny = 41
nt = 120
dx = 2/(nx-1)
dy = 2/(ny-1)
sigma = 0.0009
nu = 0.01
dt = sigma * dx * dy / nu

x = np.linspace(0,2,nx)
y = np.linspace(0,2,ny)

u = np.ones([nx,ny])
v = np.ones([nx,ny])
un = u.copy()
vn = v.copy()
comb = np.ones([nx,ny])

#I.C
u[int(0.5/dx):int(1/dx+1),int(0.5/dy):int(1/dy+1)] = 2
v[int(0.5/dx):int(1/dx+1),int(0.5/dy):int(1/dy+1)] = 2

#plot I.C
fig = plt.figure(figsize=(11,7),dpi=100)
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x, y)
ax.plot_surface(X,Y,u,cmap=cm.viridis)
ax.set_xlabel('x')
ax.set_ylabel('y')

for n in range(nt+1):
    un = u.copy()
    vn = v.copy()
    u[1:-1,1:-1] = (un[1:-1,1:-1] - 
                    dt/dx*un[1:-1,1:-1]*
                    (un[1:-1,1:-1]-un[0:-2,1:-1]) - 
                    dt/dy*vn[1:-1,1:-1]*
                    (un[1:-1,1:-1]-un[1:-1,0:-2]) + 
                    nu*dt/dx**2*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[0:-2,1:-1]) + 
                    nu*dt/dy**2*(un[1:-1,2:]-2*un[1:-1,1:-1]+un[1:-1,0:-2]))
    v[1:-1,1:-1] = (vn[1:-1,1:-1] - 
                    dt/dx*un[1:-1,1:-1]*
                    (vn[1:-1,1:-1]-vn[0:-2,1:-1]) - 
                    dt/dy*vn[1:-1,1:-1]*(vn[1:-1,1:-1]-vn[1:-1,0:-2]) + 
                    nu*dt/dx**2*(vn[2:,1:-1]-2*vn[1:-1,1:-1]+vn[0:-2,1:-1]) + 
                    nu*dt/dy**2*(vn[1:-1,2:]-2*vn[1:-1,1:-1]+vn[1:-1,0:-2]))
    
    u[0,:] = 1
    u[-1,:] = 1
    u[:,0] = 1
    u[:,-1] = 1
    
    v[0,:] = 1
    v[-1,:] = 1
    v[:,0] = 1
    v[:,-1] = 1

fig = plt.figure(figsize=(11,7),dpi=100)
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x, y)
ax.plot_surface(X,Y,u,cmap=cm.viridis)
ax.plot_surface(X,Y,v,cmap=cm.viridis)
ax.set_zlim(1, 2)
ax.set_xlabel('x')
ax.set_ylabel('y')