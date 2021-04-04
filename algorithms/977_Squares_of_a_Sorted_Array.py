# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        index = right

        while index > -1:
            if abs(nums[left]) > abs(nums[right]):
                result[index] = pow(nums[left], 2)
                left += 1
            else:
                result[index] = pow(nums[right], 2)
                right -= 1
            index -= 1
        return result


# Time complexity: O(n)
# Runtime: 252 ms (26.47%)
# Memory Usage: 16.3 MB

solution0 = Solution()
print(solution0.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100])
solution1 = Solution()
print(solution1.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121])
solution2 = Solution()
print(solution1.sortedSquares([-7, -3, -1, 0]) == [0, 1, 9, 49])
solution3 = Solution()
print(solution3.sortedSquares([1, 2, 3, 4]) == [1, 4, 9, 16])
solution4 = Solution()
print(solution4.sortedSquares([-7, -3, -2, 0, 1]) == [0, 1, 4, 9, 49])
