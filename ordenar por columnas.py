# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 20:28:01 2021

@author: thor2
"""

import numpy as np
def pivot_col (a,b):
    n=len(a)
    redux=abs(np.array(a))
    redux=np.transpose(redux)#Se saca la matriz transpuesta para hacerlo por columnas
    
    print(redux)
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
    
    
    print(auxr,auxr2)
    
pivot_col([[3,6,4],[1,9,7],[2,3,8]],[3,5,6])