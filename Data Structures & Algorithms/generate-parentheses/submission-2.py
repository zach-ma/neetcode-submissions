# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = []
#         curr = ""
#         def dfs(opened, closed):
#             nonlocal curr
#             if opened == closed == n:
#                 return res.append(curr)
            
#             if opened == n:
#                 curr += ")"
#                 dfs(opened, closed + 1)
#             else:
#                 # inlcude "("
#                 curr += "("
#                 dfs(opened + 1, closed)
#                 curr = curr[:-1] # revert
#                 if opened > closed:
#                     curr += ")"
#                     dfs(opened, closed + 1)
            
#         dfs(0, 0)
#         return res

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(opened, closed, curr):

            if opened == closed == n:
                return res.append(curr)
            
            if opened == n:
                dfs(opened, closed + 1, curr + ")")
            else:
                # inlcude "("
                dfs(opened + 1, closed, curr + "(")
                
                # include ")"
                if opened > closed:
                    dfs(opened, closed + 1, curr + ")")

            
        dfs(0, 0, "")
        return res