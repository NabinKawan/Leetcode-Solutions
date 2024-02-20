class Solution:
    def removeDuplicates(self, nums):
      values = 0
      for i in range(len(nums)):
        try:
         while nums[i] == nums[i+1]:
          item = nums.pop(i+1)
        except:
          pass
      return len(nums)

test = Solution()
print(test.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(test.removeDuplicates([1,1,2]))
print(test.removeDuplicates([1]))