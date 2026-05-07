class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        curMin = self.prefix[-1] if self.prefix else val
        self.prefix.append(min(curMin, val))

    def pop(self) -> None:
        self.stack.pop()
        self.prefix.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefix[-1]
        
