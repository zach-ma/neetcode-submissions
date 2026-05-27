"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned = {} # old -> new 
        res = Node()

        def dfs(old, new):
            new.val = old.val
            cloned[old] = new
            for neighbor in old.neighbors:
                if neighbor not in cloned:
                    n = Node()
                    dfs(neighbor, n)
                    new.neighbors.append(n)
                else:
                    new.neighbors.append(cloned[neighbor])

        dfs(node, res)
        return res
            