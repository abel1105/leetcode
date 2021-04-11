# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dict = {}
        for index in range(len(arr)):
            if arr[index] * 2 in dict:
                return True
            elif arr[index] % 2 == 0 and arr[index] / 2 in dict:
                return True
            else:
                dict[arr[index]] = index
        return False


# Time complexity: O(n)
# Space Complexity: O(n)
# Runtime: 48 ms (86.73%)
# Memory Usage: 14.4 MB (51.63%)

solution0 = Solution()
print(solution0.checkIfExist([10, 2, 5, 3]) == True)
solution1 = Solution()
print(solution1.checkIfExist([7, 1, 14, 11]) == True)
solution2 = Solution()
print(solution2.checkIfExist([3, 1, 7, 11]) == False)
solution3 = Solution()
print(solution3.checkIfExist([-20, 8, -6, -14, 0, -19, 14, 4]) == True)
