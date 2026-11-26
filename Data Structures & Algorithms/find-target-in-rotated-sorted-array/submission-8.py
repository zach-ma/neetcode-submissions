class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''my failed soln
        '''
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     m = l + (r - l) // 2
        #     print(m)
        #     if target > nums[m]:
        #         if target >= nums[l]:
        #             r = m - 1
        #         else:
        #             l = m + 1
        #     elif target < nums[m]:
        #         if target >= nums[l]:
        #             r = m - 1
        #         else:
        #             l = m + 1
        #     else:
        #         return m
        # return -1
        '''neet
        '''
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2

            if target == nums[mid]:
                return mid
            
            # left sorted portion
            if nums[mid] >= nums[l]:
                # if target > nums[mid]:
                #     l = mid + 1
                # elif target < nums[l]:
                #     l = mid + 1
                # NOTE: condensed from above
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            # right sorted portion
            else:
                # if target < nums[mid]:
                #     r = mid - 1
                # elif target >= nums[l]:
                #     r = mid - 1
                # NOTE: condensed from above
                if target < nums[mid] or target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
