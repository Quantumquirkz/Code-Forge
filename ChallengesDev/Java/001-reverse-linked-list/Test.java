public class Test {
    public static void main(String[] args) {
        testIterative();
        testRecursive();
        System.out.println("All Java tests passed!");
    }

    static void testIterative() {
        solucion solver = new solucion();
        ListNode head = createList(new int[]{1, 2, 3, 4, 5});
        ListNode result = solver.reverseListIterative(head);
        assertArrayEquals(new int[]{5, 4, 3, 2, 1}, listToArray(result));
    }

    static void testRecursive() {
        solucion solver = new solucion();
        ListNode head = createList(new int[]{1, 2, 3, 4, 5});
        ListNode result = solver.reverseListRecursive(head);
        assertArrayEquals(new int[]{5, 4, 3, 2, 1}, listToArray(result));
    }

    static ListNode createList(int[] vals) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        for (int v : vals) {
            curr.next = new ListNode(v);
            curr = curr.next;
        }
        return dummy.next;
    }

    static int[] listToArray(ListNode head) {
        int count = 0;
        ListNode curr = head;
        while (curr != null) {
            count++;
            curr = curr.next;
        }
        int[] res = new int[count];
        curr = head;
        for (int i = 0; i < count; i++) {
            res[i] = curr.val;
            curr = curr.next;
        }
        return res;
    }

    static void assertArrayEquals(int[] expected, int[] actual) {
        if (expected.length != actual.length) throw new RuntimeException("Length mismatch");
        for (int i = 0; i < expected.length; i++) {
            if (expected[i] != actual[i]) throw new RuntimeException("Value mismatch at index " + i);
        }
    }
}
