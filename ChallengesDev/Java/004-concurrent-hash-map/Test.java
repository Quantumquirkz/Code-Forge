import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class Test {
    public static void main(String[] args) throws InterruptedException {
        SimpleConcurrentHashMap<String, Integer> map = new SimpleConcurrentHashMap<>(10);
        ExecutorService executor = Executors.newFixedThreadPool(4);

        // Inserción concurrente
        for (int i = 0; i < 100; i++) {
            final int val = i;
            executor.execute(() -> map.put("key" + (val % 10), val));
        }

        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.SECONDS);

        // Verificar que no hay errores fatales y se puede recuperar un valor
        System.out.println("Valor para key0: " + map.get("key0"));
        System.out.println("Reto 004 (Java): Prueba de concurrencia básica finalizada.");
    }
}
