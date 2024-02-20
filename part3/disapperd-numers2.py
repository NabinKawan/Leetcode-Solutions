class Solution:
    def findDisappearedNumbers(self, nums):
      nums_set = set(nums )
      disappered_nums = []
      for i in range(1, (len(nums)+1)):
        if i not in nums_set:
          disappered_nums.append(i)
      return disappered_nums