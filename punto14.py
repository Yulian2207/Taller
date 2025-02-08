def shell_sort_descendente(nombres):
    n = len(nombres)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            valor_actual = nombres[i]
            j = i
            while j >= intervalo and nombres[j - intervalo] < valor_actual:
                nombres[j] = nombres[j - intervalo]
                j -= intervalo
            nombres[j] = valor_actual
        intervalo //= 2
    return nombres
nombres = ["Juan", "Santiago", "Yulian", "Gustavo", "Fabiolo", "Messi", "Cristiano"]
nombres_ordenados = shell_sort_descendente(nombres)
print("Nombres ordenados en orden alfabético inverso:", nombres_ordenados)