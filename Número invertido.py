numero = int(input("Ingresa un número entero: "))

invertido = 0
temp = abs(numero)

while temp > 0:
    digito = temp % 10 
    invertido = invertido * 10 + digito
    temp //= 10 

if numero < 0:
    invertido *= -1

print(f"El número invertido es: {invertido}")
