class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float('inf')


    def push(self, val: int) -> None:
        if self.stack == []:
            self.minVal = val
        else:
            self.minVal = min(self.minVal,val)
        self.stack += [[val,self.minVal]]

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        if self.stack != []:
            self.minVal = self.stack[-1][1]
        else:
            self.minVal = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]


    def getMin(self) -> int:
        return self.stack[-1][1]
