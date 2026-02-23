#include <vector>
#include <climits>
#include <algorithm>

/**
 * Solution to the Matrix Chain Multiplication problem using DP.
 */
class MatrixChainOptimizer {
public:
    int solve(const std::vector<int>& p) {
        int n = p.size() - 1; // Number of matrices
        std::vector<std::vector<int>> m(n + 1, std::vector<int>(n + 1, 0));

        // L is the length of the matrix chain
        for (int L = 2; L <= n; L++) {
            for (int i = 1; i <= n - L + 1; i++) {
                int j = i + L - 1;
                m[i][j] = INT_MAX;
                for (int k = i; k <= j - 1; k++) {
                    int q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j];
                    if (q < m[i][j]) {
                        m[i][j] = q;
                    }
                }
            }
        }

        return m[1][n];
    }
};

/**
 * Complexity Analysis:
 * Time: O(n^3) where n is the number of matrices.
 * Space: O(n^2) for the DP table.
 */
 pieces of code.
