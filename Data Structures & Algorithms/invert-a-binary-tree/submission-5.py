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
        T: O(n)
        S: O(n) for recursion stack!!!!
        '''
        # if not root:
        #     return None
        
        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        ''' REDO!!!!!!
        2. Breadth First Search
        T: O(n)
        S: O(n)
        '''
        # if not root:
        #     return None
        # queue = deque([root])
        # while queue:
        #     node = queue.popleft()
        #     node.left, node.right = node.right, node.left
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        # return root

        '''
        3. Iterative DFS
        Intuition:
        Iterative DFS inverts a binary tree using an explicit stack instead of recursion.
        The idea is the same as recursive DFS:
            Visit a node.
            Swap its left and right children.
            Continue the process for its children.

        But instead of the call stack, we use our own stack data structure.
        The process is:
            Push the root into the stack.
            Pop the top node, swap its children.
            Push its children onto the stack (if they exist).
            Continue until the stack is empty.

        This simulates the recursive DFS in an iterative manner and works well when recursion depth may be too large.

        T: O(n)
        S: O(n)
        '''
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root











