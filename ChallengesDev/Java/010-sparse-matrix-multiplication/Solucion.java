/**
 * Solution to Challenge 010: Sparse Matrix Multiplication.
 * Optimized implementation to ignore zeros.
 */
public class Solucion {
    public int[][] multiply(int[][] mat1, int[][] mat2) {
        int m = mat1.length;
        int k = mat1[0].length;
        int n = mat2[0].length;
        
        int[][] res = new int[m][n];
        
        for (int i = 0; i < m; i++) {
            for (int r = 0; r < k; r++) {
                // Optimization: Skip if the element in mat1 is 0
                if (mat1[i][r] != 0) {
                    for (int j = 0; j < n; j++) {
                        if (mat2[r][j] != 0) {
                            res[i][j] += mat1[i][r] * mat2[r][j];
                        }
                    }
                }
            }
        }
        
        return res;
    }
}

/**
 * Complexity Analysis:
 * Time: O(m * k * n) in the worst case, but O(m * k * L) where L is the
 * average number of non-zero elements per row in mat2.
 * Space: O(m * n) to store the result.
 */
