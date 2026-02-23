#include <iostream>
#include <cassert>
#include "solucion.cpp"

void testBST() {
    BST tree;

    // Test Inserción y Búsqueda
    tree.insert(50);
    tree.insert(30);
    tree.insert(20);
    tree.insert(40);
    tree.insert(70);
    tree.insert(60);
    tree.insert(80);

    assert(tree.search(50) == true);
    assert(tree.search(20) == true);
    assert(tree.search(90) == false);

    // Test Eliminación
    tree.remove(20); // Caso: Hoja
    assert(tree.search(20) == false);

    tree.remove(30); // Caso: Un hijo
    assert(tree.search(30) == false);
    assert(tree.search(40) == true);

    tree.remove(50); // Caso: Dos hijos
    assert(tree.search(50) == false);
    assert(tree.search(60) == true);
    assert(tree.search(70) == true);

    std::cout << "All C++ tests passed!" << std::endl;
}

int main() {
    testBST();
    return 0;
}
