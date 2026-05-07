# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pqueue, qqueue = deque([p]), deque([q])
        while pqueue and qqueue:
            pnode = pqueue.popleft()
            qnode = qqueue.popleft()
            if not pnode and not qnode:
                continue
            if pnode and qnode and pnode.val == qnode.val:
                pqueue.append(pnode.left)
                pqueue.append(pnode.right)
                qqueue.append(qnode.left)
                qqueue.append(qnode.right)
            else:
                return False
        return not pqueue and not qqueue
            
            

