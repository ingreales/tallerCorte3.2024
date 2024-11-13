# Lista con nombres de deportes
deportes = ["Fútbol", "Baloncesto", "Tenis", "Natación", "Ciclismo", "Voleibol", "Atletismo", "Boxeo"]
print("Lista original de deportes:", deportes)

# Ordenar la lista usando una función lambda
deportes.sort(key=lambda x: x)
print("Lista de deportes ordenada alfabéticamente:", deportes)
