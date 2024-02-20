class Solution:
    def dominantIndex(self, nums):
      max_index = self.find_max(nums)
      nums.sort()
      if nums[-1] >= nums[-2]*2:
        return max_index
      else:
        return -1

    def find_max(self , nums):
      max = 0
      max_index = 0
      for i in range(len(nums)):
        if nums[i] > max:
          max_index = i 
          max = nums[i]
      return max_index


test = Solution()
print(test.dominantIndex([3,6,1,0]))