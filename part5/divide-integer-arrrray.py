class Solution:
    def divideArray(self, nums):
      target = len(nums)//2
      nums = sorted(nums)
      print(nums)
      while len(nums) != 0:
        if nums[0] == nums[1]:
          nums.pop(0)
          nums.pop(0)
        else:
          return False
      return True


test = Solution()
print(test.divideArray([3,2,3,2,2,2]))