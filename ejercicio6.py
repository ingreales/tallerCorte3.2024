# Borrar el último elemento de la lista concatenada

frutas = ["Mango", "Guayaba", "Piña", "Banano", "Papaya"]
print("Lista de frutas:", frutas)


numeros = list(range(1, 11))
print("Lista de números:", numeros)
print("Longitud de la lista:", len(numeros))


lista_concatenada = frutas + numeros
print("Lista concatenada:", lista_concatenada)


lista_concatenada.pop()
print("Lista después de borrar el último elemento:", lista_concatenada)
