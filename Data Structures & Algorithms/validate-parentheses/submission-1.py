class Solution:
    def isValid(self, s: str) -> bool:
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

                