def ordenamiento_burbuja_precios(precios):
    n = len(precios)
    for i in range(n):
        for j in range(0, n-i-1):
            if precios[j] > precios[j+1]:
                precios[j], precios[j+1] = precios[j+1], precios[j]
    return precios
precios = [120500, 50999, 8000, 150750, 94100, 20450]
precios_ordenados = ordenamiento_burbuja_precios(precios)
print("Precios ordenados ascendentemente:", precios_ordenados)