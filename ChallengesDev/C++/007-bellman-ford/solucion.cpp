#include <vector>
#include <climits>

struct Edge {
    int src, dest, weight;
};

/**
 * Implementation of the Bellman-Ford algorithm.
 */
class BellmanFord {
public:
    std::vector<int> shortestPath(int V, const std::vector<Edge>& edges, int src) {
        std::vector<int> dist(V, INT_MAX);
        dist[src] = 0;

        // Step 1: Relax all edges V - 1 times
        for (int i = 1; i <= V - 1; i++) {
            for (const auto& edge : edges) {
                if (dist[edge.src] != INT_MAX && dist[edge.src] + edge.weight < dist[edge.dest]) {
                    dist[edge.dest] = dist[edge.src] + edge.weight;
                }
            }
        }

        // Step 2: Check for negative weight cycles
        for (const auto& edge : edges) {
            if (dist[edge.src] != INT_MAX && dist[edge.src] + edge.weight < dist[edge.dest]) {
                // Negative cycle detected
                return {}; 
            }
        }

        return dist;
    }
};

/**
 * Complexity Analysis:
 * Time: O(V * E) where V is the number of vertices and E is the number of edges.
 * Space: O(V) to store distances.
 */
