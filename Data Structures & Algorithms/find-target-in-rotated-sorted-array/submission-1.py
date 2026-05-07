class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m
            
            if nums[l] < nums[r]: # sorted
                if target > nums[m]:
                    l = l + 1
                else:
                    r = r - 1
            else: # rotated (nums[l] > nums[r])
                if nums[l] <= nums[m]: # m in left half
                    if target > nums[m]:
                        l = m + 1
                    else:
                        if target >= nums[l]: # target in left half
                            r = m - 1
                        else: # target in right half
                            l = m + 1
                if nums[m] <= nums[r]: # m in right half
                    if target > nums[m]:
                        if target <= nums[r]: # target in right half
                            l = m + 1
                        else:
                            r = m - 1
                    else:
                        r = m - 1
        return l if nums[l] == target else -1

            