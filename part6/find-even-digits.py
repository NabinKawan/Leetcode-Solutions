class Solution:
    def findNumbers(self, nums):
      self.even_nums = 0
      for num in nums:
        if len(str(num))%2 == 0:
          self.even_nums += 1
      return self.even_nums

test = Solution()
#print(test.findNumbers([12,345,2,6,7896]))
print(test.findNumbers([437,315,322,431,686,264,442]))