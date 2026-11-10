# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, prevMax):
            nonlocal count
            if not node:
                return
            if prevMax <= node.val:
                count += 1
            prevMax = max(prevMax, node.val)
            dfs(node.left, prevMax)
            dfs(node.right, prevMax)
        dfs(root, root.val)
        return count