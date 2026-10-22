"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''my soln after hint
        '''
        # oldToNew = {}
        # def dfs(node):
        #     if not node:
        #         return
        #     if node in oldToNew:
        #         return oldToNew[node]
        #     oldToNew[node] = Node(node.val)
        #     for n in node.neighbors:
        #         oldToNew[node].neighbors.append(dfs(n))
        #     return oldToNew[node]

        # return dfs(node)
        '''neet: dfs
        '''
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val) # NOTE: use copy as a var is clear!
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei)) # NOTE: critical
            return copy

        return dfs(node) if node else None


