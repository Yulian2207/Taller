import heapq
from datetime import datetime
def heapsort_por_caducidad(productos):
    heap = [] 
    for producto in productos:
        heapq.heappush(heap, (producto['fecha_caducidad'], producto))
    productos_ordenados = []
    while heap:
        fecha, producto = heapq.heappop(heap)
        productos_ordenados.append(producto)  
    return productos_ordenados
productos = [
    {'nombre': 'Leche', 'fecha_caducidad': datetime(2025, 2, 10).date()},
    {'nombre': 'Papitas', 'fecha_caducidad': datetime(2025, 1, 15).date()},
    {'nombre': 'Pan', 'fecha_caducidad': datetime(2025, 2, 5).date()},
    {'nombre': 'Mantequilla', 'fecha_caducidad': datetime(2025, 3, 1).date()},
    {'nombre': 'Queso', 'fecha_caducidad': datetime(2025, 1, 30).date()}
]
productos_ordenados = heapsort_por_caducidad(productos)
for producto in productos_ordenados:
    print(f'{producto["nombre"]} - {producto["fecha_caducidad"]}')