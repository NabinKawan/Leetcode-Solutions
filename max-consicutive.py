class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
      all_null = self.check_if_all_null(nums)
      if all_null:
        return 0
      max_num = 0
      for i in range(len(nums)):
        current_max_num = 1
        while i+1 != len(nums) and nums[i] == nums[i+1]:
            current_max_num +=1
            i += 1
        if current_max_num > max_num:
            max_num = current_max_num
      return max_num
    
    def check_if_all_null(self,nums):
      for item in nums:
        if item != 0:
          return False
      return True

  
test = Solution()
print(test.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(test.findMaxConsecutiveOnes([1,0,1,1,0,1]))
print(test.findMaxConsecutiveOnes([0,0,0]))