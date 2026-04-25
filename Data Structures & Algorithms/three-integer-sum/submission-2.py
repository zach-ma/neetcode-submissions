class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        my wrong soln
        '''
        # def twoSum(nums, target):
        #     s = set() # stores curr
        #     for i in range(len(nums)):
        #         curr = nums[i]
        #         compl = target - curr
        #         if compl in s:
        #             return [curr, compl]
        #         else:
        #             s.add(curr)
        #     return []
        
        # res = set()
        # for i in range(len(nums)-2):
        #     compl = 0 - nums[i]
        #     two = twoSum(nums[:i] + nums[i+1:], compl)
        #     if two:
        #         res.add(tuple(sorted([nums[i]] + two)))
        # return list(res)

        ''' REDO !!!
        1. brute force
        T: O(n^3)
        S: O(m), where m is the number of triplets and n is the length of the given array
        '''
        # res = set()
        # nums.sort() # NOTE: sort to avoid duplicates
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 tmp = [nums[i], nums[j], nums[k]]
        #                 res.add(tuple(tmp)) # NOTE: must use tuple to be hashable!!!!
        # return [list(t) for t in res]

        '''
        2. two pointers
        - sort
        - fix one number, apply twoSumII to the rest
        '''
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]: # NOTE: avoid reusing the same value
                continue

            # now apply twoSumII
            l, r = i + 1, len(nums) - 1 # NOTE: i + 1 because we are fixing pos i
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # ???????? DON't UNDERSTAND!!!!
                    # to avoid adding the same triplet
                    while nums[l] == nums[l - 1] and l < r: 
                        l += 1
                    while nums[r] == nums[r + 1] and l < r: 
                        r -= 1
        return res




        ''' REDO?????
        3. hash map: fix two (temporarily reduce their counts in the map so we don't reuse them), then find the third
        '''
        # nums.sort() # why??????
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1
        
        # res = []
        # for i in range(len(nums)):
        #     count[nums[i]] -= 1
        #     if i and nums[i] == nums[i - 1]:
        #         continue
            
        #     for j in range(i + 1, len(nums)):
        #         count[nums[j]] -= 1
        #         if 











