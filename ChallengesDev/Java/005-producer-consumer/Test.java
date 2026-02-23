public class Test {
    public static void main(String[] args) throws InterruptedException {
        DataBuffer<Integer> buffer = new DataBuffer<>(5);
        
        Thread t1 = new Thread(new Producer(buffer));
        Thread t2 = new Thread(new Consumer(buffer));
        
        t1.start();
        t2.start();
        
        t1.join();
        t2.join();
        
        System.out.println("Reto 005 (Java): Ejecución de Productor-Consumidor finalizada.");
    }
}
