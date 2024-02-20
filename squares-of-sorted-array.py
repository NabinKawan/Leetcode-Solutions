class Solution:
    def sortedSquares(self, nums):
      self.final_list = [ ]
      for num in nums:
        self.final_list.append(num*num)
      self.final_list.sort()
      return self.final_list