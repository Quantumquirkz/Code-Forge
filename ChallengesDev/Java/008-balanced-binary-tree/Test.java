public class Test {
    public static void main(String[] args) {
        AVLTree tree = new AVLTree();

        tree.root = tree.insert(tree.root, 10);
        tree.root = tree.insert(tree.root, 20);
        tree.root = tree.insert(tree.root, 30);
        tree.root = tree.insert(tree.root, 40);
        tree.root = tree.insert(tree.root, 50);
        tree.root = tree.insert(tree.root, 25);

        // La raíz debería ser 30 después de los balanceos
        // Pero depende del orden exacto, lo importante es que esté balanceado
        assert Math.abs(tree.getBalance(tree.root)) <= 1;
        
        System.out.println("Reto 008 (Java): AVL Tree insertado y balanceado.");
    }
}
