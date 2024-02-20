class Solution:
    def sortColors(self, nums):
      for i in range(len(nums)):
        min_number = nums[i]
        current_min_index = i
        for j in range(i , len(nums)):
          if nums[j] < min_number:
            min_number = nums[j]
            current_min_index = j
        nums[i] , nums[current_min_index] = nums[current_min_index] , nums[i]
      
  
test = Solution()

test.sortColors([2,0,2,1,1,0])