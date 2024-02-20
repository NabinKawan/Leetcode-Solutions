class Solution:
    def evalRPN(self, tokens):
      self.stack = []
      operators = ['+','-','*','/']
      if tokens is None:
        return None
      for elem in tokens:
        if elem in operators:
          num1 = self.stack.pop(-2)
          num2 = self.stack.pop(-1)
          self.stack.append(str(eval(f"{num1} {elem} {num2}")))
        else:
          self.stack.append(elem)
      return float(self.stack[0]).__ceil__()


test = Solution()
print(test.evalRPN(["2","1","+","3","*"]))
print(test.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

