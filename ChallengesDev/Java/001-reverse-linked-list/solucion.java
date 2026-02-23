/**
 * Solution to Challenge 001: Reverse Linked List
 * Includes iterative and recursive approaches.
 */

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class solucion {

    /**
     * Iterative Approach.
     * Uses three pointers to redirect the links.
     * 
     * Time Complexity: O(n)
     * Space Complexity: O(1)
     */
    public ListNode reverseListIterative(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }

    /**
     * Recursive Approach.
     * Reverses the rest of the list and then adjusts the current node.
     * 
     * Time Complexity: O(n)
     * Space Complexity: O(n) due to the recursion stack.
     */
    public ListNode reverseListRecursive(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode newHead = reverseListRecursive(head.next);
        head.next.next = head;
        head.next = null;
        return newHead;
    }

    /*
     * Complexity Analysis:
     * 
     * Iterative:
     * - Time: O(n) because we traverse each node once.
     * - Space: O(1) since we only use auxiliary pointers.
     * 
     * Recursive:
     * - Time: O(n) each node is visited once.
     * - Space: O(n) stack space scales with list length.
     */
}
