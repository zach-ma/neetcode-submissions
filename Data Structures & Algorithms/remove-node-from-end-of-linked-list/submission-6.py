# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''my wrong soln
        '''
        # q = deque([])
        # cur = head
        # while cur:
        #     q.append(cur)
        #     if len(q) > n + 1:
        #         q.popleft()
        #     cur = cur.next
        # if len(q) > 1:
        #     q[0].next = q[1].next
        # else:
        #     head = None
        # return head
        '''neet
        '''
        dummy = ListNode(0, head)
        l, r = dummy, head
        i = 0
        while i < n:
            r = r.next
            i += 1
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next









