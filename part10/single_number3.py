class Solution(object):
    def singleNumber(self, nums):
        result = []
        for num in nums:
            if num in result:
                result.remove(num)
            else:
                result.append(num)
        return result
        