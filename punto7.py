def ordenamiento_insercion_descendente(puntuaciones):
    for i in range(1, len(puntuaciones)):
        valor_actual = puntuaciones[i]
        j = i - 1
        while j >= 0 and puntuaciones[j] < valor_actual:
            puntuaciones[j + 1] = puntuaciones[j]
            j -= 1
        puntuaciones[j + 1] = valor_actual 
    return puntuaciones
puntuaciones = [1582, 2223, 1815, 2469, 2000, 1718]
puntuaciones_ordenadas = ordenamiento_insercion_descendente(puntuaciones)
print("Puntuaciones ordenadas de mayor a menor:", puntuaciones_ordenadas)