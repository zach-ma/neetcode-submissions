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
        '''
        my soln: hash map, two pass
        LESSON: can use 
        '''
        # if not head:
        #     return None

        # old_m = {}
        # old = head
        # idx = 0
        # while old:
        #     old_m[old] = idx
        #     idx += 1
        #     old = old.next
        
        # # val
        # new_l = []
        # old = head
        # while old:
        #     new_l.append(Node(old.val, None, None))
        #     old = old.next
        
        # old = head
        # i = 0
        # while old:
        #     # next
        #     if i < len(new_l) - 1:
        #         new_l[i].next = new_l[i + 1]

        #     # random
        #     if old.random:
        #         idx = old_m[old.random]
        #         new_l[i].random = new_l[idx]
        #     else:
        #         new_l[i].random = None
            
        #     i += 1
        #     old = old.next
        # return new_l[0]

        ''' REDO?????
        1. Recursion + Hash Map
        We must create a deep copy of a linked list where each node has both next and random pointers.
        The main difficulty: multiple nodes may point to the same random node, so we must ensure each original node is copied exactly once.

        A hash map helps us remember the copied version of each original node.
        Using recursion, we:

            copy the current node,
            store it in the map,
            recursively copy its next,
            link its random using the map.
        T: O(n)
        S: O(n)
        '''
    #     if head is None:
    #         return None
    #     if head in self.map:
    #         return self.map[head]
        
    #     copy = Node(head.val)
    #     self.map[head] = copy
    #     copy.next = self.copyRandomList(head.next)
    #     # copy.random = self.map[head.random] # NOTE: dict[key] raises key error for missing keys!!!!!
    #     copy.random = self.map.get(head.random) # NOTE: dict.get(key) returns None for missing keys
    #     return copy
    # def __init__(self): # NOTE: setup global map
    #     self.map = {}


        ''' REDO!!!!!!
        2. Hash Map (Two Pass)
            Pass 1: Create a copy of every node (just values), and store the mapping: original_node → copied_node
            Pass 2: Use this map to connect next and random pointers for each copied node.
        '''
        # oldToCopy = {None: None} # NOTE: Include null -> null for convenience.!!!!!!!!
        # cur = head
        # while cur:
        #     copy = Node(cur.val)
        #     oldToCopy[cur] = copy
        #     cur = cur.next
        
        # cur = head
        # while cur:
        #     copy = oldToCopy[cur]
        #     copy.next = oldToCopy[cur.next] # NOTE: pass by reference!!!
        #     copy.random = oldToCopy[cur.random]
        #     cur = cur.next
        # return oldToCopy[head]
        
        ''' REDO!!!
        3. Hash Map (One Pass)
        NOTE: defaultdict(lambda: Node(0)) creates a new Node automatically!!!
        Because of this behavior, the line oldToCopy[cur.random] works even if the random pointer jumps 10 nodes ahead
            into "uncharted territory." The defaultdict just spawns that future node early, and when your while loop
            eventually reaches that node's position in the original list, it simply fills in the .val for the node
            that was already created.
        '''
        oldToCopy = defaultdict(lambda: Node(0)) # CRITICAL!!!!!
        oldToCopy[None] = None

        cur = head
        while cur:
            oldToCopy[cur].val = cur.val
            oldToCopy[cur].next = oldToCopy[cur.next]
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]


        '''
        4. Space Optimized - I
        '''
        
        '''
        5. Space Optimized - II
        '''








