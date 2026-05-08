
class Node: # doubly linked list
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


