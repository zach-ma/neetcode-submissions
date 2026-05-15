# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        1. Brute Force
        '''

        '''
        2. Inorder Traversal (my soln)
        T: O(n)
        S: O(n)
        '''
        # arr = []
        # def dfs(node):
        #     if not node:
        #         return
        #     dfs(node.left)
        #     arr.append(node.val)
        #     dfs(node.right)
        # dfs(root)
        # return arr[k-1]
        
        ''' REDO!!!
        3. Recursive DFS (Optimal)

        T: O(h+k) in terms of nodes visited, worst-case O(n)
        S: O(h) for the recursion stack, worst-case O(n)
        '''
        # cnt = 0
        # res = root.val

        # def dfs(node):
        #     nonlocal cnt, res
        #     if not node:
        #         return

        #     dfs(node.left)

        #     cnt += 1
        #     if cnt == k:
        #         res = node.val
        #         return # return early!!!
            
        #     dfs(node.right)
        # dfs(root)
        # return res

        

        ''' REDO??????
        4. Iterative DFS (Optimal)
        '''
        n = 0
        stack = []
        cur = root

        # Continue as long as there are nodes to process or items in the stack
        while stack or cur:
            # 1. Reach the leftmost node of the current subtree
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # 2. Process the node (this is the "In-Order" visit)
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            
            # 3. Move to the right child to repeat the process
            cur = cur.right
        