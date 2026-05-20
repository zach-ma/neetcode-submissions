# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def recurse(preorder, inorder):
            if not preorder:
                return
            root = TreeNode(preorder[0])
            for i in range(len(inorder)):
                if inorder[i] == root.val:
                    # left subtree
                    root.left = recurse(preorder[1:i+1], inorder[:i])
                    root.right = recurse(preorder[i+1:], inorder[i+1:])
            return root
        return recurse(preorder, inorder)