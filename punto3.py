def ordenamiento_burbuja_temperaturas(temperaturas):
    n = len(temperaturas)
    for i in range(n):
        for j in range(0, n-i-1):
            if temperaturas[j] < temperaturas[j+1]:
                temperaturas[j], temperaturas[j+1] = temperaturas[j+1], temperaturas[j] 
    return temperaturas
temperaturas = [22.5, 18.2, 24.1, 19.0, 21.8, 25.3, 20.6]
temperaturas_ordenadas = ordenamiento_burbuja_temperaturas(temperaturas)
print("Temperaturas ordenadas de mayor a menor:", temperaturas_ordenadas)