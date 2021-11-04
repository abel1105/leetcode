# Input
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# Output
# [null, null, 3, null, 5]
#
# Explanation
# MapSum mapSum = new MapSum();
# mapSum.insert("apple", 3);
# mapSum.sum("ap");           // return 3 (apple = 3)
# mapSum.insert("app", 2);
# mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0


class MapSum:

    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta

    def sum(self, prefix: str) -> int:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score


# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 36 ms (48.52%)
# Memory Usage: 14.3 MB (81.66%)
