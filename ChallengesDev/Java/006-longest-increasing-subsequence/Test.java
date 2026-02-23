public class Test {
    public static void main(String[] args) {
        Solucion sol = new Solucion();

        // Caso 1
        int[] n1 = {10, 9, 2, 5, 3, 7, 101, 18};
        assert sol.lengthOfLIS(n1) == 4;

        // Caso 2
        int[] n2 = {0, 1, 0, 3, 2, 3};
        assert sol.lengthOfLIS(n2) == 4;

        // Caso 3: Todo igual
        int[] n3 = {7, 7, 7, 7};
        assert sol.lengthOfLIS(n3) == 1;

        System.out.println("Reto 006 (Java): Todos los casos pasaron.");
    }
}
