class Solution:
    def findLengthOfLCIS(self, nums):
      if nums == []:
        return None
      i = 0
      j = 0
      max_index = len(nums)-1
      while i != max_index-1 or j != max_index-1:
        if nums[i] < nums[i+1]:
          i += 1
        else:
          j += 1