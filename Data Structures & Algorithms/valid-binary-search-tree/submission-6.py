# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''my failed soln
        lesson: all nodes in left subtree should be smaller than root node
        '''
        # if not root:
        #     return True
        # l, r = True, True
        # if root.left:
        #     l = root.left.val < root.val and self.isValidBST(root.left)
        # if root.right:
        #     r = root.right.val > root.val and self.isValidBST(root.right)
        # return l and r
        '''my failed soln after hint
        '''
        # def dfs(root, lower, upper):
        #     if not root:
        #         return True
        #     l, r = True, True
        #     if root.left:
        #         l = lower < root.left.val < upper and dfs(root.left, lower, root.val)
        #     if root.right:
        #         r = lower < root.right.val < upper and dfs(root.right, root.val, upper)
        #     return l and r
        # return dfs(root, -math.inf, math.inf)

        def valid(node, lower, upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            return valid(node.left, lower, node.val) and valid(node.right, node.val, upper)
        return valid(root, -math.inf, math.inf)







