class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        1. Iterative Binary Search (my soln)
        '''
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     mid = l + (r - l) // 2
        #     if nums[mid] < target:
        #         l = mid + 1
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         return mid
        # return -1
        
        '''
        2. Recursive Binary Search
        '''
        def bst(l, r, nums):
            if not nums[l:r+1]:
                return -1
            mid = l + (r - l) // 2
            if nums[mid] < target:
                return bst(mid + 1, r, nums)
            elif nums[mid] > target:
                return bst(l, mid - 1, nums)
            else:
                return mid
        return bst(0, len(nums) - 1, nums)


        
        '''
        3. Upper Bound
        '''
        
        '''
        4. Lower Bound
        '''

        '''
        5. Built-In Function
        '''
