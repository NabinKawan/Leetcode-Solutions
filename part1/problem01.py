class Solution(object):
    def twoSum(self, nums, target):
       for indx , valx in enumerate(nums):
        for indy , valy in enumerate(nums):
          if valx + valy == target and indx != indy:
            return ([indx , indy])

test1 = Solution()
print(test1.twoSum([3,3],6))