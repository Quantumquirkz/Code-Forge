import java.util.PriorityQueue;

/**
 * Definition for a singly-linked list.
 */
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

/**
 * Solution to Challenge 003: Merge K Sorted Lists.
 * Uses a PriorityQueue (Min-Heap) to merge lists efficiently.
 */
public class Solucion {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;

        // Min-Heap based on node values
        PriorityQueue<ListNode> queue = new PriorityQueue<>((a, b) -> a.val - b.val);

        // Insert the head of each list into the queue
        for (ListNode node : lists) {
            if (node != null) {
                queue.add(node);
            }
        }

        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        while (!queue.isEmpty()) {
            // Get the smallest node
            ListNode smallest = queue.poll();
            current.next = smallest;
            current = current.next;

            // If the node has a successor, add it to the queue
            if (smallest.next != null) {
                queue.add(smallest.next);
            }
        }

        return dummy.next;
    }
}

/**
 * Complexity Analysis:
 * Time: O(N log k) - N is the total number of nodes, k is the number of lists.
 * Space: O(k) - Space for the PriorityQueue.
 */
