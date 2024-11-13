# Lista de números enteros
numeros = list(range(1, 11))
print("Lista original de números:", numeros)

# Usar un bucle while para eliminar los elementos impares
i = 0
while i < len(numeros):
    if numeros[i] % 2 != 0:
        numeros.pop(i)
    else:
        i += 1
print("Lista después de eliminar los números impares:", numeros)
