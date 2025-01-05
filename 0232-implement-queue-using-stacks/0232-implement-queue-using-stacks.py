class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, x: int) -> None:
        self.stack1.append(x)
    def pop(self) -> int:
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())

        pop_element = self.stack2.pop()

        while len(self.stack2):
            self.stack1.append(self.stack2.pop())

        return pop_element

    def peek(self) -> int:
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
        peek_element = self.stack2.pop()
        self.stack1.append(peek_element)

        while len(self.stack2):
            self.stack1.append(self.stack2.pop())

        return peek_element
    def empty(self) -> bool:
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()