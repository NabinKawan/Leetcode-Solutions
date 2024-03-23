class Solution(object):
    def minMoves2(self, nums): 
        nums.sort()
        if len(nums) == 0:
            return None
        median = None
        if len(nums) % 2 == 0:
            median = ((len(nums) / 2) + ((len(nums) / 2 ) + 1)) /2
        else:
            median = len(nums)// 2
        total = 0
        for i in range(len(nums)):
            if i != median:
                total +=  abs(nums[median] -nums[i])

        return total