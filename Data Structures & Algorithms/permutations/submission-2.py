class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(perm, options):
            if not options:
                res.append(perm.copy())
                return
            for i in range(len(options)):
                dfs(perm + [options[i]], options[:i] + options[i + 1:])
        
        dfs([], nums)
        return res