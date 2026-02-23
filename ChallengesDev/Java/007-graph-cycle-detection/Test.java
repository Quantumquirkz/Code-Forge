public class Test {
    public static void main(String[] args) {
        Solucion sol = new Solucion();

        // Caso 1: Con ciclo
        int v1 = 4;
        int[][] e1 = {{0, 1}, {1, 2}, {2, 0}, {2, 3}};
        assert sol.hasCycle(v1, e1) == true;

        // Caso 2: Sin ciclo
        int v2 = 3;
        int[][] e2 = {{0, 1}, {1, 2}};
        assert sol.hasCycle(v2, e2) == false;

        // Caso 3: Múltiples componentes, uno con ciclo
        int v3 = 5;
        int[][] e3 = {{0, 1}, {2, 3}, {3, 4}, {4, 2}};
        assert sol.hasCycle(v3, e3) == true;

        System.out.println("Reto 007 (Java): Todos los casos pasaron.");
    }
}
