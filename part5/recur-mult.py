class Solution:
    def findFinalValue(self, nums, original):
      if original not in nums:
        return original
      else:
        return self.findFinalValue(nums , original*2)

test = Solution()
print(test.findFinalValue([5,3,6,1,12],3))