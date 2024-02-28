class Solution:
    def findMin(self, nums):
      if len(nums) == 0:
        return None
      min_indx = None
      for i in range(len(nums)):
        if min_indx is None or nums[min_indx] < nums[i]:
          min_indx = i
      
      return min_indx + 1





test = Solution()
