# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        1.0 brute force(my soln)
        '''
        # def height(node):
        #     if not node:
        #         # return 0
        #         return -1 # NOTE: critical!!!! count by edge not node
        #     # if not node.left and not node.right:
        #     #     return 0
        #     return 1 + max(height(node.left), height(node.right))
        
        # if not root:
        #     return True
        # sub = self.isBalanced(root.left) and self.isBalanced(root.right)
        # return abs(height(root.left) - height(root.right)) <= 1 and sub

        '''
        1.1 brute force
        LESSON: top down, so repeated work => so bottom up instead to eliminate repeated work!!!!
        
        T: O(n^2)
        S: O(n)
        '''
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        
        if not root:
            return True
        left = height(root.left)
        right = height(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)











