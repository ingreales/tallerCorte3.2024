# Crear una lista con los números del 1 al 20
numeros = list(range(1, 21))

# Crear una nueva lista con los cuadrados de los números pares
cuadrados_pares = [num ** 2 for num in numeros if num % 2 == 0]
print("Lista de cuadrados de números pares:", cuadrados_pares)
