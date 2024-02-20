class Solution(object):
    def removeElement(self, nums, val):
      k = 0
      for item in nums:
        if item == val:
          nums.append(item)
          nums.remove(item)
      
      for i in range(len(nums)):
        if nums[i] == item:
          k = i
          break
      
      return k 


Test = Solution()
print(Test.removeElement([3,2,2,3],3))
