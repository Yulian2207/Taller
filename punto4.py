def ordenamiento_burbuja_tiempos(tiempos):
    n = len(tiempos)
    for i in range(n):
        for j in range(0, n-i-1):
            if tiempos[j] > tiempos[j+1]:
                tiempos[j], tiempos[j+1] = tiempos[j+1], tiempos[j]
    return tiempos
tiempos = [360, 420, 300, 540, 390, 480]
tiempos_ordenados = ordenamiento_burbuja_tiempos(tiempos)
print("Tiempos ordenados de menor a mayor:", tiempos_ordenados)