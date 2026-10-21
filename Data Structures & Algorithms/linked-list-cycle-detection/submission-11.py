# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # ctnl1, ctnl2 = ListNode(), ListNode()
        # ctnl1.next, ctnl2.next = ctnl2, head
        # slow, fast = ctnl1, ctnl1.next.next
        # while fast and slow:
        #     if slow == fast:
        #         return True
        #     if fast.next:
        #         fast = fast.next.next
        #     if slow:
        #         slow = slow.next
        # return False
        slow, fast = head, head
        while fast:
            if fast.next:
                fast = fast.next.next
            else:
                return False
            slow = slow.next
            if slow == fast:
                return True
        return False
