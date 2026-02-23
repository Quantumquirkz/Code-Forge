import java.util.LinkedList;
import java.util.Queue;

/**
 * Shared buffer with manual synchronization.
 */
class DataBuffer<T> {
    private final Queue<T> queue = new LinkedList<>();
    private final int capacity;

    public DataBuffer(int capacity) {
        this.capacity = capacity;
    }

    public synchronized void produce(T item) throws InterruptedException {
        while (queue.size() == capacity) {
            wait(); // Wait if full
        }
        queue.add(item);
        notifyAll(); // Notify consumers
    }

    public synchronized T consume() throws InterruptedException {
        while (queue.isEmpty()) {
            wait(); // Wait if empty
        }
        T item = queue.poll();
        notifyAll(); // Notify producers
        return item;
    }
}

/**
 * Producer generates numbers.
 */
class Producer implements Runnable {
    private final DataBuffer<Integer> buffer;

    public Producer(DataBuffer<Integer> buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        try {
            for (int i = 1; i <= 20; i++) {
                buffer.produce(i);
                System.out.println("Produced: " + i);
                Thread.sleep(100);
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

/**
 * Consumer processes numbers.
 */
class Consumer implements Runnable {
    private final DataBuffer<Integer> buffer;

    public Consumer(DataBuffer<Integer> buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        try {
            while (true) {
                Integer item = buffer.consume();
                System.out.println("Consumed: " + item);
                if (item == 20) break; // End
                Thread.sleep(150);
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

/**
 * Complexity Analysis:
 * Time: O(1) for queue operations.
 * Space: O(C) where C is the buffer capacity.
 */
