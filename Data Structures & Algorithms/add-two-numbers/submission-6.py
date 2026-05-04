# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1.0 my soln: iterative
        '''
        # n1, n2 = 0, 0
        
        # cur = l1
        # digit = 0
        # while cur:
        #     n1 += cur.val * (10 ** digit)
        #     digit += 1
        #     cur = cur.next
        
        # cur = l2
        # digit = 0
        # while cur:
        #     n2 += cur.val * (10 ** digit)
        #     digit += 1
        #     cur = cur.next

        # dummy = ListNode()
        # cur = dummy
        # s = n1 + n2
        # while s >= 0: # NOTE: = 0 to handle edge case 0 + 0
        #     cur.next = ListNode(s % 10, None)
        #     s = s // 10
        #     if s == 0: # NOTE: exit early!!!
        #         break
        #     cur = cur.next
        # return dummy.next

        ''' REDO!!!!
        1.1 iteration (with carry propagation)
        '''
        # dummy = ListNode()
        # cur = dummy

        # carry = 0
        # while l1 or l2 or carry: # NOTE: check condition carry to handle edge case like 7+8=15 !!!!
        #     v1 = l1.val if l1 else 0
        #     v2 = l2.val if l2 else 0

        #     # new digit
        #     val = v1 + v2 + carry # NOTE: critical!!!!
        #     carry = val // 10
        #     val = val % 10
        #     cur.next = ListNode(val)
            
        #     # update ptrs
        #     cur = cur.next
        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None

        # return dummy.next

        '''
        2. recursion
        '''
        def add(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return None

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry # NOTE: critical!!!

            # update
            carry = val // 10
            val = val % 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            return ListNode(val, add(l1, l2, carry))
            
        return add(l1, l2, 0)










