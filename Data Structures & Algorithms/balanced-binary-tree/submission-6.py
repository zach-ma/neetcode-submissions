# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ''' REDO!!!
        1.0 brute force(my soln)
        '''
        # def height(node):
        #     if not node:
        #         # return 0
        #         return -1 # NOTE: critical!!!! count by edge not node
        #     # if not node.left and not node.right:
        #     #     return 0
        #     return 1 + max(height(node.left), height(node.right))
        
        # if not root:
        #     return True
        # sub = self.isBalanced(root.left) and self.isBalanced(root.right)
        # return abs(height(root.left) - height(root.right)) <= 1 and sub

        ''' REDO!!!
        1.1 brute force
        LESSON: top down, so repeated work => so bottom up instead to eliminate repeated work!!!!
        
        T: O(n^2)
        S: O(n)
        '''
        # def height(root):
        #     if not root:
        #         return 0 # NOTE!!!: neetcode didn't use -1, it's fine in this problem because we only need diff, not actual height
        #     return 1 + max(height(root.left), height(root.right))
        
        # if not root:
        #     return True
        # left = height(root.left)
        # right = height(root.right)
        # if abs(left - right) > 1:
        #     return False
        # return self.isBalanced(root.left) and self.isBalanced(root.right)

        ''' REDO!!!!!!!!
        2. DFS (bottom up)
        - The brute-force solution wastes time by repeatedly recomputing subtree heights.
        - fix by doing one DFS that returns [isBlanaced, height] => each subtree is processed only once.
        T: O(n)
        S: O(h), best O(logn), worst O(n)
        '''
        def dfs(root): # returns [is_balanced, height]
            if not root:
                return [True, 0] # NOTE!!!: neetcode didn't use -1, it's fine in this problem because we only need diff, not actual height
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
        