# Crear una lista con los números del 1 al 20
numeros = list(range(1, 21))

# Crear una nueva lista con solo los números pares
numeros_pares = [num for num in numeros if num % 2 == 0]
print("Lista de números pares:", numeros_pares)
