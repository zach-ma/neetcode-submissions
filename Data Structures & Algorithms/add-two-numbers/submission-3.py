# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        my soln: iterative
        '''
        n1, n2 = 0, 0
        
        cur = l1
        digit = 0
        while cur:
            n1 += cur.val * (10 ** digit)
            digit += 1
            cur = cur.next
        
        cur = l2
        digit = 0
        while cur:
            n2 += cur.val * (10 ** digit)
            digit += 1
            cur = cur.next

        dummy = ListNode()
        cur = dummy
        s = n1 + n2
        while s >= 0: # NOTE: = 0 to handle edge case 0 + 0
            cur.next = ListNode(s % 10, None)
            s = s // 10
            if s == 0: # NOTE: exit early!!!
                break
            cur = cur.next
        return dummy.next









