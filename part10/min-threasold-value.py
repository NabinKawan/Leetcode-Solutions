class Solution(object):
    def minOperations(self, nums, k):
        operations = 0
        if nums == []:
            return 0
        nums.sort()
        while True:
            num = nums.pop(0)
            if num >= k:
                break
            else:
                operations +=1
        return operations
