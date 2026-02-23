import java.util.concurrent.locks.ReentrantLock;

/**
 * Simplified implementation of a concurrent hash map.
 * Uses an array of locks to reduce contention.
 */
public class SimpleConcurrentHashMap<K, V> {
    private static class Node<K, V> {
        final K key;
        V value;
        Node<K, V> next;

        Node(K key, V value, Node<K, V> next) {
            this.key = key;
            this.value = value;
            this.next = next;
        }
    }

    private final Node<K, V>[] table;
    private final ReentrantLock[] locks;
    private final int capacity;

    @SuppressWarnings("unchecked")
    public SimpleConcurrentHashMap(int capacity) {
        this.capacity = capacity;
        this.table = new Node[capacity];
        this.locks = new ReentrantLock[capacity];
        for (int i = 0; i < capacity; i++) {
            locks[i] = new ReentrantLock();
        }
    }

    private int getIndex(K key) {
        return Math.abs(key.hashCode() % capacity);
    }

    public void put(K key, V value) {
        int index = getIndex(key);
        locks[index].lock();
        try {
            Node<K, V> head = table[index];
            Node<K, V> curr = head;
            while (curr != null) {
                if (curr.key.equals(key)) {
                    curr.value = value;
                    return;
                }
                curr = curr.next;
            }
            table[index] = new Node<>(key, value, head);
        } finally {
            locks[index].unlock();
        }
    }

    public V get(K key) {
        int index = getIndex(key);
        // In a real implementation, 'get' could be lock-free using 'volatile'
        locks[index].lock();
        try {
            Node<K, V> curr = table[index];
            while (curr != null) {
                if (curr.key.equals(key)) {
                    return curr.value;
                }
                curr = curr.next;
            }
            return null;
        } finally {
            locks[index].unlock();
        }
    }
}

/**
 * Complexity Analysis:
 * Time: O(1) average for put/get.
 * Space: O(N + C) where N is the number of elements and C the bucket capacity.
 */
