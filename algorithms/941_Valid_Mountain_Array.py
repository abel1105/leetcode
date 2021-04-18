# Input: arr = [2,1]
# Output: false
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        first = 0
        last = length - 1

        while first + 1 < length and arr[first] < arr[first + 1]:
            first += 1

        while arr[last - 1] > arr[last]:
            last -= 1

        return 0 < first == last < length - 1


# Time complexity: O(n)
# Space Complexity: O(1)
# Runtime: 184 ms (99.17%)
# Memory Usage: 15.4 MB (95.81%)

solution0 = Solution()
print(solution0.validMountainArray([2, 1]) == False)
solution1 = Solution()
print(solution1.validMountainArray([3, 5, 5]) == False)
solution2 = Solution()
print(solution2.validMountainArray([0, 3, 2, 1]) == True)
solution3 = Solution()
print(solution3.validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == False)
solution4 = Solution()
print(solution4.validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False)
solution5 = Solution()
print(solution5.validMountainArray([3, 7, 20, 14, 15, 14, 10, 8, 2, 1]) == False)
