# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:49:56 2020

@author: Hamdani
"""

import numpy as np
from matplotlib import pyplot as plt
import time,sys

nx = 41
dx = 2/(nx-1)
nt = 25
dt = 0.025
c = 1

u = np.ones(nx)
u[int(0.5/dx):int(1/dx+1)]=2

plt.plot(np.linspace(0,2,nx),u)

un = np.ones(nx)

for n in range(nt):
    un = u.copy()
    for i in range(1,nx):
   #for in range(nx):
        u[i]=un[i]-un[i]*dt/dx*(un[i]-un[i-1])
        
plt.plot(np.linspace(0,2,nx),u)
