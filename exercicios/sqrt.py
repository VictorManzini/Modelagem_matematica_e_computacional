import math 

#com o int(math.sqrt()) ele vai printar o resultado da raíz como um numero inteiro, sem decimal
numero = 9
sqrt = int(math.sqrt(numero))
print(sqrt) 

#printa o resulado da raíz com o decimal, como se tivesse um float antes do math.sqrt()
numero = 9
sqrt = math.sqrt(numero)
print(sqrt) 