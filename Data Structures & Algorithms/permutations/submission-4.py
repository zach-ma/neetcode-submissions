class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''my soln
        '''
        # res = []
        # def dfs(cur, options):
        #     if not options:
        #         res.append(cur.copy())
        #         return
        #     for i in range(len(options)):
        #         dfs(cur + [options[i]], options[:i] + options[i + 1:])
        
        # dfs([], nums)
        # return res

        '''neet1: recursive
        '''
        # if len(nums) == 0:
        #     return [[]]

        # perms = self.permute(nums[1:]) # recursively get all permutations the remaining numbers
        
        # # for each smaller permutation, insert the first number into every possible position
        # res = []
        # for p in perms:
        #     for i in range(len(p) + 1):
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)
        # return res


        '''neet2: iterative
        '''
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        return new_perms


        # if len(nums) == 0:
        #     return [[]]

        # perms = self.permute(nums[1:]) # recursively get all permutations the remaining numbers
        
        # # for each smaller permutation, insert the first number into every possible position
        # res = []
        # for p in perms:
        #     for i in range(len(p) + 1):
        #         p_copy = p.copy()
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)
        # return res













