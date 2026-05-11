# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # if not root:
        #     return res
        
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if i == 0:
        #             res.append(node.val)
        #         if node.right:
        #             q.append(node.right)
        #         if node.left:
        #             q.append(node.left)
        # return res
        res = []
        def dfs(node, level):
            if not node:
                return
            if level == len(res):
                res.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 0)
        return res












