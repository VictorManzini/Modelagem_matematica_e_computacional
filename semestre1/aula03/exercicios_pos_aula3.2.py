#calcular o ∆ de uma equação de 2º grau

print("Calculadora de equaçãode 2º grau")

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

def calcular_delta(a,b,c): 
    delta = b**2 - 4*a*c
    return delta

result = calcular_delta(a, b, c)
print(f"O valor de ∆ é: {result}")