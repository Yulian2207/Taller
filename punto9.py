def ordenamiento_insercion_ventas(ventas):
    for i in range(1, len(ventas)):
        valor_actual = ventas[i]
        j = i - 1
        while j >= 0 and ventas[j] > valor_actual:
            ventas[j + 1] = ventas[j]
            j -= 1
        ventas[j + 1] = valor_actual
    return ventas
ventas_diarias = [250, 1200, 6800, 15300, 9700, 20500]
ventas_ordenadas = ordenamiento_insercion_ventas(ventas_diarias)
print("Ventas ordenadas de menor a mayor:", ventas_ordenadas)
