# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''my soln
        '''
        # def height(node):
        #     if not node:
        #         return 0
        #     return 1 + max(height(node.left), height(node.right))
        # if not root:
        #     return True
        # if abs(height(root.left) - height(root.right)) > 1:
        #     return False
        # return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        '''neet
        cons: return is too complex to manage
        '''
        # def dfs(root): # -> [balanced, height]
        #     if not root:
        #         return [True, 0]
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     balanced = False
        #     if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
        #         balanced = True
        #     return [balanced, 1 + max(left[1], right[1])]
        # return dfs(root)[0]
        '''
        '''
        self.balanced = True
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) > 1:
                self.balanced = False
            return 1 + max(left, right)
        dfs(root)
        return self.balanced









