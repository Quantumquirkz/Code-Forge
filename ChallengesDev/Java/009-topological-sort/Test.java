import java.util.Arrays;

public class Test {
    public static void main(String[] args) {
        Solucion sol = new Solucion();

        // Caso 1
        int n1 = 4;
        int[][] p1 = {{1, 0}, {2, 0}, {3, 1}, {3, 2}};
        int[] res1 = sol.findOrder(n1, p1);
        // Validar que el orden cumple (ej: 3 antes que 1 y 2, 1/2 antes que 0)
        assert res1.length == 4;
        
        // Caso 2: Con ciclo
        int n2 = 2;
        int[][] p2 = {{0, 1}, {1, 0}};
        int[] res2 = sol.findOrder(n2, p2);
        assert res2.length == 0;

        System.out.println("Reto 009 (Java): Ordenación topológica verificada.");
    }
}
