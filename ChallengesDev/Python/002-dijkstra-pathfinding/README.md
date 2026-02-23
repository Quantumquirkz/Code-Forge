# Challenge 002: Dijkstra Pathfinding

## Problem Description
Implement **Dijkstra's algorithm** to find the shortest path between a starting node and all others in a directed graph with non-negative weights. The algorithm must be efficient and return both the minimum distances and the path to reach each node.

## Input and Output Format
- **Input**: 
  - A graph represented as an adjacency list: `Dict[int, List[Tuple[int, int]]]` (source_node: [(target_node, weight)]).
  - An integer `start` representing the starting node.
- **Output**:
  - A dictionary with the minimum distance to each node.
  - A dictionary with the "parent" node to reconstruct the path.

## Constraints and Edge Cases
- Weights are always non-negative ($\ge 0$).
- The graph can be disconnected (distance = infinity).
- Optimization with a **Priority Queue** (Min-Heap) is mandatory to achieve $O(E \log V)$.

## Usage Example
```python
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
distances, parents = dijkstra(graph, 0)
# distances[3] -> 4 (0 -> 2 -> 1 -> 3)
```

## Key Concepts
- **Priority Queue (Heapq)**: To always select the node with the minimum accumulated distance.
- **Edge Relaxation**: The process of updating the distance to a node if we find a shorter path through a neighbor.
- **Time Complexity**: $O((V+E) \log V)$ using a Binomial Heap.
