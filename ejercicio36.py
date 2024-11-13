# Crear una lista con los números del 1 al 12
numeros = list(range(1, 13))

# Crear una nueva lista con los números divisibles por 3
divisibles_por_3 = [num for num in numeros if num % 3 == 0]
print("Lista de números divisibles por 3:", divisibles_por_3)
