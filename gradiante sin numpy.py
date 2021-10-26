# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:29:02 2021

@author: thor2
"""
import numpy as np

def producto (A_1,x_1):
    resultado=[]
    for i in range(len(A_1)):
        aux=0
        for j in range(len(A_1)):
            aux+=x_1[j]*A_1[i][j]
        resultado.append(aux)
    return(resultado)

def trans(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_T = []
    for i in range(columnas):
        fila_res = []
        for j in range(filas):
           fila_res.append(matriz[j][i])
        matriz_T.append(fila_res)

    return matriz_T

def gradiante (x,A,b):
    elemento_1=producto(trans(A),producto(A,x))
    elemento_2=producto(trans(A),b)
    resultado=[]
    for i in range(len(elemento_1)):
        resultado.append(elemento_1[i]-elemento_2[i])
    resultado=np.array(resultado)
    return resultado

def linear(x_sol,A_coef,b_coef,umbral):
    k=.01
    for i in range(100000000):
        x_sol=x_sol-k*gradiante(x_sol,A_coef,b_coef)
        a=producto(A_coef,x_sol)
        if a[0]<(b_coef[0]+umbral) and a[0]>(b_coef[0]-umbral):
            break
        
    print("El resultado es: ",x_sol,"\n Se requirieron ",i, "iteraciones.")


    
    
linear([1.0, 1.0, 1.0],[[2.0, 1.0, -3.0], [5.0, -4.0, 1.0], [1.0, -1.0, -4.0]],[7.0, -19.0, 4.0],.00000000000001)
