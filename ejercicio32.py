# Crear una lista con los números del 1 al 15
numeros = list(range(1, 16))

# Crear una nueva lista con los números impares
numeros_impares = [num for num in numeros if num % 2 != 0]
print("Lista de números impares:", numeros_impares)
