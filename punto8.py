def ordenamiento_insercion_palabra(palabra):
    caracteres = list(palabra)
    for i in range(1, len(caracteres)):
        valor_actual = caracteres[i]
        j = i - 1
        while j >= 0 and caracteres[j] > valor_actual:
            caracteres[j + 1] = caracteres[j]
            j -= 1
        caracteres[j + 1] = valor_actual
    return ''.join(caracteres)
palabra = "esternocleidomastoideo"
palabra_ordenada = ordenamiento_insercion_palabra(palabra)
print("Palabra ordenada alfabéticamente:", palabra_ordenada)