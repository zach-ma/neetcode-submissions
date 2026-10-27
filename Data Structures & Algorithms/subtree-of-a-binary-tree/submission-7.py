# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(t1, t2):
            if not t1 and not t2:
                return True
            if t1 and t2:
                return t1.val == t2.val and isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)
            return False
        if not root or not subRoot:
            return False
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
            