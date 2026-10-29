# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = []
        second = []
        
        cur = head
        while cur:
            first.append(cur)
            cur = cur.next
        
        for _ in range(len(first) // 2):
            second.append(first.pop())
        
        first.append(None)
        second.append(None)

        for i in range(len(first)):
            if first[i]:
                first[i].next = second[i]
            if i + 1 < len(first) and second[i]:
                second[i].next = first[i + 1]
        


                

