class MinStack:

    def __init__(self):
        self.result = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.result.append(val)
        if self.minStack:
            val = min(val, minStack[-1])
        else:
            val = val 
        self.minStack.append(val)  

    def pop(self) -> None:
        self.result.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.result[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

