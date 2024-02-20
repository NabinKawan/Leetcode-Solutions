class Solution:
    def maxProduct(self, nums):
      max_num1 = max(nums)
      nums.remove(max_num1)
      max_num2 = max(nums)
      return (max_num1-1)*(max_num2-1)

test = Solution()
print(test.maxProduct([3,4,5,2]))