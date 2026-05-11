# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
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

        res = 0
        q = deque([(root, root.val)])
        while q:
            for _ in range(len(q)):
                node, curMax = q.popleft()
                if node:
                    if node.val >= curMax:
                        res += 1
                        curMax = max(curMax, node.val)
                    q.append((node.left, curMax))
                    q.append((node.right, curMax))
        return res


