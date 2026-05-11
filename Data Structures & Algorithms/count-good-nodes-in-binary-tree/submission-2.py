# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        1.0 DFS (my soln)
        LESSON: nonlocal can be avoided by eliminating global var, and return directly from dfs() instead!!!
        '''
        # res = 0

        # def dfs(node, curMax):
        #     if not node:
        #         return
        #     if node.val >= curMax:
        #         curMax = max(curMax, node.val)
        #         nonlocal res # NOTE: nonlocal required for reassignment!!! res is int which is immutable, if append to list then not neccessary!!!!
        #         res += 1
        #     dfs(node.left, curMax)
        #     dfs(node.right, curMax)
        
        # dfs(root, root.val)

        # return res

        ''' REDO????? hard to understand!!!!
        1.1 DFS
        '''
        # def dfs(node, maxVal):
        #     if not node:
        #         return 0
        #     res = 1 if node.val >= maxVal else 0
        #     maxVal = max(maxVal, node.val)
        #     res += dfs(node.left, maxVal)
        #     res += dfs(node.right, maxVal)
        #     return res
        # return dfs(root, root.val)

        '''
        2.0 BFS (my soln)
        LESSON: for loop not needed!!!!!
        '''
        # res = 0
        # q = deque([(root, root.val)])
        # while q:
        #     for _ in range(len(q)): # NOTE: no need level-order loop, curMax is path-specific, making level-wise processing redundant.
        #         node, curMax = q.popleft()
        #         if node:
        #             if node.val >= curMax:
        #                 res += 1
        #                 curMax = max(curMax, node.val) # NOTE: max() is redundant here since node.val >= curMax
        #             q.append((node.left, curMax))
        #             q.append((node.right, curMax))
        # return res

        '''
        2.1 BFS
        '''
        res = 0
        q = deque()
        q.append((root, root.val))
        while q:
            node, maxVal = q.popleft()
            if node.val >= maxVal:
                res += 1
                maxVal = node.val
            if node.left:
                q.append((node.left, maxVal))
            if node.right:
                q.append((node.right, maxVal))
        return res


