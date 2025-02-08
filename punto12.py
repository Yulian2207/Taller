def quicksort(puntajes):
    if len(puntajes) <= 1:
        return puntajes
    else:
        pivote = puntajes[0]
        menores = [x for x in puntajes[1:] if x < pivote]
        mayores = [x for x in puntajes[1:] if x > pivote]
        iguales = [x for x in puntajes[1:] if x == pivote]
        return quicksort(menores) + [pivote] + iguales + quicksort(mayores)
puntajes_deportivos = [85.3, 92.0, 78.5, 88.3, 76.1, 95.0, 90.9, 81.5]
puntajes_ordenados = quicksort(puntajes_deportivos)
print("Puntajes ordenados de menor a mayor:", puntajes_ordenados)