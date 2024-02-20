class Solution:
    def isSameAfterReversals(self, num: int) -> bool:

      if num == 0:
        return True


      new_num = ''
      reversed_num = str(num)[::-1]
      self.reversed_num_list = [reversed_num[i] for i in range(len(reversed_num))]
      self.filter_list()
      for item in self.reversed_num_list:
        new_num += item
      new_num = new_num[::-1]
      if int(new_num) == num:
        return True
      else:
        return False
    

    def filter_list(self):
      i = 0
      while self.reversed_num_list[i] == '0':
        self.reversed_num_list.remove('0')

      


test = Solution()
print(test.isSameAfterReversals(526))
print(test.isSameAfterReversals(1800))
print(test.isSameAfterReversals(0))
print(test.isSameAfterReversals(100000))