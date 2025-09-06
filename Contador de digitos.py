numero = int(input("Ingresa un número entero: "))
contador = 0
if numero == 0:
    contador = 1
else:
    numero = abs(numero)
    
    while numero > 0:
        numero //= 10
        contador += 1
print("El número tiene", contador, "dígitos.")
