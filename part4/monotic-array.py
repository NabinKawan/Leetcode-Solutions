class Solution:
    def isMonotonic(self, nums):
      if len(nums) == 1:
        return True
      increasing = self._check_pattern_(nums)
      if increasing:
        for i in range(len(nums)-1):
          if nums[i] > nums[i+1]:
            return False
        return True
      else:
        for i in range(len(nums)-1):
          if nums[i] < nums[i+1]:
            return False
        return True
    
    def _check_pattern_(self , nums):
      first_number = nums[0]
      second_number = 0
      for i in range(len(nums)):
        if nums[i] != first_number:
          second_number = nums[i]
          break
      if first_number < second_number:
        return True
      else:
        return False

test = Solution()
#print(test.isMonotonic([6,5,4,4]))
#print(test.isMonotonic([1,2,3,4,1]))
#print(test.isMonotonic([1,2,2,3]))
print(test.isMonotonic([1,3,2]))
  