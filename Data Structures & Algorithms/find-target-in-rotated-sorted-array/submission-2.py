class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ''' REDO!!!
        1.0 binary search, one pass (my soln) 
        PROBLEM:
            - TOO long, need to condense!!!!
            - should use l <= r, not <, to handle target == nums[l] case automatically!!!
            - no need to explicitly handle "sorted" case
        '''
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     m = l + (r - l) // 2
        #     if target == nums[m]:
        #         return m
            
        #     if nums[l] < nums[r]: # sorted
        #         if target > nums[m]:
        #             l = l + 1
        #         else:
        #             r = r - 1
        #     else: # rotated (nums[l] > nums[r])
        #         if nums[l] <= nums[m]: # m in left half
        #             if target > nums[m]:
        #                 l = m + 1
        #             else:
        #                 if target >= nums[l]: # target in left half
        #                     r = m - 1
        #                 else: # target in right half
        #                     l = m + 1
        #         if nums[m] <= nums[r]: # m in right half
        #             if target > nums[m]:
        #                 if target <= nums[r]: # target in right half
        #                     l = m + 1
        #                 else:
        #                     r = m - 1
        #             else:
        #                 r = m - 1
        # return l if nums[l] == target else -1

        ''' REDO!!!
        1.1 binary search, one pass
        HIGHLIGHT: cases are condensed!!!!
        '''
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m
            
            if nums[m] >= nums[l]: # left sorted portion
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else: # right sorted portion
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

                
            





        ''' REDO!!!!
        2. binary search, two pass

        Intuition

        A rotated sorted array is really two sorted arrays stuck together.
        So we break the problem into two simple binary searches:

            1. First binary search:
            Find the pivot — the index of the smallest element.
            This tells us where the array was rotated.

            2. Second binary search:
            Decide which sorted half may contain the target,
            then run a standard binary search only on that half.
        '''

            