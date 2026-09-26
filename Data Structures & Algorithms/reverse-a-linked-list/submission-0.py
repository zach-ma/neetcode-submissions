# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''my wrong soln: use three pointers
        '''
        # if not head:
        #     return head
        # prev, curr, next = None, head, None
        # while curr and curr.next:
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
        # return curr
        if not head:
            return head
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        