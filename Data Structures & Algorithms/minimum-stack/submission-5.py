class MinStack:
    '''my soln after hint: 1 stack
    '''
    # def __init__(self):
    #     self.stack = []

    # def push(self, val: int) -> None:
    #     curMin = val
    #     if self.stack:
    #         curMin = min(curMin, self.stack[-1][1])
    #     self.stack.append([val, curMin])

    # def pop(self) -> None:
    #     self.stack.pop()

    # def top(self) -> int:
    #     if self.stack:
    #         return self.stack[-1][0]

    # def getMin(self) -> int:
    #     if self.stack:
    #         return self.stack[-1][1]
    '''neet: 2 stacks
    '''
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        curMin = val
        if self.minStack:
            curMin = min(val, self.minStack[-1])
        self.minStack.append(curMin)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]