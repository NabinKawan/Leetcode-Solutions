class Solution:
    def findDisappearedNumbers(self, nums):
      disappered_nums = []
      nums.sort()
      last_num = len(nums)
      if last_num not in nums:
        disappered_nums.append(last_num)
      nums = set(nums)
      nums = list(nums)
      for i in range(len(nums)-1):
        biggernum = nums[i+1]
        while biggernum - nums[i] != 1:
          disappered_nums.append (biggernum-1)
          biggernum -= 1 
      print(disappered_nums)
      return disappered_nums


test = Solution()
test.findDisappearedNumbers([4,3,2,7,8,2,3,1])
test.findDisappearedNumbers([1,1])
        