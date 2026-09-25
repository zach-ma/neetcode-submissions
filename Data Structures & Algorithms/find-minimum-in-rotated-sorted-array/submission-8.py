class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            else:
                m = l + (r - l) // 2
                res = min(res, nums[m])
                if nums[l] <= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return res


        # while l <= r:
        #     if l == r:
        #         return l
        #     m = l + (r - l) // 2
        #     if nums[l] <= nums[m] <= nums[r]: # sorted
        #         return l
        #     elif nums[l] <= nums[m]: # m is in the left sorted portion
        #         l = m + 1
        #     elif nums[l] > nums[m]: # m is in the right sorted portion
        #         r = m
        

