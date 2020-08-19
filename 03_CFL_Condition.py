# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:21:03 2020

@author: Hamdani
"""

#CFL is not defined, therefore whenr nx>90. the wave is travelling a distance which is greater than dx
"""
import numpy as np
from matplotlib import pyplot as plt

def linearconv(nx):
    nt=25
    dt=0.025
    dx=2/(nx-1)
    c=1
    
    u=np.ones(nx)
    u[int(0.5/dx):int(1/dx+1)]=2
    
    for n in range(nt):
        un=u.copy()
        for i in range(1,nx):
            u[i]=un[i]-dt/dx*c*(un[i]-un[i-1])
    plt.plot(np.linspace(0,2,nx),u)
            
"""   

import numpy as np
from matplotlib import pyplot as plt

def linearconv(nx):
    nt=25
    dx=2/(nx-1)
    c=1
    sigma=0.5
    
    dt=sigma*dx/c
    
    u=np.ones(nx)
    u[int(0.5/dx):int(1/dx+1)]=2
    
    for n in range(nt):
        un=u.copy()
        for i in range(1,nx):
            u[i]=un[i]-dt/dx*c*(un[i]-un[i-1])
    plt.plot(np.linspace(0,2,nx),u)
    
#added a comment in the bottom line
    