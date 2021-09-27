# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]
#
# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)


class MyHashSet:
    def eval_hash(self, key):
        return key % self.size

    def __init__(self):
        self.size = 10000
        self.arr = [None] * self.size

    def add(self, key: int) -> None:
        t = self.eval_hash(key)
        if self.arr[t] is None:
            self.arr[t] = [key]
        elif key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        if self.arr[t] is not None and key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key: int) -> bool:
        t = self.eval_hash(key)
        if self.arr[t] is None:
            return False
        return key in self.arr[t]

# Time complexity: O(1)
# Space Complexity: O(10000)
# Runtime: 164 ms (78.79%)
# Memory Usage: 18.9 MB (62.04%)
