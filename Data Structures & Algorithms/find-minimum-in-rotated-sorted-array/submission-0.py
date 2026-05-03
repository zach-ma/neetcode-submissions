class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]: # sorted
                return nums[l]
            else: #  nums[l] > nums[r] => rotated
                m = l + (r - l) // 2
                if nums[l] < nums[m]:
                    l = m + 1
                else:
                    l = l + 1
                    r = m
        return nums[l]
            
