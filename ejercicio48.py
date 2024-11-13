# Crear una lista con los números del 1 al 18
numeros = list(range(1, 19))

multiplos_3_y_5 = [num for num in numeros if num % 3 == 0 and num % 5 == 0]
print("Lista de números múltiplos de 3 y 5:", multiplos_3_y_5)
