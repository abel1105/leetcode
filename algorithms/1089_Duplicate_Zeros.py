# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr) - 1
        duplicate = 0

        for index in range(length):
            if index > length - duplicate:
                break
            if arr[index] == 0:
                # no more space for duplicate, add the lonely zero first
                if index > length - duplicate - 1:
                    arr[length] = 0
                    length -= 1
                    break
                else:
                    duplicate += 1

        last = length - duplicate

        # Only deal with the actually duplicate zero
        for index in range(last, -1, -1):
            if arr[index] == 0:
                arr[index + duplicate] = 0
                duplicate -= 1
                arr[index + duplicate] = 0
            else:
                arr[index + duplicate] = arr[index]
        return None


# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 64 ms (92.67%)
# Memory Usage: 14.7 MB (86.42%)

solution0 = Solution()
input0 = [1, 0, 2, 3, 0, 4, 5, 0]
solution0.duplicateZeros(input0)
print(input0 == [1, 0, 0, 2, 3, 0, 0, 4])
solution1 = Solution()
input1 = [1, 2, 3]
solution1.duplicateZeros(input1)
print(input1 == [1, 2, 3])
solution2 = Solution()
input2 = [8, 4, 5, 0, 0, 0, 0, 7]
solution2.duplicateZeros(input2)
print(input2 == [8, 4, 5, 0, 0, 0, 0, 0])
solution3 = Solution()
input3 = [8, 0, 0, 2, 0, 0, 0]
solution3.duplicateZeros(input3)
print(input3 == [8, 0, 0, 0, 0, 2, 0])
