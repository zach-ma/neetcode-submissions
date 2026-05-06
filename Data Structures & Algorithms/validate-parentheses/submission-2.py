class Solution:
    def isValid(self, s: str) -> bool:
        ''' REDO!!! 
        1. burte force
        intuition: (interesting!!!)
            valid parentheses must always appear in matching pairs like "()", "{}", or "[]"
            So if the string is valid, we can repeatedly remove these matching pairs until nothing is left.
        '''
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
        '''
        '''
        stack = []
        m = {')':'(',
            '}':'{',
            ']':'['}
        for c in s:
            if c in m.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if m[c] != popped:
                    return False
        return not stack

                