# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        visited = {}
        return self.dfs(node, visited)

    def dfs(self, node, visited):
        if node.val in visited:
            return visited[node.val]
        copy = Node(node.val)
        visited[node.val] = copy
        for i in node.neighbors:
            copy.neighbors.append(self.dfs(i, visited))

        return copy

# Time complexity: O(N + M)
# Space Complexity: O(N)
# Runtime: 55 ms (28.13%)
# Memory Usage: 14.7 MB (26.94%)
