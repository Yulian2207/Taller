def ordenamiento_burbuja_por_longitud(nombres):
    n = len(nombres)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(nombres[j]) > len(nombres[j+1]):
                nombres[j], nombres[j+1] = nombres[j+1], nombres[j]  
    return nombres
nombres = ["Ana", "Marlon", "Yulian", "Santiago", "Juan", "Arnoldo"]
nombres_ordenados = ordenamiento_burbuja_por_longitud(nombres)

print("Nombres ordenados por longitud:", nombres_ordenados)