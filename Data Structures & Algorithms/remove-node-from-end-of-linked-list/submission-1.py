# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        1. Brute Force
        We store all nodes in an array so we can directly access the node that is n positions from the end.
        Once we know which node to delete, we simply adjust the next pointer of the previous node.
        '''
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        removeIndex = len(nodes) - n
        if removeIndex == 0:
            head = head.next
            return head
        nodes[removeIndex - 1].next = nodes[removeIndex].next
        return head
        



        # size = 0
        # cur = head
        # while cur:
        #     size += 1
        #     cur = cur.next
        
        # cur = head
        # while size > n + 1:
        #     size -= 1
        #     cur = cur.next
        # if cur and cur.next:
        #     tmp = cur.next
        #     cur.next = cur.next.next
        #     tmp.next = None
        
        # return head