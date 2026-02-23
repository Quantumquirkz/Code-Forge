public class Test {
    public static void main(String[] args) {
        Solucion sol = new Solucion();

        // Caso 1: Impar
        int[] n1 = {1, 3};
        int[] n2 = {2};
        assert sol.findMedianSortedArrays(n1, n2) == 2.0;

        // Caso 2: Par
        int[] n3 = {1, 2};
        int[] n4 = {3, 4};
        assert sol.findMedianSortedArrays(n3, n4) == 2.5;

        // Caso 3: Uno vacío
        int[] n5 = {};
        int[] n6 = {1};
        assert sol.findMedianSortedArrays(n5, n6) == 1.0;

        System.out.println("Reto 002 (Java): Todos los casos pasaron.");
    }
}
