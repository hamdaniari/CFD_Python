# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:27:16 2020

@author: Hamdani
"""

import  numpy as np
import matplotlib.pyplot as plt

lamda = 10 #W/m/K
rho = 2000 #kg/m3
cp = 500 #J/kg/K
L = 0.5 #m
nx = 51
dx = L / (nx-1)
t_sim = 500              #second
dt = 0.5                #second
nt = int(t_sim/dt)+1      #second

x = np.linspace(0, L, nx)

#I.C
T = np.ones(nx)*(30+273.15)
Tn = T.copy()

for n in range(nt+1):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    Tn = T.copy()
    T[1:-1] = T[1:-1] + lamda*dt/(dx**2*rho*cp)*(T[2:]-2*T[1:-1]+T[0:-2])
    
    
    T[0] = (20+273.15)
    T[-1] = T[-2]
    
plt.plot(x, T-273.15)