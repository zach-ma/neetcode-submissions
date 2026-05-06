# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    1. brute force
    '''
    def maxHeight(self, root: Optional[TreeNode]):
        if not root:
            return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        diameter = leftHeight + rightHeight
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)

    '''REDO!!!
    2. recursive dfs
    '''
    # res = 0
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     self.res = 0

    #     # dfs() returns height
    #     def dfs(node):
    #         if not node:
    #             return 0
    #         left = dfs(node.left)
    #         right = dfs(node.right)
    #         self.res = max(self.res, left + right)
    #         return 1 + max(left, right)
    #     dfs(root)
    #     return self.res













