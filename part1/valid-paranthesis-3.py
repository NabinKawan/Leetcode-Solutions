class Solution(object):
    def isValid(self, s):
      self.valid_string_format = [('{','}'),('[',']'),('(',')')]
      self.stack = []
      for i in range(len(s)):
        self.append_to_stack(s[i])

      if self.stack == []: return True
      else: return False


    def append_to_stack(self ,value):
      self.stack.insert(0,value)
      if len(self.stack) > 1:
        self._pop_value()

    def _pop_value(self):
      if (self.stack[1],self.stack[0]) in self.valid_string_format:
        self.stack.pop(1)
        self.stack.pop(0)
      
      

TestCase1 = Solution()
print(TestCase1.isValid("()"))#true
print(TestCase1.isValid("()[]{}"))#true
print(TestCase1.isValid("()[{}"))#true