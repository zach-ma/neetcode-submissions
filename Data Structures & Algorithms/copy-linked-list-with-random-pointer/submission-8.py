"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''my soln after hint
        lesson:
            - forgot Null check to prevent oldToNew[old.next] when old.next == None
        '''
        # if not head:
        #     return None

        # oldToNew = {} # oldNode -> newNode
        
        # # init
        # cur = head
        # while cur:
        #     oldToNew[cur] = Node(cur.val, None, None)
        #     cur = cur.next
        
        # # set .next and .random
        # for old, new in oldToNew.items():
        #     if old.next is None: # CRITICAL: must check to prevent oldToNew[old.next] when old.next == None
        #         new.next = None
        #     else:
        #         new.next = oldToNew[old.next]
            
        #     if old.random is None:
        #         new.random = None
        #     else:
        #         new.random = oldToNew[old.random]
        # return oldToNew[head]
        '''neet
        '''
        oldToCopy = {None: None} # SMART!!!!

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]


