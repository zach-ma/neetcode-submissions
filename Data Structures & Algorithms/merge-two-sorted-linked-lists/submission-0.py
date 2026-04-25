# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        '''
        arr = []
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val <= p2.val:
                arr.append(p1.val)
                p1 = p1.next
            else:
                arr.append(p2.val)
                p2 = p2.next
        while p1:
            arr.append(p1.val)
            p1 = p1.next
        while p2:
            arr.append(p2.val)
            p2 = p2.next
        newHead = None
        newTail = None
        for val in arr:
            if not newHead:
                newHead = ListNode(val, None)
                newTail = newHead
            else:
                newTail.next = ListNode(val, None)
                newTail = newTail.next
        return newHead




