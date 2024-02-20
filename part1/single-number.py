class Solution(object):
    def singleNumber(self, nums):
        dict = {}
        for item in nums:
          if item in dict:
            dict[item] += 1
          else:
            dict[item] = 1
        
        for key,value in dict.items():
          if value == 1:
            return key

Test = Solution()
print(Test.singleNumber([1,2,2,1,3]))