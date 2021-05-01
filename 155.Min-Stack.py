class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        

    def push(self, val: int) -> None:
        self.data.append(val)
        

    def pop(self) -> None:
        
        if self.data:
            front = self.data[-1]
            self.data =  self.data[:-1]
            return front
        else:
            print('stack is already empty')
        

    def top(self) -> int:
        if self.data:
            return self.data[-1]
        else:
            print('Stack is empty')
        

    def getMin(self) -> int:
        if  self.data:
            return min(self.data)
        


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
print(minStack.pop())
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2
