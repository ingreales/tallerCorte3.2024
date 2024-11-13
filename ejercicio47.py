# Lista con nombres de monumentos colombianos
monumentos = ["Cristo Rey", "La Popa", "Monserrate", "Santuario de Las Lajas", "La Piedra del Peñol", 
              "Puente de Boyacá", "Plaza de Bolívar"]

monumentos.sort(key=lambda x: len(x))
print("Lista de monumentos ordenada por longitud de nombre:", monumentos)
