class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''my soln: prefix & postfix
        lesson: uses O(n) memory, can be space optimized using output array!!!
        '''
        # pre, post = [0] * len(nums), [0] * len(nums)
        # prod = 1
        # for i in range(len(nums)):
        #     prod *= nums[i]
        #     pre[i] = prod

        # prod = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     prod *= nums[i]
        #     post[i] = prod
        
        # res = []
        # for i in range(len(nums)):
        #     prod = 1
        #     if i > 0:
        #         prod *= pre[i - 1]
        #     if i < len(nums) - 1:
        #         prod *= post[i + 1]
        #     res.append(prod)
        # return res
        '''neet
        '''
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res





        



