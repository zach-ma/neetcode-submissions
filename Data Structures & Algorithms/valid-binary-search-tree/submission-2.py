# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        0.0 my wrong solution
        LESSON:
            - binary search tree properties: ALL values in its left/right subtree are strictly less/greater than node's value!!!!!
            - CANNOT just check neighbours!!!
        '''
        # if not root:
        #     return True
        # if root.left and root.val <= root.left.val:
        #     return False
        # if root.right and root.val >= root.right.val:
        #     return False
        # return self.isValidBST(root.left) and self.isValidBST(root.right)
        
        '''
        intuition: pass down upper and lower bound when doing dfs(), and update the bounds
        '''
        def dfs(node, lower, upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root, -math.inf, math.inf)


