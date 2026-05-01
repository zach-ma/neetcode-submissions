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
        LESSON: can merge one base case to recursive case
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
        '''
        1. Recursive DFS
        - The depth of a tree = 1 + maximum depth of its left and right subtrees.
        T: O(n)
        S: O(h): 
            - best case (balanced tree): O(logn)
            - worst case (degenerate tree): O(n)
            Where n is the number of nodes in the tree and h is the height of the tree.!!!
        '''
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        '''
        2. Iterative DFS (Stack)
        
        Intuition:

        Instead of relying on recursion to explore the tree, we can simulate DFS explicitly using a stack.
        The stack will store pairs of:

            the current node
            the depth of that node in the tree

        Every time we pop a node from the stack:

            We update the maximum depth seen so far.
            We push its left and right children onto the stack with depth + 1.

        This approach works like a manual DFS where we keep track of depth ourselves.
        It avoids recursion and is useful when recursion depth may become too large.
        '''
        res = 0
        stack = [(root, 1)] # NOTE: destructuring 
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(depth, res)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return res


        ''' REDO!!!
        3. BFS (by level!!!)
        - Every iteration of BFS processes one entire level of the tree.!!!!!!
        - So each completed level corresponds to increasing the depth by 1.!!!!
        '''
        q = deque()
        if root:
            q.append(root)
        level = 0
        while q:
            # NOTE: processes one entire level!!!!
            for i in range(len(q)): # NOTE: "snapshot", range(len(q)) evaluated exactly ONLY ONCE before the first iteration loop starts!!!!! 
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level











