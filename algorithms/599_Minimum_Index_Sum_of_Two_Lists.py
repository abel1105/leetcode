# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        bucket = {}
        result = []
        minimum = len(list1) + len(list2) - 2

        for key, value in enumerate(list1):
            bucket[value] = key
        for key, value in enumerate(list2):
            if value in bucket:
                temp = bucket[value] + key
                if temp < minimum:
                    result.clear()
                    result.append(value)
                    minimum = temp
                elif temp == minimum:
                    result.append(value)

        return result


# Time complexity: O(l1 + l2)
# Space Complexity: O(l1 * x) (x: average string length)
# Runtime: 152 ms (87.97%)
# Memory Usage: 14.6 MB (86.93%)
