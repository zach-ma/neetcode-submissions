class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        for t in tokens:
            if t in ops:
                n2 = stack.pop()
                n1 = stack.pop()
                res = 0
                if t == '+':
                    res = n1 + n2
                if t == '-':
                    res = n1 - n2
                if t == '*':
                    res = n1 * n2
                if t == '/':
                    res = int(n1 / n2)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[-1]

