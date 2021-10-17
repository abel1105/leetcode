# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.nums_dict = {}

    def insert(self, val: int) -> bool:
        if val in self.nums_dict:
            return False
        self.nums.append(val)
        self.nums_dict[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nums_dict:
            return False
        cur, last = self.nums_dict[val], len(self.nums) - 1
        self.nums_dict[self.nums[last]] = cur
        self.nums[cur], self.nums[last] = self.nums[last], self.nums[cur]
        self.nums.pop()
        del self.nums_dict[val]
        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Time complexity: O(1)
# Space Complexity: O(N)
# Runtime: 528 ms (51.73%)
# Memory Usage: 61.8 MB (66.67%)
