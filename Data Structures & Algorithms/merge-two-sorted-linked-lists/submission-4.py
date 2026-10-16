# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        my soln
        lesson: condition too redundent, can be simplified
        '''
        # p1, p2 = list1, list2
        # dummy = ListNode()
        # cur = dummy
        # while p1 or p2:
        #     if p1 and p2:
        #         if p1.val <= p2.val:
        #             cur.next = p1
        #             p1 = p1.next
        #         else:
        #             cur.next = p2
        #             p2 = p2.next
        #         cur = cur.next
        #     else:
        #         if p1:
        #             cur.next = p1
        #         else:
        #             cur.next = p2
        #         break

        # return dummy.next
        
        '''neet
        '''
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next