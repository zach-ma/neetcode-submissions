class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        1.0 my soln: binary search
        '''
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     if nums[l] < nums[r]: # sorted
        #         return nums[l]
        #     else: #  nums[l] > nums[r] => rotated
        #         m = l + (r - l) // 2
        #         if nums[l] < nums[m]:
        #             l = m + 1
        #         else:
        #             l = l + 1
        #             r = m
        # return nums[l]

        '''
        1.1 Binary Search
        key question: is nums[m] currently in left sorted portion or in right sorted portion? if it's in left sorted portion, we want to search to the right sorted portion
        key observation: every value in right sorted portion is smaller than any value in the left sorted portion
            => nums[m] >= nums[l] > nums[r] ==> nums[m] is in left sorted portion ==> want to search to the right
        '''
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] <= nums[r]: # sorted
                res = min(res, nums[l])
                break
            m = l + (r - l) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]: # nums[m] is part of the left sorted portion
                l = m + 1
            else:
                r = m
        return res











            
