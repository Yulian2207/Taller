def ordenamiento_insercion_distancias(distancias):
    for i in range(1, len(distancias)):
        valor_actual = distancias[i]
        j = i - 1
        while j >= 0 and distancias[j] > valor_actual:
            distancias[j + 1] = distancias[j]
            j -= 1
        distancias[j + 1] = valor_actual
    return distancias
distancias = [523, 158, 300, 1032, 765, 485]
distancias_ordenadas = ordenamiento_insercion_distancias(distancias)
print("Distancias ordenadas de menor a mayor:", distancias_ordenadas)