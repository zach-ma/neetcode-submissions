''' REDO!!!!
1. Doubly Linked List

    Intuition

    We want all operations to be O(1) while still following LRU (Least Recently Used) rules.

    To do that, we combine:

        Hash Map -> quickly find a node by its key in O(1).
        Doubly Linked List -> quickly move nodes to the most recently used position and remove the least recently used node from the other end in O(1).

    We keep:

        The most recently used node near the right side.
        The least recently used node near the left side.

    Whenever we:

        Get a key: move that node to the right (most recently used).
        Put a key:
            If it exists: update value and move it to the right.
            If it's new:
                If at capacity: remove the leftmost real node (LRU).
                Insert the new node at the right.

    Dummy left and right nodes make insert/remove logic cleaner.
'''

class Node: # customized doubly linked list node
    def __init__(self, key = 0, val = 0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> node

        # left=LRU, right=most recent
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left
    
    # remove from list
    def _remove(self, node): # NOTE: hard to implement!!!!
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def _insert(self, node): # NOTE: hard to implement!!!!
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            self._remove(node)
            self._insert(node)

            return node.val
        return -1

    def put(self, key: int, value: int) -> None: # NOTE: hard to implement!!!!
        if key in self.cache: # key exists
            node = self.cache[key]
            self._remove(node)
        elif len(self.cache) == self.cap: # reached cap  
            # evict LRU
            lru = self.left.next # NOTE: .next!!!!!
            self._remove(lru)
            del self.cache[lru.key] # NOTE: delete from hashmap, lru.key is why we also store key inside node

        # insert as MRU
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert(new_node)


