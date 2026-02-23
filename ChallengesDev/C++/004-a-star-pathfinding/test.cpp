#include "solucion.cpp"
#include <iostream>
#include <cassert>

int main() {
    AStar solver;
    vector<vector<int>> grid = {
        {0, 0, 0, 0},
        {1, 1, 0, 1},
        {0, 0, 0, 0}
    };
    pair<int, int> start = {0, 0};
    pair<int, int> goal = {2, 0};

    vector<pair<int, int>> path = solver.findPath(grid, start, goal);

    assert(!path.empty());
    assert(path.front() == start);
    assert(path.back() == goal);

    std::cout << "Reto 004 (C++): A* Pathfinding verificado." << std::endl;
    return 0;
}
