# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        Intuition

        We are working with a Binary Search Tree (BST), so:

            All values in the left subtree of a node are smaller than the node’s value.
            All values in the right subtree are greater than the node’s value.

        For two nodes p and q:

            If both values are smaller than the current node -> both must lie in the left subtree.
            If both values are greater than the current node -> both must lie in the right subtree.
            Otherwise, the current node is the split point where one node is on the left and the other is on the right (or one is equal to the current node).
            That split point is the Lowest Common Ancestor (LCA).
        '''

        '''
        1.0 recursion (my soln)
        '''
        # if p.val < root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # if p.val > root.val and q.val > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # return root

        '''
        1.1 recurison
        T: O(h)!!!!
        S: O(h)
        '''
        if not root or not p or not q:
            return None
        if max(p.val, q.val) < root.val: # NOTE: smart to use max/min!!!!
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

        ''' REDO!!
        2. iteration
        T: O(h)!!!!
        S: O(1)
        '''
        # cur = root
        # while cur:
        #     if p.val < cur.val and q.val < cur.val:
        #         cur = cur.left
        #     elif p.val > cur.val and q.val > cur.val:
        #         cur = cur.right
        #     else:
        #         return cur
        

        