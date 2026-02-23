import java.util.Arrays;

/**
 * Solution to Challenge 006: Longest Increasing Subsequence.
 * Optimized implementation using Binary Search in O(n log n).
 */
public class Solucion {
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) return 0;

        int[] tails = new int[nums.length];
        int size = 0;

        for (int x : nums) {
            int i = 0, j = size;
            // Binary search to find insertion position
            while (i != j) {
                int m = (i + j) / 2;
                if (tails[m] < x)
                    i = m + 1;
                else
                    j = m;
            }
            tails[i] = x;
            if (i == size) size++;
        }

        return size;
    }
}

/**
 * Complexity Analysis:
 * Time: O(n log n) thanks to binary search.
 * Space: O(n) for the tails array.
 */
