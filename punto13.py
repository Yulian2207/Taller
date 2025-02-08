import random
def mergesort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]
    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)
    return merge(izquierda, derecha)
def merge(izquierda, derecha):
    lista_ordenada = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            lista_ordenada.append(izquierda[i])
            i += 1
        else:
            lista_ordenada.append(derecha[j])
            j += 1
    lista_ordenada.extend(izquierda[i:])
    lista_ordenada.extend(derecha[j:])
    return lista_ordenada
numeros_aleatorios = [random.randint(1, 100) for _ in range(20)]
numeros_ordenados = mergesort(numeros_aleatorios)
print("Lista de números aleatorios:", numeros_aleatorios)
print("Lista ordenada con mergesort:", numeros_ordenados)