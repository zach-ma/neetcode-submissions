class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        2.1 Backtracking (my soln after trial and error)
        '''
        # res = []
        # def recurse(opening, closing, cur):
        #     if opening == n and closing == n:
        #         res.append(''.join(cur.copy()))
        #         return
        #     if opening < n:
        #         cur.append('(')
        #         recurse(opening+1, closing, cur)
        #         cur.pop()
        #     if opening > closing:
        #         cur.append(')')
        #         recurse(opening, closing+1, cur)
        #         cur.pop()
            
        # recurse(0, 0, [])
        # return res
        ''' REDO!!!!
        2.2 Backtracking
        - only add open parenthesis if openN < n
        - only add closed parenthesis if openN > closedN
        - valid IFF openN == closedN == n
        '''
        res = []
        stack = [] # NOTE: use glocal var so we don't have to pass in cur!!!!

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append(''.join(stack))
                return
            
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()
                
            if openN > closedN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)

        return res

        ''' REDO???
        3. Dynamic Programming
        '''



        









