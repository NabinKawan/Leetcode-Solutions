class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[0]*nums[1]*nums[2] , nums[-1]*nums[-2]*nums[-3])


test = Solution()
print(test.maximumProduct([-1,-2,-3]))