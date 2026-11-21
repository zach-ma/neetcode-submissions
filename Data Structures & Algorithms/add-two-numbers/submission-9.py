# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        m, n = 0, 0
        while p1:
            p1 = p1.next
            m += 1
        while p2:
            p2 = p2.next
            n += 1
        
        p1, p2 = l1, l2 # reset
        
        res = ListNode()
        cur = res
        carry = 0
        while p1 and p2:
            combined = p1.val + p2.val + carry
            carry = 0
            if combined >= 10:
                carry = 1
            cur.next = ListNode(combined % 10)
            p1, p2 = p1.next, p2.next
            cur = cur.next
        
        rest = p1 if p1 else (p2 if p2 else None)
        while rest:
            combined = rest.val + carry
            carry = 0
            if combined >= 10:
                carry = 1
            cur.next = ListNode(combined % 10)
            rest = rest.next
            cur = cur.next
        
        if carry == 1:
            cur.next = ListNode(1)

        # while m > n:
        #     cur.next = ListNode(p1.val)
        #     p1 = p1.next
        #     cur = cur.next
        #     m -= 1
        # while m < n:
        #     cur.next = ListNode(p2.val)
        #     p2 = p2.next
        #     cur = cur.next
        #     n -= 1
        
        

        return res.next















