# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        1. Hash Set
        T: O(n)
        S: O(n)
        '''
        seen = set()
        cur = head
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False

        
        ''' REDO!!
        2.0 Fast And Slow Pointers (my soln)
        WHAT TO IMPROVE:
            1. can update fast and slow at the beginning of the loop to avoid initializing fast to be ahead of slow !!!
            2. can merge fast.next check to while condition check!!!
        '''
        # if not head:
        #     return False
        # # NOTE: important to init fast to be ahead at the beginning, if not update fast and slow at the beginning of the loop!!!!!!
        # slow, fast = head, head.next 
        # while fast:
        #     if not fast.next:
        #         return False
        #     if slow == fast:
        #         return True
        #     slow = slow.next
        #     fast = fast.next.next
        # return False

        '''
        2.0 Fast And Slow Pointers
        T: O(n)
        S: O(1)
        '''
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False




