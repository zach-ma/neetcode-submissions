"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        1.1 Depth First Seacrh (my soln after trial and error)
        '''
        # if not node:
        #     return None
        # cloned = {} # old -> new, to avoid recreating new nodes!!!
        # res = Node()

        # def dfs(old, new):
        #     new.val = old.val
        #     cloned[old] = new
        #     for neighbor in old.neighbors:
        #         if neighbor not in cloned:
        #             n = Node()
        #             dfs(neighbor, n)
        #             new.neighbors.append(n)
        #         else:
        #             new.neighbors.append(cloned[neighbor])

        # dfs(node, res)
        # return res
        
        '''
        1.2 Depth First Seacrh
        '''
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None
            













