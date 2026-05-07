# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        1.0 BFS(my soln)

        T: O(n)
        S: O(n)
        '''
        # pqueue, qqueue = deque([p]), deque([q])
        # while pqueue and qqueue:
        #     pnode = pqueue.popleft()
        #     qnode = qqueue.popleft()
        #     if not pnode and not qnode:
        #         continue
        #     if pnode and qnode and pnode.val == qnode.val:
        #         pqueue.append(pnode.left)
        #         pqueue.append(pnode.right)
        #         qqueue.append(qnode.left)
        #         qqueue.append(qnode.right)
        #     else:
        #         return False
        # return not pqueue and not qqueue # IMPROVEMENT: no need, just return True

        ''' REDO!!!
        2. recursive DFS
        
        T: O(n)
        S: O(n), O(logn) best, O(n) worst
        '''
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

        ''' REDO!!!
        3. iterative DFS
        '''
        stack = [(p, q)] # NOTE: bundled as pairs to process at the same time using one container!!!!
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val: # NOTE: hard to understand!!!!
                return False
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
        return True
            










        

