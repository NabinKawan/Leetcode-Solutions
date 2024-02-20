class Solution(object):
    def containsDuplicate(self, nums):
      if len(set(nums)) < len(nums):
        return True
      else:
        return False


Test = Solution()
print(Test.containsDuplicate([1,2,3,4,1]))
        