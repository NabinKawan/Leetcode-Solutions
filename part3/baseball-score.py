class Solution:
    def calPoints(self, operations):
      self.operations = operations
      self.stack = []
      for item in self.operations:
        print(self.stack)
        if self.stack == []:
          self.stack.append(int(item))
        else:
          self.compare_to_stack(item)
      
      final_sum = 0
      for items in self.stack:
        final_sum += items
      
      return final_sum

    def compare_to_stack(self,value):
      if value == 'C':
        self.stack.pop(-1)
      elif value == 'D':
        self.stack.append(self.stack[-1]*2)
      elif value == '+':
        tmp = self.stack[-1] + self.stack[-2]
        self.stack.append(tmp)
      else:
        self.stack.append(int(value))
    

test = Solution()
test.calPoints(["5","2","C","D","+"])