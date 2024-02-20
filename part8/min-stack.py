class MinStack:

    def __init__(self):
        self.list = []

    def push(self, val: int) -> None:
        self.list.append(val)

    def pop(self) -> None:
        return self.list.pop(0)

    def top(self) -> int:
        return self.list[0]

    def getMin(self) -> int:
        return min(self.list)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

test = MinStack()
test.push(-2)
test.push(0)
test.push(-3)
print(test.getMin())
print(test.pop())
print(test.top())
print(test.getMin())


"""
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

output
[null,null,null,null,-3,null,0,-3]

expected 
[null,null,null,null,-3,null,0,-2]
"""