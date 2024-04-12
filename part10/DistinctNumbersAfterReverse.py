class Solution(object):
    def countDistinctIntegers(self, nums):
        reversed_number = [int(str(num)[::-1] )for num in nums]
        nums += reversed_number
        return len(set(nums))
