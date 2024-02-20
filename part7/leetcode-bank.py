class Solution:
    def totalMoney(self, n: int) -> int:
      self.total_week = 0
      self.total_sum = 0
      self.days_invested = 0
      self.j = 1
      while self.days_invested != n :
        self.total_sum += self.total_week + self.j
        print(self.total_sum)
        self.j +=1
        self.days_invested += 1
        if self.j %8 == 0:
          self.j = 1
          self.total_week += 1
      return self.total_sum


test = Solution()
test.totalMoney(4)

