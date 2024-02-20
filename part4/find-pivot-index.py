class Solution:
    def pivotIndex(self, nums):
      self.nums = nums
      for i in range(len(nums)):
        start_number = self._find_sum(0 , i)
        end_number = self._find_sum(i+1 , len(self.nums))
        if start_number == end_number:
          return i
      return -1
    
    def _find_sum (self ,start , end):
      sum = 0
      for i in range(start, end):
        sum += self.nums[i]
      return sum


test = Solution()
print(test.pivotIndex([1,7,3,6,5,6]))
print(test.pivotIndex([2,1,-1]))