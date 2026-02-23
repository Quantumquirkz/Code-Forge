#include "solucion.cpp"
#include <iostream>
#include <cassert>

int main() {
    MatrixChainOptimizer optimizer;

    // Caso 1
    std::vector<int> p1 = {10, 30, 5, 60};
    assert(optimizer.solve(p1) == 4500);

    // Caso 2
    std::vector<int> p2 = {40, 20, 30, 10, 30};
    assert(optimizer.solve(p2) == 26000);

    // Caso 3: Solo una matriz (dos dimensiones)
    std::vector<int> p3 = {10, 20};
    assert(optimizer.solve(p3) == 0);

    std::cout << "Reto 010 (C++): Matrix Chain Multiplication verificado." << std::endl;
    return 0;
}
 pieces of code.
