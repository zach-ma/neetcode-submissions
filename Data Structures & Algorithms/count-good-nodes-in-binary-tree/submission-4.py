# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # count = 0
        # def dfs(node, prevMax):
        #     nonlocal count # immutable var so need to declare it nonlocal
        #     if not node:
        #         return
        #     if prevMax <= node.val:
        #         count += 1
        #     prevMax = max(prevMax, node.val)
        #     dfs(node.left, prevMax)
        #     dfs(node.right, prevMax)
        # dfs(root, root.val)
        # return count

        def dfs(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(node.val, maxVal)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        return dfs(root, root.val)




