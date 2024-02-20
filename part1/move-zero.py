class Solution(object):
    def moveZeroes(self, nums):
        for item in nums:
          if item == 0:
            nums.append(item)
            nums.remove(item)



test = Solution()
test.moveZeroes([1,0,0,2,3])