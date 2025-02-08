def ordenamiento_seleccion_salarios(salarios):
    for i in range(len(salarios)):
        indice_minimo = i
        for j in range(i + 1, len(salarios)):
            if salarios[j] < salarios[indice_minimo]:
                indice_minimo = j
        salarios[i], salarios[indice_minimo] = salarios[indice_minimo], salarios[i]
    return salarios
salarios = [3500000, 2800000, 1650000, 3150000, 2500000, 3980000]
salarios_ordenados = ordenamiento_seleccion_salarios(salarios)
print("Salarios ordenados de menor a mayor:", salarios_ordenados)