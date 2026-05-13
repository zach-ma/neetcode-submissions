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
        
        ''' REDO???
        1. DFS
        KEY idea: pass down upper and lower bound when doing dfs(), and update the bounds
        
        Intuition

        A Binary Search Tree isn’t just about each node being smaller or larger than its parent —
        every node must fit within a valid value range decided by all its ancestors.

            For the root, the allowed range is (-∞, +∞).
            When you go left, the node’s value must be less than the parent, so the upper bound becomes smaller.
            When you go right, the node’s value must be greater than the parent, so the lower bound becomes larger.

        As we move down the tree, we keep tightening these bounds.
        If any node violates its allowed range → the tree is not a BST.

        This checks all BST rules efficiently in one DFS pass.
        '''
        def valid(node, lower, upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            return valid(node.left, lower, node.val) and valid(node.right, node.val, upper)

        return valid(root, -math.inf, math.inf)


