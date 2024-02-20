class Solution:
    def intersection(self, nums):
      result = []
      for num in nums[0]:
        exist = True
        for arr in nums:
          if num not in arr:
            exist = False
            break
        if exist:
         result.append(num)
      result.sort()
      return result

test = Solution()
print(test.intersection([[3,1,2,4,5,-1],[-1,1,2,3,4],[-1,3,4,5,6]]))