# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 16:50:58 2021

@author: thor2
"""

import numpy as np
def gradient(x, A, b):
	element_1 = np.dot(np.transpose(A),np.dot(A, x))
	element_2 = np.dot(np.transpose(A), b)
	return element_1 - element_2


def linear(x_sol,A_coef,b_coef,umbral):
    k=.01
    for i in range(1000000):
        x_sol=x_sol-k*gradient(x_sol,A_coef,b_coef)
        a=np.dot(A_coef,x_sol)
        if a[0]<(b_coef[0]+umbral) and a[0]>(b_coef[0]-umbral):
            break
        
    print("El resultado es: ",x_sol,"\n Se requirieron ",i, "iteraciones.")


    
    
linear([1.0, 1.0, 1.0],[[2.0, 1.0, -3.0], [5.0, -4.0, 1.0], [1.0, -1.0, -4.0]],[7.0, -19.0, 4.0],.0000000000001)