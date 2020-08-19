# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:42:06 2020

@author: Hamdani
"""

import numpy as np
from matplotlib import pyplot as plt

def linearconv(nx):
    nt=25
    dx=2/(nx-1)
    sigma=0.3
    nu=0.3 #value of viscosity
    
    dt=sigma*dx**2/nu
    
    u=np.ones(nx)
    u[int(0.5/dx):int(1/dx+1)]=2
    
    for n in range(nt):
        un=u.copy()
        for i in range(1,nx-1):
            u[i]=un[i]+dt/(dx**2)*nu*(un[i+1]-2*un[i]+un[i-1])
    plt.plot(np.linspace(0,2,nx),u)