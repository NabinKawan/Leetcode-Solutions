class MyStack(object):

    def __init__(self):
        self.list = []

    def push(self, x):
        self.list.append(x)
        

    def pop(self):
        tmp = self.list[-1]
        self.list.pop(-1)
        return tmp
        

    def top(self):
        return self.list[-1]
        

    def empty(self):
       return self.list == []


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()