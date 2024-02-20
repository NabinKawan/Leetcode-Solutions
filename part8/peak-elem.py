class Solution:
    def findPeakElement(self, nums):
        self.list = [i for i in range(1 , len(nums)- 1) if nums[i] > nums[i-1] and nums[i] > nums[i+1]]
        if len(self.list) == 0:
          return None
        else:
          return self.list[0]



test = Solution()
test.findPeakElement( [1,2,3,1])