# Crear una lista con los números del 1 al 25
numeros = list(range(1, 26))
print("Lista original de números:", numeros)

# Crear una nueva lista con los múltiplos de 5 usando una comprensión de listas
multiplos_de_5 = [num for num in numeros if num % 5 == 0]
print("Lista de números múltiplos de 5:", multiplos_de_5)
