# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_pointer = m - 1
        nums2_pointer = n - 1
        if nums2_pointer < 0:
            return None

        for index in range(m + n - 1, -1, -1):
            if nums1[nums1_pointer] > nums2[nums2_pointer] and nums1_pointer > -1:
                nums1[index] = nums1[nums1_pointer]
                nums1_pointer -= 1
            else:
                nums1[index] = nums2[nums2_pointer]
                nums2_pointer -= 1
                if nums2_pointer < 0:
                    break
        return None


# Time complexity: O(m + n)
# Space Complexity: O(1)
# Runtime: 36 ms (68.04%)
# Memory Usage: 14.3 MB (63.25%)

solution0 = Solution()
input0 = [1, 2, 3, 0, 0, 0]
solution0.merge(input0, 3, [2, 5, 6], 3)
print(input0 == [1, 2, 2, 3, 5, 6])
solution1 = Solution()
input1 = [1]
solution1.merge(input1, 1, [], 0)
print(input1 == [1])
solution2 = Solution()
input2 = [4, 5, 6, 0, 0, 0]
solution2.merge(input2, 3, [1, 2, 3], 3)
print(input2 == [1, 2, 3, 4, 5, 6])
