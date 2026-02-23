import java.util.*;

/**
 * Solution to Challenge 007: Graph Cycle Detection.
 * Implementation using DFS with color states.
 */
public class Solucion {
    public boolean hasCycle(int numVertices, int[][] edges) {
        // Build adjacency list
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numVertices; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
        }

        // 0 = not visited, 1 = visiting, 2 = processed
        int[] state = new int[numVertices];

        for (int i = 0; i < numVertices; i++) {
            if (state[i] == 0) {
                if (isCyclicDFS(i, adj, state)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean isCyclicDFS(int u, List<List<Integer>> adj, int[] state) {
        state[u] = 1; // Marking as "processing"

        for (int v : adj.get(u)) {
            if (state[v] == 1) {
                return true; // Found back edge (cycle)
            }
            if (state[v] == 0 && isCyclicDFS(v, adj, state)) {
                return true;
            }
        }

        state[u] = 2; // Marking as "finished"
        return false;
    }
}

/**
 * Complexity Analysis:
 * Time: O(V + E) where V is the number of vertices and E is the number of edges.
 * Space: O(V + E) for the adjacency list and the recursion stack.
 */
