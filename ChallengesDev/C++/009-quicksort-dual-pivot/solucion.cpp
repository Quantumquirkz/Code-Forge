#include <vector>
#include <algorithm>

/**
 * Implementation of Dual-Pivot Quicksort.
 */
class DualPivotSorting {
public:
    void sort(std::vector<int>& nums, int low, int high) {
        if (low < high) {
            int lp, rp;
            partition(nums, low, high, lp, rp);
            sort(nums, low, lp - 1);
            sort(nums, lp + 1, rp - 1);
            sort(nums, rp + 1, high);
        }
    }

private:
    void partition(std::vector<int>& nums, int low, int high, int& lp, int& rp) {
        if (nums[low] > nums[high]) {
            std::swap(nums[low], nums[high]);
        }

        int p1 = nums[low];
        int p2 = nums[high];

        int i = low + 1;
        int j = high - 1;
        int k = low + 1;

        while (k <= j) {
            if (nums[k] < p1) {
                std::swap(nums[k], nums[i]);
                i++;
            } else if (nums[k] >= p2) {
                while (nums[j] > p2 && k < j) {
                    j--;
                }
                std::swap(nums[k], nums[j]);
                j--;
                if (nums[k] < p1) {
                    std::swap(nums[k], nums[i]);
                    i++;
                }
            }
            k++;
        }
        i--;
        j++;

        std::swap(nums[low], nums[i]);
        std::swap(nums[high], nums[j]);

        lp = i;
        rp = j;
    }
};

/**
 * Complexity Analysis:
 * Time: O(n log n) average.
 * Space: O(log n) for the recursion stack.
 */
