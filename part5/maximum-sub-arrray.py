class Solution:
    def maxSubArray(self, nums):
      nums = set(nums)
      max_sum = 0
      for num in nums:
        if num > 0:
          max_sum += num
      return max_sum