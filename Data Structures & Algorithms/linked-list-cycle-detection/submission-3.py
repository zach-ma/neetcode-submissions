# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        1. Hash Set
        '''
        hs = set()
        node = head
        while node:
            if node in hs:
                return True
            hs.add(node)
            node = node.next
        return False

        
        ''' REDO!!
        2.0 Fast And Slow Pointers (my soln)
        '''
        # if not head:
        #     return False
        # slow, fast = head, head.next # NOTE: important to init fast to be ahead at the beginning
        # while fast:
        #     if not fast.next:
        #         return False
        #     if slow == fast:
        #         return True
        #     slow = slow.next
        #     fast = fast.next.next
        # return False