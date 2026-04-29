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
        if not head:
            return None

        old_m = {}
        old = head
        idx = 0
        while old:
            old_m[old] = idx
            idx += 1
            old = old.next
        
        # val
        new_l = []
        old = head
        while old:
            new_l.append(Node(old.val, None, None))
            old = old.next
        
        old = head
        i = 0
        while old:
            # next
            if i < len(new_l) - 1:
                new_l[i].next = new_l[i + 1]

            # random
            if old.random:
                idx = old_m[old.random]
                new_l[i].random = new_l[idx]
            else:
                new_l[i].random = None
            
            i += 1
            old = old.next
        return new_l[0]














