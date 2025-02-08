def ordenamiento_insercion_edades(edades):
    for i in range(1, len(edades)):
        valor_actual = edades[i]
        j = i - 1
        while j >= 0 and edades[j] > valor_actual:
            edades[j + 1] = edades[j]
            j -= 1
        edades[j + 1] = valor_actual 
    return edades
edades = [25, 18, 30, 22, 27, 19, 35]
edades_ordenadas = ordenamiento_insercion_edades(edades)
print("Edades ordenadas de menor a mayor:", edades_ordenadas)