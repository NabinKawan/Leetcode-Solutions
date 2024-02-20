class Solution:
    def maxSubArray(self, nums):
      if nums is None:
        return None
      max_num = None
      i = 0
      j = 0
      current_sum = None
      while i!= len(nums) and j != len(nums)+1:
        subarray = nums[i:j]
        sum = self.total_sum(subarray)
        if max_num is None or sum > max_num:
          max_num = sum
          j+=1
        else:
          i+=1
      print(max_num)
      return max_num
    
    def total_sum(self , arr):
      total = 0
      for num in arr:
        total += num
      return total

test = Solution()
print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(test.maxSubArray([5,4,-1,7,8]))