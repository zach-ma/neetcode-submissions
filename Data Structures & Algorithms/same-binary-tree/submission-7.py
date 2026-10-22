# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        t1, t2 = p, q
        if t1 is None and t2 is None:
            return True
        if t1 and t2 and t1.val == t2.val:
            return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)
        return False