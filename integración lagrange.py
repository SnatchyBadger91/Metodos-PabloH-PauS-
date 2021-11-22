# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 10:44:37 2021

@author: thor2
"""
import math as mt
from functools import reduce
import numpy as np

def normal_den(x):
	return (1/mt.sqrt(2*mt.pi))*mt.exp(-0.5*mt.pow(x, 2))

# Asignar valores, (inicio,final,#términos) el # de términos debe de ser mayor a 3 e impar.
tamaño=15
x_c = np.linspace(-4,1,tamaño)
y_c = [normal_den(i) for i in x_c]

def lagrange_basis(x, idx, x_at):
    res_1=reduce(lambda x, y: x*y,[(x_at - j)/(x[idx] - j) for i,j in enumerate(x) if idx != i]) 
    return res_1

def lagrange(x, y, x_at):
    res=sum([j*lagrange_basis(x, i, x_at) for i,j in enumerate(y)])
    return res

def poli_lagrange(yeval):
    a=np.array([[1,1,1],[4,2,1],[9,3,1]])
    b=np.array(yeval)
    x=np.linalg.solve(a,b)
    return x
    
    
aux_x=[]
aux_y=[]
result=0
for i in range(0,len(x_c)-2,2):
    aux_x=[x_c[i],x_c[i+1],x_c[i+2]]
    aux_y=[y_c[i],y_c[i+1],y_c[i+2]]
    y_eval=[lagrange(aux_x,aux_y,l+1)for l in range(3)]
    poli=poli_lagrange(y_eval)
    poli=poli.tolist()
    evalmin=((poli[0]*mt.pow(aux_x[0],3)/3)+(poli[1]*mt.pow(aux_x[0],2)/2)+(poli[2]*aux_x[0]))
    evalmax=((poli[0]*mt.pow(aux_x[2],3)/3)+(poli[1]*mt.pow(aux_x[2],2)/2)+(poli[2]*aux_x[2]))
    integral=evalmax-evalmin
    result+=integral
    
print(result, " Se requirieron: ",tamaño," puntos.")
    
    




