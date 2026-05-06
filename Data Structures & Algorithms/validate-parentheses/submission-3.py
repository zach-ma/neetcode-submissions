class Solution:
    def isValid(self, s: str) -> bool:
        ''' REDO!!! 
        1. burte force
        intuition: (interesting!!!)
            valid parentheses must always appear in matching pairs like "()", "{}", or "[]"
            So if the string is valid, we can repeatedly remove these matching pairs until nothing is left.
        
        T: O(n^2)!!!!
        S: O(n)
        '''
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        # return s == ''

        '''
        2.0 Stack (my soln)
        LESSON: can merge two false return into one!!!

        T: O(n)
        S: O(n)
        '''
        # stack = []
        # m = {')':'(',
        #     '}':'{',
        #     ']':'['}
        # for c in s:
        #     if c in m.values():
        #         stack.append(c)
        #     else:
        #         if not stack:
        #             return False
        #         popped = stack.pop()
        #         if m[c] != popped:
        #             return False
        # return not stack

        ''' REDO!
        2.1 Stack
        T: O(n)
        S: O(n)
        '''
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: # NOTE: better implementation!!!
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

                