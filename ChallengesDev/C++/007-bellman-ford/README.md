# Challenge 007: Bellman-Ford Algorithm

## Problem Description
Implement the **Bellman-Ford** algorithm to find the shortest paths from a single source node to all other nodes in a graph that may contain edges with negative weights. Additionally, the algorithm must be able to detect if there is a **negative weight cycle** reachable from the source.

## Input and Output Format
- **Input**: 
  - The number of vertices `V`.
  - A list of edges `vector<Edge> edges`, where each has `src`, `dest`, and `weight`.
  - A source vertex `src`.
- **Output**: A `vector<int>` with the minimum distances, or an empty vector if a negative cycle is detected.

## Constraints and Edge Cases
- $1 \le V \le 1000$.
- Weights can be negative.
- Use `INT_MAX` to represent infinite distances.

## Usage Example
```cpp
V = 5, src = 0;
edges = {{0, 1, -1}, {0, 2, 4}, {1, 2, 3}, {1, 3, 2}, {1, 4, 2}, {3, 2, 5}, {3, 1, 1}, {4, 3, -3}};
// Result: distances from 0: [0, -1, 2, -2, 1]
```

## Key Concepts
- **Relaxation**: Attempting to improve the estimated distance to a node `v` through an edge `(u, v)`.
- **Negative Cycles**: A cycle whose edge weights sum to a negative value. It prevents finding the "shortest path" as it can be reduced indefinitely.
- **Time Complexity**: $O(V \times E)$.
