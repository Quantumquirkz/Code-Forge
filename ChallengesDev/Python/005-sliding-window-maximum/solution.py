from collections import deque
from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    """
    Finds the maximum in each window of size k using a monotonic queue.
    
    Time Complexity: O(n)
    Space Complexity: O(k) for the deque
    """
    if not nums or k == 0:
        return []
    if k == 1:
        return nums
        
    result = []
    dq = deque()  # Will store indices
    
    for i in range(len(nums)):
        # 1. Remove indices that are outside the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
            
        # 2. Maintain monotonic descending queue:
        # If the current number is greater than elements at the end of the queue,
        # those elements will never be the maximum in a future window.
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
            
        dq.append(i)
        
        # 3. The element at the front of the queue is the maximum for the current window
        # We only start adding results once we've processed at least k elements
        if i >= k - 1:
            result.append(nums[dq[0]])
            
    return result

# --- Complexity Analysis ---
# Time: O(n)
#   Each index enters and leaves the deque exactly once.
# Space: O(k)
#   The deque stores at most k elements.
