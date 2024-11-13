# Lista del ejercicio 4 (concatenación de las listas de frutas y números del 1 al 10)
frutas = ["Mango", "Guayaba", "Piña", "Banano", "Papaya"]
numeros = list(range(1, 11))
lista_concatenada = frutas + numeros
print("Lista concatenada original:", lista_concatenada)


if 100 in lista_concatenada:
    indice = lista_concatenada.index(100)
    print("Índice del elemento 100 en la lista concatenada:", indice)
else:
    print("El elemento 100 no se encuentra en la lista concatenada.")
