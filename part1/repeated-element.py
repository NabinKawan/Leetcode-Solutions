class Solution(object):
    def repeatedNTimes(self, nums):
        dict = {}
        for item in nums:
          if item in dict:
            dict[item] += 1
          else:
           dict[item] = 1
    
        for key,value in dict.items():
          if value == len(nums)//2:
            return key

Test = Solution()
print(Test.repeatedNTimes([1,2,2,3]))