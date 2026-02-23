#include <vector>

/**
 * Bit manipulation utilities.
 */
class BitMaster {
public:
    // Counts bits (Kernighan's Algorithm)
    int countSetBits(unsigned int n) {
        int count = 0;
        while (n > 0) {
            n &= (n - 1);
            count++;
        }
        return count;
    }

    // Reverses bit order
    unsigned int reverseBits(unsigned int n) {
        unsigned int res = 0;
        for (int i = 0; i < 32; i++) {
            res <<= 1;
            res |= (n & 1);
            n >>= 1;
        }
        return res;
    }

    // Checks for power of two in O(1)
    bool isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }

    // Finds the unique number using XOR
    int getSingleNumber(const std::vector<int>& nums) {
        int res = 0;
        for (int n : nums) {
            res ^= n;
        }
        return res;
    }
};

/**
 * Complexity Analysis:
 * Time:
 * - countSetBits: O(K) where K is the number of bits set to 1.
 * - reverseBits: O(log W) where W is the word size (32).
 * - isPowerOfTwo: O(1).
 * - getSingleNumber: O(N).
 * Space: O(1) for all.
 */
