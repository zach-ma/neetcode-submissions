# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        my soln: recursive dfs
        '''
        # if not root:
        #     return 0
        # if not root.left and not root.right:
        #     return 1
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        '''
        my soln: iterative bfs, FAILED!!!
        '''
        # if not root:
        #     return 0

        # maxDepth = 0
        # queue = deque([root])
        # while queue:
        #     node = queue.popleft()
        #     if node.left:
        #         queue.append(node.left)
        #     elif node.right:
        #         queue.append(node.right)
        #     else:
        #         maxDepth = max()
        ''' REDO!!!
        3. BFS (by level)
        - Every iteration of BFS processes one entire level of the tree.!!!!!!
        - So each completed level corresponds to increasing the depth by 1.!!!!
        '''
        q = deque()
        if root:
            q.append(root)
        level = 0
        while q:
            # NOTE: processes one entire level!!!!
            for i in range(len(q)): # NOTE: range(len(q)) evaluated exactly ONLY ONCE before the first iteration loop starts!!!!! like snapshot
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level











