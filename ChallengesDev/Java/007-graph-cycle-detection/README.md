# Challenge 007: Graph Cycle Detection

## Problem Description
Given a directed graph, determine if it contains at least one **cycle**. A cycle in a directed graph is a path that starts and ends at the same vertex, following the direction of the edges.

## Input and Output Format
- **Input**: The number of vertices `numVertices` and an array of edges `int[][] edges`, where `edges[i] = [u, v]` represents a directed edge from `u` to `v`.
- **Output**: A `boolean` value (true if there is a cycle, false otherwise).

## Constraints and Edge Cases
- The graph can be disconnected.
- There can be multiple components.
- Vertices are numbered from `0` to `numVertices - 1`.

## Usage Example
```java
int numVertices = 4;
int[][] edges = {{0, 1}, {1, 2}, {2, 0}, {2, 3}};
// Result: true (Cycle 0->1->2->0)
```

## Key Concepts
- **DFS (Depth First Search)**: Use visiting states to detect back edges.
  - 0: Not visited.
  - 1: Visiting (in the current recursion stack).
  - 2: Visited (fully processed).
- **Kahn's Algorithm**: Cycle detection based on in-degree.
- **Time Complexity**: $O(V + E)$.
