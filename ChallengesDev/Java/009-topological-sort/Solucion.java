import java.util.*;

/**
 * Solution to Challenge 009: Topological Sort.
 * Implementation using Kahn's Algorithm (BFS).
 */
public class Solucion {
    public int[] findOrder(int numTasks, int[][] prerequisites) {
        int[] inDegree = new int[numTasks];
        List<List<Integer>> adj = new ArrayList<>();
        
        for (int i = 0; i < numTasks; i++) {
            adj.add(new ArrayList<>());
        }
        
        // Build graph and calculate in-degrees
        for (int[] pre : prerequisites) {
            adj.get(pre[0]).add(pre[1]);
            inDegree[pre[1]]++;
        }
        
        // Queue for nodes with in-degree 0
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numTasks; i++) {
            if (inDegree[i] == 0) {
                queue.add(i);
            }
        }
        
        int[] result = new int[numTasks];
        int index = 0;
        
        while (!queue.isEmpty()) {
            int u = queue.poll();
            result[index++] = u;
            
            for (int v : adj.get(u)) {
                inDegree[v]--;
                if (inDegree[v] == 0) {
                    queue.add(v);
                }
            }
        }
        
        // If we couldn't process all nodes, there is a cycle
        if (index != numTasks) {
            return new int[0];
        }
        
        return result;
    }
}

/**
 * Complexity Analysis:
 * Time: O(V + E) where V is the number of tasks and E is the number of prerequisites.
 * Space: O(V + E) for the adjacency list and the in-degree array.
 */
