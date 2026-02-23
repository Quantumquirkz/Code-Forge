#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

struct Node {
    int x, y;
    int g, h;
    pair<int, int> parent;

    int f() const { return g + h; }
};

struct CompareNode {
    bool operator()(const Node& a, const Node& b) {
        return a.f() > b.f();
    }
};

class AStar {
private:
    int heuristic(int x1, int y1, int x2, int y2) {
        return abs(x1 - x2) + abs(y1 - y2);
    }

public:
    vector<pair<int, int>> findPath(const vector<vector<int>>& grid, pair<int, int> start, pair<int, int> goal) {
        int rows = grid.size();
        int cols = grid[0].size();

        priority_queue<Node, vector<Node>, CompareNode> openSet;
        map<pair<int, int>, pair<int, int>> parentMap;
        map<pair<int, int>, int> gScore;

        openSet.push({start.first, start.second, 0, heuristic(start.first, start.second, goal.first, goal.second), {-1, -1}});
        gScore[start] = 0;

        int dx[] = {0, 0, 1, -1};
        int dy[] = {1, -1, 0, 0};

        while (!openSet.empty()) {
            Node current = openSet.top();
            openSet.pop();

            if (current.x == goal.first && current.y == goal.second) {
                // Reconstruct path
                vector<pair<int, int>> path;
                pair<int, int> curr = goal;
                while (curr.first != -1) {
                    path.push_back(curr);
                    curr = parentMap[curr];
                }
                reverse(path.begin(), path.end());
                return path;
            }

            for (int i = 0; i < 4; i++) {
                int nx = current.x + dx[i];
                int ny = current.y + dy[i];

                if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && grid[nx][ny] == 0) {
                    int tentG = current.g + 1;
                    if (gScore.find({nx, ny}) == gScore.end() || tentG < gScore[{nx, ny}]) {
                        gScore[{nx, ny}] = tentG;
                        parentMap[{nx, ny}] = {current.x, current.y};
                        openSet.push({nx, ny, tentG, heuristic(nx, ny, goal.first, goal.second), {current.x, current.y}});
                    }
                }
            }
        }
        return {};
    }
};
