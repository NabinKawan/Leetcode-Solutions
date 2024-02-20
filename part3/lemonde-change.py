class Solution:
    def lemonadeChange(self, bills):
      self.queue = []
      for bill in bills:
        print(self.queue)
        if bill == 5 :
          self.queue.append(bill)
        else:
          change_return = self._change_possible_(bill)
          if change_return:
            self.queue.append(bill)
          else:
            return False
        self.queue.sort()
      print(self.queue)
      return True

    def _change_possible_(self , bill):
      change_to_return = bill - 5
      returned_change = 0
      for i in range(len(self.stack)):
        pass

      return False

test = Solution()
print(test.lemonadeChange([5,5,5,10,20]))