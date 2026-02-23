import heapq
from typing import Dict, List, Tuple, Optional

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
    """
    Calcula el camino más corto en un grafo pesado usando el algoritmo de Dijkstra.
    
    Args:
        graph: Diccionario donde las claves son nodos y valores son listas de (vecino, peso).
        start: Nodo inicial.
        
    Returns:
        Tuple: (distancias, padres) para reconstrucción de caminos.
    """
    # Inicializar distancias como infinito y padres como None
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parents = {node: None for node in graph}
    
    # Priority Queue: (distancia_acumulada, nodo_actual)
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Si ya encontramos un camino más corto a este nodo, saltar
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Relajación de la arista
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
                
    return distances, parents

def reconstruct_path(parents: Dict[int, Optional[int]], target: int) -> List[int]:
    """Reconstruye el camino desde el inicio hasta el objetivo."""
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = parents[curr]
    return path[::-1]

# --- Análisis de Complejidad ---
# Temporal: O((V + E) log V)
#   - Cada nodo se extrae del heap una vez: O(V log V)
#   - Cada arista se relaja una vez y puede provocar un push al heap: O(E log V)
# Espacial: O(V + E)
#   - Almacenamos distancias, padres y el grafo en memoria.
