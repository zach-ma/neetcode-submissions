# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        1.0 BFS(my soln)
        '''
        # res = []
        # if not root:
        #     return res

        # q = deque([root])
        # while q:
        #     curLevel = []
        #     curSize = len(q)
        #     for i in range(curSize):
        #         node = q.popleft()
        #         curLevel.append(node.val)

        #         if node.left: # NOTE: redundant checking, can check if node instead
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #         if i == curSize - 1: # NOTE: can move out of for loop
        #             res.append(curLevel)
        # return res

        ''' REDO!!!! 
        1.1 BFS
        '''
        res = []
        q = deque([root])
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
                    
        ''' REDO!!!! can't solve!
        2. DFS
        '''
        # def dfs()














            
            

