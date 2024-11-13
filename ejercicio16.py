# Lista del ejercicio 4 (concatenación de las listas de frutas y números del 1 al 10)
frutas = ["Lulo", "Mango", "Guanábana", "Guayaba", "Maracuyá"]
numeros = list(range(1, 11))
lista_concatenada = frutas + numeros
print("Lista concatenada original:", lista_concatenada)


ultimo_elemento = lista_concatenada.pop()
print("Último elemento eliminado de la lista concatenada:", ultimo_elemento)
print("Lista concatenada después de eliminar el último elemento:", lista_concatenada)
