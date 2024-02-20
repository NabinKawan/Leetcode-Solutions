class Solution:
    def missingNumber(self, nums):
      nums = set(nums)
      for i in range(len(nums)):
        if i not in nums:
          return i