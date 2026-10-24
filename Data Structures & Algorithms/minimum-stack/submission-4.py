class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curMin = val
        if self.stack:
            curMin = min(curMin, self.stack[-1][1])
        self.stack.append([val, curMin])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]