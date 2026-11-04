# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        q = deque([])
        cur = head
        while cur:
            q.append(cur)
            if len(q) > n + 1:
                q.popleft()
            cur = cur.next
        # if len(q) > 1:
        #     q[0].next = q[1].next
        # else:
        #     head = None
        # return head
        if len(q) <= n:  # target is the head
            return head.next if head else None

        q[0].next = q[1].next
        return head