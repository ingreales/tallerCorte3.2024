
# Dos listas con 5 números enteros cada una
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5]

# Multiplicamos los elementos correspondientes
resultado = [a * b for a, b in zip(lista1, lista2)]
print("Resultado de la multiplicación de elementos correspondientes:", resultado)
