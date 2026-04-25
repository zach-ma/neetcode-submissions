# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        my soln: iterative, requires extra arr!!!!!
        '''
        # arr = []
        # p1 = list1
        # p2 = list2
        # while p1 and p2:
        #     if p1.val <= p2.val:
        #         arr.append(p1.val)
        #         p1 = p1.next
        #     else:
        #         arr.append(p2.val)
        #         p2 = p2.next
        # while p1:
        #     arr.append(p1.val)
        #     p1 = p1.next
        # while p2:
        #     arr.append(p2.val)
        #     p2 = p2.next
        # newHead = None
        # newTail = None
        # for val in arr:
        #     if not newHead:
        #         newHead = ListNode(val, None)
        #         newTail = newHead
        #     else:
        #         newTail.next = ListNode(val, None)
        #         newTail = newTail.next
        # return newHead

        ''' REDO!!!!!
        iterative
        '''
        dummy = ListNode() # NOTE: create dummy node!!!!
        tail = dummy

        # compare
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next # update tail after both condition
        
        # take remainder
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next # NOTE: dummy.next!!!




