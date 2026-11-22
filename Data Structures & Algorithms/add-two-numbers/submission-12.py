# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''my soln after trial and error
        '''
        # p1, p2 = l1, l2
        # res = ListNode()
        # cur = res
        # carry = 0
        # while p1 and p2:
        #     combined = p1.val + p2.val + carry
        #     carry = 0
        #     if combined >= 10:
        #         carry = 1
        #     cur.next = ListNode(combined % 10)
        #     p1, p2 = p1.next, p2.next
        #     cur = cur.next
        
        # rest = p1 if p1 else (p2 if p2 else None)
        # while rest:
        #     combined = rest.val + carry
        #     carry = 0
        #     if combined >= 10:
        #         carry = 1
        #     cur.next = ListNode(combined % 10)
        #     rest = rest.next
        #     cur = cur.next
        
        # if carry == 1:
        #     cur.next = ListNode(1)

        # return res.next
        '''neet
        '''
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry: # CRITICAL: "or carry" condition is important to add to handle the case 7 + 8 = 15
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next















