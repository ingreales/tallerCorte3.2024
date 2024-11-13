# Crear una lista con los números del 1 al 25
numeros = list(range(1, 26))
print("Lista original de números:", numeros)


elemento_pos_7 = numeros.pop(7)
print("Elemento eliminado en la posición 7:", elemento_pos_7)
print("Lista después de eliminar el elemento en la posición 7:", numeros)
