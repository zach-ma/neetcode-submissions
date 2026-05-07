class MinStack:
    '''REDO!!!!
    1. Two Stacks (prefix approach!!!)
    - keep a second stack that always stores the minimum value up to that point!!!!
    '''
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
    '''
    '''
    # def __init__(self):
    #     self.stack = []
    #     self.minStack = []

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     curMin = self.minStack[-1] if self.minStack else val
    #     self.minStack.append(min(curMin, val))

    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.minStack.pop()

    # def top(self) -> int:
    #     return self.stack[-1]
        

    # def getMin(self) -> int:
    #     return self.minStack[-1]
        
