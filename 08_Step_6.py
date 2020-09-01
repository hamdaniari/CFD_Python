# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 09:12:21 2020

@author: Hamdani
"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, pyplot as plt 
import numpy as np

#variable declarations
nx = 81
ny = 81
dx = 2/(nx-1)
dy = 2/(ny-1)
sigma = 0.2
nt = 100
dt = sigma * dx

x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)

#initial conditon
u = np.ones([nx,ny])
v = np.ones([nx,ny])
un = u.copy()
vn = v.copy()

u[int(0.5/dx):int(1/dx+1), int(0.5/dy):int(1/dy+1)] = 2
v[int(0.5/dx):int(1/dx+1), int(0.5/dy):int(1/dy+1)] = 2

#plot initial  condition
fig = plt.figure(figsize=(11,7),dpi=100)
ax = fig.gca(projection='3d')
#make mesh
X, Y = np.meshgrid(x,y)
#plot
surf = ax.plot_surface(X,Y,u,cmap = cm.viridis )
ax.set_xlabel('x')
ax.set_ylabel('y')

for n in range(nt+1):
    un = u.copy()
    vn = v.copy()
    u[1:,1:] = un[1:,1:] - dt*un[1:,1:]/dx*(un[1:,1:]-un[0:-1,1:]) - dt*vn[1:,1:]/dy*(un[1:,1:]-un[1:,0:-1])
    v[1:,1:] = vn[1:,1:] - dt*un[1:,1:]/dx*(vn[1:,1:]-vn[0:-1,1:]) - dt*vn[1:,1:]/dy*(vn[1:,1:]-vn[1:,0:-1])
    
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
X, Y = np.meshgrid(x,y)
surf2 = ax.plot_surface(X,Y,u,cmap = cm.viridis )
ax.set_xlabel('x')
ax.set_ylabel('y')

fig = plt.figure(figsize=(11,7),dpi=100)
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x,y)
surf3 = ax.plot_surface(X,Y,v,cmap = cm.viridis )
ax.set_xlabel('x')
ax.set_ylabel('y')