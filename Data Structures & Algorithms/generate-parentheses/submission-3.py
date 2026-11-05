class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        '''
        # res = []
        # curr = ""
        # def dfs(opened, closed):
        #     nonlocal curr
        #     if opened == closed == n:
        #         return res.append(curr)
            
        #     if opened == n:
        #         curr += ")"
        #         dfs(opened, closed + 1)
        #     else:
        #         # inlcude "("
        #         curr += "("
        #         dfs(opened + 1, closed)
        #         curr = curr[:-1] # revert
        #         if opened > closed:
        #             curr += ")"
        #             dfs(opened, closed + 1)
            
        # dfs(0, 0)
        # return res
        res = []
        def dfs(opened, closed, curr):
            # base case 1: complete
            if opened == closed == n:
                return res.append(curr)
            # base case 2: can only add close parenthesis
            if opened == n:
                dfs(opened, closed + 1, curr + ")")

            if opened < n:
                # choice 1: inlcude "("
                dfs(opened + 1, closed, curr + "(")
                
                # choice 2: include ")", only if there are open parenthesis not closed
                if opened > closed:
                    dfs(opened, closed + 1, curr + ")")

        dfs(0, 0, "")
        return res