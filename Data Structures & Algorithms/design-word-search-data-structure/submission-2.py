'''my failed soln
'''
# class WordDictionary:
#     def __init__(self):
#         self.wordmap = {}

#     def addWord(self, word: str) -> None:
#         cur = self.wordmap
#         for c in word:
#             if c not in cur:
#                 cur[c] = {}
#             cur = cur[c]
#         cur['#'] = {}

#     def search(self, word: str) -> bool:
#         cur = self.wordmap
#         for c in word:
#             if c not in cur:
#                 return False
#             cur = cur[c]
#         if '#' in cur:
#             return True
#         return False

'''neet
'''

# NOTE: important to add customized TrieNode() 
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    # try every possible child, advancing to the next character
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        return dfs(0, self.root)


        

        
