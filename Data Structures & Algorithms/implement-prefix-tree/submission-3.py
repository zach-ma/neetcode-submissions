
class PrefixTree:
    '''
    my soln: hashmap without trie node class
    '''
    # def __init__(self):
    #     self.head = {}

    # def insert(self, word: str) -> None:
    #     ptr = self.head
    #     for c in word:
    #         if c not in ptr:
    #             ptr[c] = {}
    #         ptr = ptr[c]
    #     ptr['/'] = {}
    #     return None

    # def search(self, word: str) -> bool:
    #     ptr = self.head
    #     for c in word:
    #         if c not in ptr:
    #             return False
    #         ptr = ptr[c]
    #     if '/' in ptr:
    #         return True
    #     return False

    # def startsWith(self, prefix: str) -> bool:
    #     ptr = self.head
    #     for c in prefix:
    #         if c not in ptr:
    #             return False
    #         ptr = ptr[c]
    #     return True
    '''neetcode: use TrieNode class
    '''
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False # NOTE: critical to add the attr endOfWord
        
        