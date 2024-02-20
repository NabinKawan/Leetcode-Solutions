class Solution:
    def arrayPairSum(self, nums):
     nums.sort()
     nums_list = []
     i = 0
     total_sum = 0
     while i < len(nums):
      nums_list.append((nums[i] , nums[i+1]))
      i += 2
     for item in nums_list:
      total_sum += min(item[0] , item[1])
     return total_sum 

test = Solution()
test.arrayPairSum([6,2,6,5,1,2])