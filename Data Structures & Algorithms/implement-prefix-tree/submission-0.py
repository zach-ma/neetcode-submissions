class PrefixTree:
    # class Node:
    #     def __init__(self, char):
    #         self.char = cur
    #         self.next_char = {}

    def __init__(self):
        self.head = {}

    def insert(self, word: str) -> None:
        ptr = self.head
        for c in word:
            if c not in ptr:
                ptr[c] = {}
            ptr = ptr[c]
        ptr['/'] = {}
        return None

    def search(self, word: str) -> bool:
        ptr = self.head
        for c in word:
            if c not in ptr:
                return False
            ptr = ptr[c]
        if '/' in ptr:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        ptr = self.head
        for c in prefix:
            if c not in ptr:
                return False
            ptr = ptr[c]
        return True
        
        