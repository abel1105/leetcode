# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            real_index = abs(nums[i]) - 1
            if nums[real_index] > 0:
                nums[real_index] = -nums[real_index]
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result


# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 368 ms (43.73%)
# Memory Usage: 22.4 MB (53.19%)

solution0 = Solution()
print(solution0.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]), solution0.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6])
solution1 = Solution()
print(solution1.findDisappearedNumbers([1, 1]), solution1.findDisappearedNumbers([1, 1]) == [2])
