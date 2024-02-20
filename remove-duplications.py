class Solution(object):
    def removeDuplicates(self, nums):
       for item in nums:
        current_num = item
        for item in nums[inde::]:
          if current_num == item:
            pass
            
       return nums
        
test = Solution()
print(test.removeDuplicates([1,1,2]))