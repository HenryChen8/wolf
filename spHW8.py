#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 09:00:51 2018

@author: Henry
"""

import pylab as plt
import numpy as np

a_s=1
a_f=2
m=1
a1=1
a2=3

def w2(kx,ky):
    ww=4/m*a_s*(np.sin(kx*a1/2)**2)+4/m*a_f*(np.sin(ky*a2/2)**2)
    return ww**0.5
def w22(kx,ky):
    ww=4/m*a_f*(np.sin(kx*a1/2)**2)+4/m*a_s*(np.sin(ky*a2/2)**2)
    return ww**0.5

x1=np.linspace(0.,np.pi/a1,100)
x2=np.linspace(0.,np.pi/a2,100)
x3=np.linspace(np.pi/a1,0.,100)
x4=np.linspace(np.pi/a2,0.,100)
x=[[],[],[],[],[],[],[],[]]
y=[[],[],[],[],[],[],[],[]]

for i in x1:
    y[0].append(w2(i,0.))
    y[4].append(w22(i,0.))
for i in x2:
    y[1].append(w2(np.pi/a1,i))
    y[5].append(w22(np.pi/a1,i))
for i in x3:
    y[2].append(w2(i,np.pi/a2))
    y[6].append(w22(i,np.pi/a2))
for i in x4:
    y[3].append(w2(0.,i))
    y[7].append(w22(0.,i))
r =np.linspace(0.,np.pi/a1,100)
r1=np.linspace(   np.pi/a1         ,   np.pi/a1+   np.pi/a2,100)
r2=np.linspace(   np.pi/a1+np.pi/a2,2.*np.pi/a1+   np.pi/a2,100)
r3=np.linspace(2.*np.pi/a1+np.pi/a2,2.*np.pi/a1+2.*np.pi/a2,100)
for i in r:
    x[0].append(i)
    x[4].append(i)
for i in r1:
    x[1].append(i)
    x[5].append(i)
for i in r2:
    x[2].append(i)
    x[6].append(i)
for i in r3:
    x[3].append(i)
    x[7].append(i)


plt.plot(x[0],y[0],'b')
plt.plot(x[1],y[1],'b')
plt.plot(x[2],y[2],'b')
plt.plot(x[3],y[3],'b')
plt.plot(x[4],y[4],'r')
plt.plot(x[5],y[5],'r')
plt.plot(x[6],y[6],'r')
plt.plot(x[7],y[7],'r')