class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                elif t == '/':
                    if (a > 0 and b > 0) or (a < 0 and b < 0):
                        stack.append(abs(a) // abs(b))
                    else:
                        stack.append(-(abs(a) // abs(b)))
            else:
                stack.append(int(t))
        return stack[0]

        