class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        4.1 Stack
        '''
        # stack = []
        # for t in tokens:
        #     if t in {'+', '-', '*', '/'}:
        #         b = stack.pop() # NOTE: order matters!!!
        #         a = stack.pop()
        #         if t == '+':
        #             stack.append(a + b)
        #         elif t == '-':
        #             stack.append(a - b)
        #         elif t == '*':
        #             stack.append(a * b)
        #         elif t == '/': # NOTE: can use int() instead of manually!!!
        #             if (a > 0 and b > 0) or (a < 0 and b < 0):
        #                 stack.append(abs(a) // abs(b))
        #             else:
        #                 stack.append(-(abs(a) // abs(b)))
        #     else:
        #         stack.append(int(t))
        # return stack[0]

        '''
        4.2 Stack
        '''
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a)) # NOTE: use int() to round towards zero!!!!! 
            else:
                stack.append(int(c))
        return stack[0]
        