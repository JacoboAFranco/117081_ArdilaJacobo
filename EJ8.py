# -*- coding: utf-8 -*-
#%% EJERCICIO 8 TALLER
''' INICIO '''
#%% FUNCIONES PARA DAR RANGO Y HACER LISTAS

def first_100():
    c100 = []
    for element in range(0,101): #Hasta 101 para que me incluya el 100
         c100.append(element) #Almacenamiento
    return c100

def three_four(c100):
    mthree = [] #Creamos las listas para los multiplos de 3 y de 4
    mfour = []
    for element in c100:
        if 0<element<46: #Los 15 primeros multiplos de 3 llegan hasta el 45
            if element%3 ==0:#por tanto, deben cumplir este rango
                mthree.append(element) #se almacena si cumple rango y multiplo
        if 46<element<101: #Se toma este rango ya que ya se iteró para el 3
            if element%4==0:
                mfour.append(element) #se almacena si cumple rango y multiplos
    return mthree, mfour

#%% SALIDA DE DATOS (LECTURA)
x = first_100()
y = three_four(x)
print(y) #imprimimos

'''FIN'''
