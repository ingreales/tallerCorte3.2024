# Crear una lista con los números del 1 al 12
numeros = list(range(1, 13))

# Crear una nueva lista con los cuadrados de cada número
cuadrados = [num ** 2 for num in numeros]
print("Lista de cuadrados de cada número:", cuadrados)
