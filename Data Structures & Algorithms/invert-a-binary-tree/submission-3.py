# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        my soln
        LESSON: no helper needed!
        '''
        # def invert(node):
        #     if not node:
        #         return None
        #     node.left, node.right = node.right, node.left
        #     invert(node.left)
        #     invert(node.right)
        #     return node
        # return invert(root)

        '''
        1. Depth First Search
        '''
        # if not root:
        #     return None
        
        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        ''' REDO!!!
        2. Breadth First Search
        '''
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root










