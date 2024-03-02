class MinStack:

    def __init__(self):
      self.list = []
      self.min_index = None 

    def push(self, val: int) -> None:
      self.list.append(val)
      if self.min_index is None or self.list[self.min_index] > val:
        self.min_index = len(self.list) - 1

    def pop(self) -> None:
      item = self.list.pop(-1)
      if len(self.list) != 0 :
       self.min_index = self.list.index(min(self.list))
      else:
        self.min_index = None

    def top(self) -> int:
      return self.list[-1]
        
    def getMin(self) -> int:
        return self.list[self.min_index]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()