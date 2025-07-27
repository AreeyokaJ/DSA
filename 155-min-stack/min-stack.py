class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []
    

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        # self.min_stack.append(val if (self.min_stack and  val < self.min_stack[0]) or (not self.min_stack)) else self.min_stack[0])
        self.min_stack.append(val if not self.min_stack else min(val, self.min_stack[-1]))
        

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()