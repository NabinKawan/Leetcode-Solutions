class Solution:
    def runningSum(self, nums):
      result = []
      for i in range(len(nums)):
        if i == 0:
          result.append(nums[i])
        else:
          result.append(nums[i]+result[i-1])
      return result

test = Solution()
print(test.runningSum([3,1,2,10,1]))