# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ''' REDO??? 1. hard to understand the 1 + max(left, right) thing!!!! 2. hard to understand comparing to max of subtrees
    1. brute force

    Intuition

    For any node in a tree, the longest path that goes through it is:

        height of left subtree + height of right subtree

    So to find the tree’s diameter, we check this value for every node.
    We also compare it with the best diameter found in the left and right subtrees.

    T: O(n^2) ?????????
    S: O(n)
    '''
    # def maxHeight(self, root: Optional[TreeNode]):
    #     if not root:
    #         return 0
    #     return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))

    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     leftHeight = self.maxHeight(root.left)
    #     rightHeight = self.maxHeight(root.right)
    #     diameter = leftHeight + rightHeight
    #     sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    #     return max(diameter, sub)

    '''REDO??? hard to understand the 1 + max(left, right) thing
    2.1 recursive dfs (use self. for variable)

    Intuition

    The diameter of a binary tree is the longest path between any two nodes.
    This path must go through some node, and at that node the path length is:

        (left subtree height) + (right subtree height)

    So while doing a DFS to compute heights, we can simultaneously track the
    maximum left + right seen so far.
    This gives the diameter in one pass without recomputing heights.

    T: O(n) !!!!
    S: O(h), best case(balanced tree): O(logn), worst case(degenerate tree): O(n),
        where nn is the number of nodes in the tree and hh is the height of the tree. !!!!!
    '''
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

    '''REDO???
    2.2 recursive dfs (use nonlocal for variable)
    '''
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        # dfs() returns height
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal res # NOTE: nonlocal!!!!!!
            res = max(res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return res

    ''' REDO???
    3. Iterative DFS
    '''











