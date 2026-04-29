# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ''' REDO!!!
        1. Brute Force
        We store all nodes in an array so we can directly access the node that is n positions from the end.
        Once we know which node to delete, we simply adjust the next pointer of the previous node.
        T: O(n)
        S: O(n)
        '''
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        removeIndex = len(nodes) - n # NOTE: use removeIndex = (N - n) to track!!!
        if removeIndex == 0: # NOTE: boundary edge case!!!
            return head.next

        nodes[removeIndex - 1].next = nodes[removeIndex].next # NOTE: use [removeIndex].next not [removeIndex+1] to avoid index out of range!!!
        return head

        '''
        2.0 Iteration (Two Pass), my failed soln
        '''
        # size = 0
        # cur = head
        # while cur:
        #     size += 1
        #     cur = cur.next
        
        # cur = head
        # while size > n + 1:
        #     size -= 1
        #     cur = cur.next
        # if cur and cur.next:
        #     tmp = cur.next
        #     cur.next = cur.next.next
        #     tmp.next = None
        
        # return head

        '''
        2. Iteration (Two Pass)
        T: O(n)
        S: O(1)
        '''
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next
        
        removeIndex = N - n # NOTE: use removeIndex = (N - n) to track!!!
        if removeIndex == 0:
            return head.next
        
        cur = head
        for i in range(N - 1):
            if i + 1 == removeIndex:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head















