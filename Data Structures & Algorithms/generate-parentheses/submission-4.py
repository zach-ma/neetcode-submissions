class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''my failed soln (don't know why fail)
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
        '''my soln (after trial and error, 36mins)
        idea: backtrack + string (NOT space efficient)!!!
        '''
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
        
        '''neet: backtrack + stack (more space efficient)
        '''
        res = []
        stack = []
        def dfs(openN, closedN):
            # 1. only add open parenthesis if openN < n
            # 2. only add a closing parenthesis if closedN < openN
            # 3. valid IFF openN == closedN == n

            # base case:
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                dfs(openN + 1, closedN)
                stack.pop() # clean up once
            
            if closedN < openN:
                stack.append(")")
                dfs(openN, closedN + 1)
                stack.pop() # clean up twice!!!!!??????
                '''
stack is shared by every recursive call, so each call must undo its own change before it returns.

Each branch follows the same pattern:
1. Add a character to stack.
2. Explore that branch recursively.
3. Remove the character that branch added.
The first pop() undoes the "(" branch. The second pop() undoes the ")" branch. They don’t both run for every path; each runs only if its corresponding if branch runs.

For example, when both choices are available, the "(" branch runs first. Its recursive calls restore their own changes, then this call pops "(". Next the ")" branch runs, and this call pops ")" afterward. That leaves stack exactly as it was when this call started, ready for its caller or the next branch.
                '''

        dfs(0, 0)
        return res