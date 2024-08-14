def S(n):
    return n + 1

def suma(a, b):
    resultado = a
    for _ in range(b):
        resultado = S(resultado)
    return resultado

def resta(a, b):
    resultado = a
    for _ in range(b):
        resultado = resultado - 1
    return resultado


print(suma(2, 8))  
print(suma(97, 5))  
print(resta(123, 45))  
print(resta(38, 23))  