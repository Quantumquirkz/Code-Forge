# Challenge 004: A* Pathfinding

## Problem Description
Implement the **A*** (A-Star) pathfinding algorithm to find the shortest path between two points in a 2D grid. The algorithm must consider obstacles and use a heuristic function to optimize the search.

## Input and Output Format
- **Input**: 
  - A grid `vector<vector<int>> grid` where `0` is traversable and `1` is an obstacle.
  - Start point `pair<int, int> start` and goal point `pair<int, int> goal`.
- **Output**: A list of coordinates `vector<pair<int, int>>` representing the shortest path, or an empty list if no route exists.

## Constraints and Edge Cases
- Allowed movement: Up, Down, Left, Right (4 directions).
- Suggested heuristic: Manhattan Distance.
- The grid can be up to $100 \times 100$.

## Usage Example
```cpp
grid = {{0, 0, 0}, {1, 1, 0}, {0, 0, 0}};
start = {0, 0}, goal = {2, 0};
// Result: {(0,0), (0,1), (0,2), (1,2), (2,2), (2,1), (2,0)}
```

## Key Concepts
- **Priority Queue**: To always explore the node with the lowest estimated total cost $f(n) = g(n) + h(n)$.
- **$g(n)$**: Actual cost from the start to node $n$.
- **$h(n)$**: Estimated cost (heuristic) from $n$ to the goal.
- **Time Complexity**: $O(E \log V)$ in the worst case, but much more efficient with a good heuristic.
