# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        1.1 Depth First Search (my soln after 1 hint)
        '''
        # def recurse(preorder, inorder):
        #     if not preorder:
        #         return
        #     root = TreeNode(preorder[0])
        #     for i in range(len(inorder)):
        #         if inorder[i] == root.val:
        #             root.left = recurse(preorder[1:i+1], inorder[:i])
        #             root.right = recurse(preorder[i+1:], inorder[i+1:])
        #     return root
        # return recurse(preorder, inorder)
        ''' REDO!!!
        1. Depth First Search
        T: O(n^2)
            Each recursive call does a linear search using inorder.index(), and since we do that for every node, the total complexity becomes O(n^2)
        S: O(n^2)
            Slicing costs extra memory.
            Across all recursive calls, the total auxiliary memory can grow to O(n^2)
        '''
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # NOTE: use of linear scan index()!!!
        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

        ''' REDO???
        2. Hash Map + Depth First Search
        '''

        ''' REDO???
        3. Depth First Search (Optimal)
        '''






















