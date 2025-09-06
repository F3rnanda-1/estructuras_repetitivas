n = int(input("Ingresa un número n: "))

suma_pares = 0
suma_impares = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i

print(f"La suma de los números pares hasta {n} es: {suma_pares}")
print(f"La suma de los números impares hasta {n} es: {suma_impares}")
