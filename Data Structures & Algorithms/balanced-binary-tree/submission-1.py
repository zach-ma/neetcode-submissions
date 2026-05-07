# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                # return 0
                return -1
            # if not node.left and not node.right:
            #     return 0
            left = height(node.left)
            right = height(node.right)
            return 1 + max(height(node.left), height(node.right))
        
        if not root:
            return True
        sub = self.isBalanced(root.left) and self.isBalanced(root.right)
        return abs(height(root.left) - height(root.right)) <= 1 and sub
