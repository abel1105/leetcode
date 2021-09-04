# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
from typing import List
from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        sl = SortedList()
        for i in range(len(nums)):
            if i > k:
                sl.remove(nums[i - k - 1])

            left = sl.bisect_left(nums[i] - t)
            right = sl.bisect_right(nums[i] + t)

            if right - left > 0:
                return True

            sl.add(nums[i])

        return False

# Time complexity: O(Nlogk)
# Space Complexity: O(k)
# Runtime: 426 ms (14.14%)
# Memory Usage: 17.2 MB (91.64%)
