public class Test {
    public static void main(String[] args) {
        Solucion sol = new Solucion();

        int[][] m1 = {{1, 0, 0}, {-1, 0, 3}};
        int[][] m2 = {{7, 0, 0}, {0, 0, 0}, {0, 0, 1}};
        int[][] res = sol.multiply(m1, m2);

        // Validar resultado
        assert res[0][0] == 7;
        assert res[1][0] == -7;
        assert res[1][2] == 3;

        System.out.println("Reto 010 (Java): Multiplicación de matrices dispersas finalizada.");
    }
}
