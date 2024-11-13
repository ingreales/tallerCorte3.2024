# Lista inicial con números del 1 al 10
numeros = list(range(1, 11))
print("Lista original de números:", numeros)

# Segunda lista con números del 11 al 15
nuevos_numeros = list(range(11, 16))

# Usar .extend() para agregar la segunda lista
numeros.extend(nuevos_numeros)
print("Lista de números después de extender con otra lista:", numeros)
