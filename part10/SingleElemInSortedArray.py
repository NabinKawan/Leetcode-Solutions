class Solution(object):
    def singleNonDuplicate(self, nums):

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 0:
            return None
        
        if nums[0] != nums[1]:
            return nums[0]

        index = 0
        while True:
            if index == len(nums) - 1:
                return nums[index]
            if nums[index] != nums[index-1] and nums[index] != nums[index + 1]:
                return nums[index]
            index+= 1
