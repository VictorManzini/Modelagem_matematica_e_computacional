import numpy as np
import matplotlib.pyplot as plt

#Aula sobre arrays e funções f(x)
#o ipynb desta aula é o Aula_1s_03_Função.ipynb 
#Primeiros exemplos de arrays 

a = np.array([0.1, 0.2, 0.3, 0.4, 0.5]) #Matriz linha 
print(a)
print('Dimension:', a.ndim)
print('Shape', a.shape)
print('Size:', a.size)

b = np.array([[1,2,3,4,5]])
print(b)
print('Dimension:', b.ndim)
print('Shape:', b.shape)
print('Size:', b.size)

'''
a = 3
b = 9
c = 2

def Delta(a,b,c):
    return b**2 - 4*a*c
'''

