# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:28:03 2021

@author: thor2
"""

import numpy as np
def pivot_fila (a,b):
    
    n=len(a)
    redux=abs(np.array(a))
    orden=[]
    aux=[]
    for i in range(n-1):
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
    for i in range(n):
        if redux[i]!=0:
            orden.append(i)
    auxr=[]
    for i in orden:
        auxr.append(a[i])
    auxr2=[]
    for i in orden:
        auxr2.append(b[i])
    print(auxr,auxr2)
    return(auxr,auxr2)

    
pivot_fila([[3,8,4],[7,9,7],[2,3,8]],[3,5,6])
