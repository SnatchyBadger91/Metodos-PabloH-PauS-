# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 12:10:27 2021

@author: thor2
"""

import numpy as np
def pivot_fila (a,b):
    n=len(a)
    redux=abs(np.array(a))
    orden=[]
    aux=[]
    for i in range(n):
        for k in range(n):
            if redux[k][0]!=0:   
               aux.append(redux[k][0]/max(redux[k]))
            if redux[k][0]==0:
                aux.append(0)
        q= np.where(aux==max(aux))
        t = ''.join(map(str, q))
        t=eval(t)
        orden.append(t[0]) 
        aux.clear()
        redux[q]=0
        redux=redux.tolist()
        for k in range(len(redux)):
            del redux[k][0]
        redux=np.array(redux)
    auxr=[]
    for i in orden:
        auxr.append(a[i])
    auxr2=[]
    for i in orden:
        auxr2.append(b[i])
    return(auxr,auxr2)

def pivot_col (a,b):
    n=len(a)
    redux=abs(np.array(a))
    redux=np.transpose(redux)#Se saca la matriz transpuesta para hacerlo por columnas
    orden=[]
    aux=[]
    for i in range(n):
        for k in range(n):
            if redux[k][0]!=0:   
               aux.append(redux[k][0]/max(redux[k]))
            if redux[k][0]==0:
                aux.append(0)
        q= np.where(aux==max(aux))
        t = ''.join(map(str, q))
        t=eval(t)
        orden.append(t[0]) 
        aux.clear()
        redux[q]=0
        redux=redux.tolist()
        for k in range(len(redux)):
            del redux[k][0]
        redux=np.array(redux)
    auxr=[]
    for i in orden:
        auxr.append(a[i])
    auxr2=[]
    for i in orden:
        auxr2.append(b[i])
    return(auxr,auxr2)


def Gauss_Seidel_numpy (matriz,resultados):
    print("Se aplico el método Gauss-Seidel con numpy\n")
    m_np,r_np=pivot_fila(matriz,resultados)
    m_np=np.array(m_np)
    r_np=np.array(r_np)
    x=np.array([0.0 for i in range(len(matriz))])
    aux=np.array([1.0 for i in range(len(matriz))])
    for i in range(len(matriz)-1):
        if len(matriz[i]) != len(matriz[i+1]):
            print("\n Solo se aceptan matrices cuadradas.")
            return
        if len(matriz) != len(resultados):
            print("Verifique que tiene la misma cantidad de ecuaciones que de resultados")
            return
    for ite in range(10000):
        for i in range(len(matriz)):
            aux[i]=0.0
            x[i] = (r_np[i] - np.sum(x*aux*m_np[i,:]))/m_np[i][i]
            aux[i]=1
        r_act = np.dot(m_np,x)
        result = np.sum(np.abs(r_act-r_np))
        if result==0:
            break
    for i in range(len(matriz)):
        print("x_",i+1,"=",x[i],"\n")
        
Gauss_Seidel_numpy([[3,8,4],[7,9,7],[2,3,8]],[3,5,6])
