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
        '''
        1. Depth First Search
        '''
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # NOTE: use of index()!!!
        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root






















