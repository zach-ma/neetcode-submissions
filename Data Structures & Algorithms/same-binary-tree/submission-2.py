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
        # return not pqueue and not qqueue

        '''
        2. recursive DFS
        '''
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
        '''
        2. iterative DFS
        '''









        

