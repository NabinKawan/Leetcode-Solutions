class Solution:
    def removeElement(self, nums, val: int) -> int:
      nums.sort()
      for i in range(len(nums)):
        try:
         while nums[i] == val:
          nums.pop(i)
        except:
          pass
      return len(nums)

test = Solution()
test.removeElement([0,1,2,2,3,0,4,2] , 2)
        