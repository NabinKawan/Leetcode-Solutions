class Solution(object):
    def addTwoNumbers(self, l1, l2):
      self.l1 = l1
      self.l2 = l2
      num1 =''
      num2 = ''
      final_list = []
      for item in self.l1:
          num1+= str(item)
      for item in self.l2:
        num2+= str(item)
      finalnum = int(num1)+int(num2)
      for item in reversed(str(finalnum)):
        final_list.append(int(item))
      return final_list

TestCase1 = Solution()
TestCase2 = Solution()
TestCase3 = Solution()

print(TestCase1.addTwoNumbers([2,4,3],[5,6,4]))