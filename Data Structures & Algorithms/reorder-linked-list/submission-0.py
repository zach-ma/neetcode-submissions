# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ''' REDO!!!
        1. Brute Force: store all nodes in an array, then access using two pointers
        '''
        # nodes = []
        # curr = head
        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next
        
        # l, r = 0, len(nodes) - 1
        # while l < r:
        #     nodes[l].next = nodes[r]
        #     # if l + 1 < r:
        #     #     nodes[r].next = nodes[l + 1]
        #     # l += 1
        #     # r -= 1
        #     l += 1
        #     if l >= r:
        #         break
        #     nodes[r].next = nodes[l]
        #     r -= 1
        # nodes[l].next = None # NOTE: important to break circular reference!!!!!

        ''' REDO????
        2. Recursion
        '''

        ''' REDO!!!!
        3. Reverse And Merge
            1. Find the middle of the linked list using slow and fast pointers.
                This splits the list into two halves.
            2. Reverse the second half of the list.
                Doing this makes it easy to merge nodes from the front and back alternately.
            3. Merge the two halves one-by-one:
                Take one node from the first half (first), then one from the reversed second half (second), and repeat.
        '''

        # 1. Find the middle of the linked list using slow and fast pointers.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # 2. Reverse the second half of the list.
        second = slow.next
        slow.next = None # NOTE: splitting the list to two halves
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # 3. Merge the two halves one-by-one:
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        

        






