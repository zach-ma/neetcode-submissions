class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ''' REDO????
        1. Recursion
        For each smaller permutation, insert the first number into every possible position.
        
        T: O(n! * n^2)?????
        S: O(n! * n)
        '''
        # if len(nums) == 0:
        #     return [[]]

        # perms = self.permute(nums[1:])
        # res = []
        # for p in perms:
        #     for i in range(len(p) + 1):
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)
        # return res

        ''' REDO???
        2. Iteration
        '''

        '''
        3.1 Backtracking (my soln, I think mine is clearer)
        '''
        # res = []
        # def backtrack(cur, candidates):
        #     if not candidates:
        #         res.append(cur.copy())
        #         return
        #     for i in range(len(candidates)):
        #         cur.append(candidates[i])
        #         backtrack(cur, candidates[:i]+candidates[i+1:])
        #         cur.pop()

        # backtrack([], nums)
        # return res


        ''' REDO?????
        3.2 Backtracking
        Intuition

        Backtracking builds permutations by choosing numbers one-by-one and exploring all possible orders.

        At every step:

            We pick a number that has not been used yet.
            Add it to the current permutation.
            Recursively continue building.
            When we reach a full permutation (length == len(nums)), we save it.
            Then we undo the last choice (backtrack) and try a different number.

        We use a pick array to mark which elements are already used, ensuring each number appears only once per permutation.

        This method explores a decision tree where each level chooses the next number until all numbers are used.
        
        T: O(n! * n)?????
        S: O(n! * n)
        '''
        res = []
        def backtrack(perm, nums, pick):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    backtrack(perm, nums, pick)
                    perm.pop()
                    pick[i] = False
        backtrack([], nums, [False] * len(nums))
        return res


        '''
        4. Backtracking (Bit Mask)
        '''
        '''
        5. Backtracking (Optimal)
        '''












