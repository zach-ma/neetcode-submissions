class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = 0
        for n in nums:
            if cur < 0:
                return False
            if n > cur:
                cur = n
            cur -= 1
        return True