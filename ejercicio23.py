# Crear una lista con los números del 1 al 15
numeros = list(range(1, 16))
print("Lista original de números:", numeros)

# Crear una nueva lista con los múltiplos de 3 usando comprensión de listas
multiplos_de_3 = [num for num in numeros if num % 3 == 0]
print("Lista de números múltiplos de 3:", multiplos_de_3)
