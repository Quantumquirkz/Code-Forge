# Challenge 009: Topological Sort

## Problem Description
Given a list of tasks with dependencies between them (represented as a Directed Acyclic Graph or DAG), return a valid order to perform all tasks. If there are multiple solutions, any will be accepted. If the graph contains cycles, return an empty array.

## Input and Output Format
- **Input**: The number of tasks `numTasks` and an array of prerequisites `int[][] prerequisites`, where `prerequisites[i] = [u, v]` indicates that task `u` must be done before task `v`.
- **Output**: An integer array `int[]` with the task order.

## Constraints and Edge Cases
- $1 \le \text{numTasks} \le 2000$.
- $0 \le \text{prerequisites.length} \le 5000$.
- Handle cases with disconnected graphs.

## Usage Example
```java
int numTasks = 4;
int[][] prerequisites = {{1, 0}, {2, 0}, {3, 1}, {3, 2}};
// A valid order: [3, 2, 1, 0] or [3, 1, 2, 0]
```

## Key Concepts
- **Kahn's Algorithm**: Uses a queue and tracks the "in-degree" of each node.
- **In-degree**: Number of edges pointing to a node.
- **Time Complexity**: $O(V + E)$.
