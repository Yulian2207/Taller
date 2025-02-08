def buble_sort (calificaciones):
    n = len(calificaciones)
    for i in range (n):
        for j in range (0, n - i - 1):
            if calificaciones [j] > calificaciones [j + 1]:
                calificaciones [j], calificaciones [j + 1] = calificaciones [j + 1], calificaciones [j]
    return calificaciones
calificaciones  = [85, 92, 65, 89, 70, 90]
print ("Calificaciones ordenadas:", buble_sort(calificaciones))
       