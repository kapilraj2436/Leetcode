class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.data.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.data:
            front = self.data[0]
            self.data =  self.data[1:]
            return front
        else:
            print('Queue is already empty')

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.data:
            return self.data[0]
        else:
            print('Queue is empty')
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if self.data else True


# Your MyQueue object will be instantiated and called as such:

#Explanation
myQueue = MyQueue()
print(myQueue.push(1)) # queue is: [1]
print(myQueue.push(2)) # queue is: [1, 2] (leftmost is front of the queue)
print(myQueue.peek()) # return 1
print(myQueue.pop()) # return 1, queue is [2]
print(myQueue.empty()) 
