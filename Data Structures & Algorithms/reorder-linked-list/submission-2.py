# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''my soln
        M: O(n) can be optimized to O(1)!!!
        '''
        # first = []
        # second = []
        
        # cur = head
        # while cur:
        #     first.append(cur)
        #     cur = cur.next
        
        # for _ in range(len(first) // 2):
        #     second.append(first.pop())
        
        # first.append(None)
        # second.append(None)

        # for i in range(len(first)):
        #     if first[i]:
        #         first[i].next = second[i]
        #     if i + 1 < len(first) and second[i]:
        #         second[i].next = first[i + 1]
        '''neet
        '''
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None # CRITICAL!!!

        # reverse second half
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev # CRITICAL!!!

        # merge two halves
        while second:
            nxt1, nxt2 = head.next, second.next
            head.next = second
            second.next = nxt1
            head, second = nxt1, nxt2
        








        


                

